import pandas as pd
import pyodbc
import threading
from queue import Queue
from config_sql import SQL_SERVER_CONFIG
from datetime import datetime
import time
import os
import csv

class ParallelInserter:
    def __init__(self, table_name, df, clm_table, source_file, batch_size=2000, max_threads=5):
        self.table_name = table_name
        self.df = df.fillna("") 
        self.source_file = source_file
        self.batch_size = batch_size
        self.max_threads = max_threads
        self.queue = Queue()
        self.lock = threading.Lock()
        self.colunas = clm_table

        self.conn_str = (
            f"DRIVER={SQL_SERVER_CONFIG['driver']};"
            f"SERVER={SQL_SERVER_CONFIG['server']};"
            f"DATABASE={SQL_SERVER_CONFIG['database']};"
            f"UID={SQL_SERVER_CONFIG['username']};"
            f"PWD={SQL_SERVER_CONFIG['password']}"
        )

        # Prepara log
        data_str = datetime.now().strftime("%Y-%m-%d")
        self.log_path = f"logs/inserts_{table_name.lower()}_{data_str}.csv"
        os.makedirs("logs", exist_ok=True)

    def _worker(self):
        conn = pyodbc.connect(self.conn_str)
        cursor = conn.cursor()
        cursor.fast_executemany = True  # ganho real aqui!

        while not self.queue.empty():
            lote_num, batch = self.queue.get()
            try:
                start = time.time()
                placeholders = ",".join(["?"] * len(batch[0]))
                columns = self.colunas
                sql = f"INSERT INTO {self.table_name} ({columns}) VALUES ({placeholders})"
                cursor.executemany(sql, batch)
                conn.commit()
                elapsed = round(time.time() - start, 4)
                
            except Exception as e:
                print(f"[ERRO] Lote {lote_num} falhou: {e}")
                conn.rollback()
            self.queue.task_done()

        cursor.close()
        conn.close()

    def run(self):
        if self.df.empty:
            print("[INFO] DataFrame vazio.")
            return

        # Escreve cabeçalho do log
        if not os.path.exists(self.log_path):
            with open(self.log_path, mode="w", newline="", encoding="utf-8") as log_file:
                writer = csv.writer(log_file)
                writer.writerow(["arquivo", "lote", "registros", "tempo_segundos", "data_hora"])

        total = len(self.df)
        for i in range(0, total, self.batch_size):
            lote_num = (i // self.batch_size) + 1
            batch = self.df.iloc[i:i + self.batch_size].values.tolist()
            self.queue.put((lote_num, batch))

        threads = []
        for _ in range(self.max_threads):
            t = threading.Thread(target=self._worker)
            t.start()
            threads.append(t)

        self.queue.join()
        for t in threads:
            t.join()

        print("[FINALIZADO] Inserção paralela concluída.")

    def close(self):
        self.cursor.close()
        self.conn.close()
