import time
import aiofiles
import aiohttp
from pathlib import Path
from utils import verificar_zip
import os
import async_timeout
import asyncio

# Configuração do diretório de downloads
DOWNLOAD_DIR = Path("downloads")
DOWNLOAD_DIR.mkdir(exist_ok=True)

# Arquivos desejados para download
arquivos_desejados = [    
    "Empresas1.zip",
    "Municipios.zip",    
    "Socios1.zip",
    "Paises.zip",
    "Simples.zip",
    "Estabelecimentos1.zip"
]

async def baixar_arquivo(session, url, tentativas=3):
    nome_arquivo = url.split("/")[-1]
    caminho_arquivo = DOWNLOAD_DIR / nome_arquivo

     # Só baixa se estiver na lista de arquivos desejados
    if nome_arquivo not in arquivos_desejados:
        print(f"Ignorado (não está na lista): {nome_arquivo}")
        return None, url, None, 0.0 
    
    if caminho_arquivo.exists():
        tamanho_local = caminho_arquivo.stat().st_size
        print(f"Já existe: {nome_arquivo}")
        return nome_arquivo, url, tamanho_local, 0.0    
    
    # for tentativa in range(1, tentativas + 1):
    try:

        # Marca o tempo de início
        inicio_download = time.time()            

        async with async_timeout.timeout(360):  # em segundos de timeout
            async with session.get(url) as resp:

                if resp.status == 200:
                    resp.raise_for_status()
                    tamanho = int(resp.headers.get("Content-Length", 0))                 

                    with open(caminho_arquivo, 'wb') as f:
                        while True:
                            chunk = await resp.content.read(1024)
                            if not chunk:
                                break
                            f.write(chunk)
                    # Verifica o zip
                    if verificar_zip(caminho_arquivo):
                        print(f"Download concluído e verificado: {os.path.basename(caminho_arquivo)}")                 
                    else:
                        print(f"Arquivo corrompido: {os.path.basename(caminho_arquivo)}")
                        os.remove(caminho_arquivo)  # Remove o arquivo inválido

                else:
                    print(f"Falha no download: {url} - Status {resp.status}")
                

        # Marca o tempo de término
        fim_download = time.time()
        
        # Calcula a duração
        tempo_download = fim_download - inicio_download
        print(f"Baixado: {nome_arquivo} | Tempo: {tempo_download:.2f} segundos | Tamanho: {tamanho:,} bytes")

        return nome_arquivo, url, tamanho, tempo_download    
    except Exception as e:
        print(f"Erro ao baixar {nome_arquivo}: {e}")
        return nome_arquivo, url, None, None

    