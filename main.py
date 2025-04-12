import requests
import os
import re
from bs4 import BeautifulSoup

url_base = 'https://arquivos.receitafederal.gov.br/cnpj/dados_abertos_cnpj/2025-03/'
os.makedirs("downloads", exist_ok=True)


def download_zip_files(url):
    try:
        response = requests.get(url)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')
        zip_links = []
        for a_tag in soup.find_all('a', href=True):
            href = a_tag['href']
            if href.endswith('.zip'):
                zip_links.append(url + href)

        if not zip_links:
            print('Nenhum arquivo .zip encontrado na página.')
            return
        for zip_url in zip_links:
            filename = os.path.basename(zip_url)
            caminho = os.path.join("downloads",filename)
            try:
                zip_response = requests.get(zip_url, stream=True)
                zip_response.raise_for_status()
                with open(caminho, 'wb') as file:
                    for chunk in zip_response.iter_content(chunk_size=8192):
                        file.write(chunk)
                print(f'Arquivo {filename} baixado com sucesso.')
            except requests.exceptions.RequestException as e:
                print(f'Erro ao baixar {zip_url}: {e}')
            except IOError as e:
                print(f'Erro ao salvar {caminho}: {e}')

    except requests.exceptions.RequestException as e:
        print(f'Erro ao acessar a página {url}: {e}')
    except Exception as e:
        print(f'Ocorreu um erro inesperado: {e}')

download_zip_files(url_base)
print('Processo de download concluído.')