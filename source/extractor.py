import zipfile
from pathlib import Path
from database import listar_arquivos_baixados, gravar_extracao
import time
import os
import shutil 
from utils import verificar_zip

class DescompactadorArquivos:
    def __init__(self, conn, download_dir="downloads", destino_dir="extraidos"):
        self.conn = conn
        self.download_dir = Path(download_dir)
        self.destino_dir = Path(destino_dir)
        self.destino_dir.mkdir(parents=True, exist_ok=True)
        self.processados_dir = self.download_dir / "processados"        
        self.processados_dir.mkdir(exist_ok=True)
        self.remover_arquivos_downloads = False

    def descompactar_todos(self):
        arquivos = listar_arquivos_baixados(self.conn)
        for nome in arquivos:
            caminho_zip = self.download_dir / nome
            destino = self.destino_dir #/ nome.replace(".zip", "")
            destino.mkdir(exist_ok=True)
            
            #print(destino, caminho_zip)
            if verificar_zip(caminho_zip):
                print(f"Descompactando {nome}...")
                inicio = time.time()
                try:

                    with zipfile.ZipFile(caminho_zip, 'r') as zip_ref:
                        zip_ref.extractall(destino)
                        nomes_extraidos = zip_ref.namelist()

                    # Assumindo que tenha 1 principal (ou pega o primeiro)
                    nome_extraido = nomes_extraidos[0] if nomes_extraidos else "desconhecido"                  
                    tempo_total = time.time() - inicio
                    gravar_extracao(self.conn, nome, "sucesso", tempo_total, nome_extraido)

                    if self.remover_arquivos_downloads:                       
                        os.remove(caminho_zip)
                        print(f"Removido {caminho_zip} da pasta de downloads.")
                    else:                       
                        caminho_destino_zip = self.processados_dir / nome
                        shutil.move(str(caminho_zip), str(caminho_destino_zip))
                        print(f"Movido para: {caminho_destino_zip}") 


                except Exception as e:
                    tempo_total = time.time() - inicio
                    print(f"Falha ao descompactar {nome}: {e}")
                    gravar_extracao(self.conn, nome, "erro", tempo_total, None)
            else:
                print(f"Arquivo não é .zip válido: {nome}")  
