import pyodbc
from config_sql import SQL_SERVER_CONFIG

# Dados para conexão com SQL Server
SERVER = SQL_SERVER_CONFIG['server']
DATABASE = SQL_SERVER_CONFIG['database']
USERNAME = SQL_SERVER_CONFIG['username']
PASSWORD = SQL_SERVER_CONFIG['password']

def salvar_no_sql(conn, mes, nome_arquivo, link, tamanho, tempo_download):
    cursor = conn.cursor()  

    try:

        cursor.execute("""
            SELECT COUNT(*) FROM TabLinks
            WHERE mes = ? AND nome_arquivo = ?
        """, (mes, nome_arquivo))
        existe = cursor.fetchone()[0]

        if existe == 0:
            cursor.execute("""
                INSERT INTO TabLinks (mes, nome_arquivo, link, tamanho_arquivo_bytes, tempo_download)
                VALUES (?, ?, ?, ?, ?)
            """, (mes, nome_arquivo, link, tamanho, tempo_download))
            conn.commit()
            print(f"Inserido: {nome_arquivo} | {tamanho:,} bytes | Tempo: {tempo_download:.2f}s")
        else:
            print(f"Já existe no banco: {nome_arquivo}")


    except Exception as e:
        print(f"Erro SQL ({nome_arquivo}): {e}")
        conn.rollback()

    finally:
        if cursor:
            cursor.close()     

def conectar_banco():
    try:
        conn = pyodbc.connect(
            f"DRIVER={{ODBC Driver 17 for SQL Server}};"
            f"SERVER={SERVER};DATABASE={DATABASE};UID={USERNAME};PWD={PASSWORD}"
        )
        return conn
    except Exception as e:
        print(f"Erro ao conectar ao banco: {e}")
        return None
    
def listar_arquivos_baixados(conn):
        cursor = conn.cursor()
        try:
            cursor.execute("""
                SELECT nome_arquivo FROM TabLinks
                WHERE tamanho_arquivo_bytes IS NOT NULL AND tempo_download IS NOT NULL
            """)
            return [row[0] for row in cursor.fetchall()]
        finally:
            cursor.close()

def gravar_extracao(conn, nome_arquivo, status, tempo_extracao, nome_extraido):
    cursor = conn.cursor()
    try:
        cursor.execute("""
            UPDATE TabLinks
            SET status_extracao = ?
                , data_extracao = GETDATE() 
                , tempo_extracao_seg = ?    
                , nome_arquivo_extraido  = ?           
            WHERE nome_arquivo = ?
        """, (status, tempo_extracao, nome_extraido, nome_arquivo))
        conn.commit()
    except Exception as e:
        print(f"Erro ao atualizar status da extração para {nome_arquivo}: {e}")
        conn.rollback()
    finally:
        cursor.close()

def buscar_links_extraidos(conn):
        cursor = conn.cursor()
        try:
            cursor.execute("""
                SELECT nome_arquivo
                FROM TabLinks
                WHERE status_extracao = 'sucesso'
            """)
            return [row[0] for row in cursor.fetchall()]
        finally:
            cursor.close()

def listar_arquivos_extraidos_sucesso(conn):
    cursor = conn.cursor()
    try:
        cursor.execute("""
            SELECT 
                nome_arquivo_extraido,
                nome_arquivo
            FROM TabLinks
            WHERE status_extracao = 'sucesso'
        """)

        resultados = [
            {
                "nome_extraido": row.nome_arquivo_extraido,
                "arquivo_original": row.nome_arquivo
            }
            for row in cursor.fetchall()
        ]
        return resultados
    finally:
        cursor.close()

def inserir_dados_banco_paralelo():
    pass

def chamar_procedure_transform_data():
    nome_proc = 'dbo.proc_TransformacaoDados'
    parametros = None   

    conn = None
    cursor = None
    try:
        conn = conectar_banco()
        cursor = conn.cursor()

        if parametros:          
            placeholders = ','.join('?' for _ in parametros)
            comando = f"EXEC {nome_proc} {placeholders}"
            cursor.execute(comando, parametros)
        else:
            comando = f"EXEC {nome_proc}"
            cursor.execute(comando)

        conn.commit()

        print(f"Procedure {nome_proc} executada com sucesso!")

    except Exception as e:
        print(f"Erro ao executar procedure {nome_proc}: {e}")
        if conn:
            conn.rollback()

    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()






 
