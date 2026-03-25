import os
from dotenv import load_dotenv
import pyodbc

# Carrega as variáveis do .env
load_dotenv()

def get_conexao():
    driver = os.getenv("DB_DRIVER")
    server = os.getenv("DB_SERVER")
    database = os.getenv("DB_NAME")
    user = os.getenv("DB_USER")
    password = os.getenv("DB_PASSWORD")    

    conn = pyodbc.connect(
            f"DRIVER={{ODBC Driver 17 for SQL Server}};"
            f"SERVER={server};DATABASE={database};UID={user};PWD={password}"
        )
    return conn  


def validar_processamento_mes(mes):   
    print(mes) 

    conn = get_conexao()
    
    cursor = conn.cursor()

    try:
        query = """
            SELECT COUNT(*) 
            FROM TabLinks 
            WHERE mes = ? 
            --AND status_download = 'Sucesso'
            --AND status_extracao = 'Sucesso'
        """
        cursor.execute(query, (mes,))
        total_processados = cursor.fetchone()[0]
    finally:
        cursor.close()

    return total_processados

