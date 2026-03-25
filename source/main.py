import asyncio
import aiohttp
from bs4 import BeautifulSoup
from download import baixar_arquivo
from database import conectar_banco, salvar_no_sql
from manipula_arquivo import processar_arquivos, inserir_dados_banco
from transforma_dados import realiza_transformacao_dados
from notificacao import enviar_notificacao
import time

BASE_URL = "https://arquivos.receitafederal.gov.br/dados/cnpj/dados_abertos_cnpj/2025-04/"
MES_PASTA = "2025-04"

HEADERS = {
    "User-Agent": "Mozilla/5.0"
}

async def get_links():

     async with aiohttp.ClientSession(headers=HEADERS) as session:
        async with session.get(BASE_URL) as resp:
            html = await resp.text()
            soup = BeautifulSoup(html, "html.parser")

            tamanho = 0
            links = []      

            for a in soup.find_all('a'):
                href = a['href']
                if href.endswith(".zip"):
                    full_link = BASE_URL + href
                    nome = href
                  
                    links.append(full_link)

            return links

async def main():
    # Conexão com banco
    conn = conectar_banco()
    if conn is None:
        print("Falha ao conectar no banco. Abortando o processo.")
        return

    links = await get_links()
    print(f"{len(links)} links encontrados. Iniciando download...")

    resultados = []   
    async with aiohttp.ClientSession() as session:
        tarefas = [baixar_arquivo(session, url) for url in links]
        resultados = await asyncio.gather(*tarefas) 
  
    for nome_arquivo, link, tamanho, tempo in resultados:     
           
        if nome_arquivo is not None:
            print(nome_arquivo, link, tamanho, tempo)
            salvar_no_sql(conn, MES_PASTA, nome_arquivo, link, tamanho, tempo)
        else:
            #print(f"⚠️ Ignorado no salvamento: {nome_arquivo}")
            pass

    if conn:
        conn.close()

if __name__ == "__main__":
    start_global = time.time()
    asyncio.run(main())
    #print('Processamento dos arquivos')
    processar_arquivos()
    conn = conectar_banco()
    inserir_dados_banco(conn)
    conn.close()

    #  Transformação dos dados
    realiza_transformacao_dados()   

    # Envia e-mail
    enviar_notificacao()

    # Marca o tempo de término
    fim_global = time.time()
        
    # Calcula a duração
    tempo_total = fim_global - start_global
    print(f"✅ Tempo: {tempo_total:.2f} segundos")
