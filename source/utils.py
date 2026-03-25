import re
import zipfile

def limpar_nome_arquivo(nome):    
    nome_sem_extensao = nome.replace('.zip', '').strip()    
    nome_limpo = re.sub(r'\d+$', '', nome_sem_extensao)
    return nome_limpo

def verificar_zip(caminho_zip):
    if not zipfile.is_zipfile(caminho_zip):
        return False
    try:
        with zipfile.ZipFile(caminho_zip, 'r') as zip_ref:
            if zip_ref.testzip() is not None:
                return False
        return True
    except zipfile.BadZipFile:
        return False
    
