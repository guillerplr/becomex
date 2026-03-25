import schedule
import time
import requests
from datetime import datetime
import os
from bs4 import BeautifulSoup
import sys
from hackdb import validar_processamento_mes

# Adiciona o diretório 'app' ao path
sys.path.append(os.path.join(os.path.dirname(__file__), "source"))

BASE_URL = 'https://arquivos.receitafederal.gov.br/dados/cnpj/dados_abertos_cnpj'


def listar_arquivos(base_url):
    response = requests.get(base_url)

    if response.status_code != 200:
        print(f"Erro ao acessar a URL: {response.status_code}")
        return 0

    soup = BeautifulSoup(response.text, 'html.parser')
    links_encontrados = [a['href'] for a in soup.find_all('a', href=True) if a['href'].endswith('.zip')]   

    return len(links_encontrados)


def existe_mes_atual(ano_mes_formatado):
    url = f'{BASE_URL}/{ano_mes_formatado}/' 
    # Faz o GET
    response = requests.get(url)   
    # Verifica o resultado
    if response.status_code == 200:
        return True           
    else:
        return False
    
def escrever_arquivo(msg):
    with open('log_diario.txt', 'a', encoding='utf-8') as arquivo:
        arquivo.write(msg + "\n")  


def tarefa_diaria():

    inicio = time.time()  # 🕒 Início da contagem    

    data_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    hora_atual = datetime.now().hour

    print(hora_atual)

    ano_mes_formatado = datetime.now().strftime("%Y-%m")
    url = f'{BASE_URL}/{ano_mes_formatado}/' 

    existe_url_mes = existe_mes_atual(ano_mes_formatado)
    total_arq_esperados = listar_arquivos(url)
    total_arq_processados = validar_processamento_mes(ano_mes_formatado)  

    print(f"Tarefa executada em: {data_hora}")
    if existe_url_mes and total_arq_esperados > total_arq_processados and 22 <= hora_atual < 23:
        escrever_arquivo(f'Rotina iniciada: {data_hora}')
    else:
        escrever_arquivo(f'Rotina não iniciada: {data_hora}')
        

    fim = time.time()  # 🕒 Fim da contagem
    duracao = fim - inicio    
    print(f"🕐 Tempo total: {duracao:.2f} segundos.")   

schedule.every(5).minutes.do(tarefa_diaria)

while True:
    schedule.run_pending()
    data_hora_atual = datetime.now()
    print('Em execução .....', data_hora_atual.strftime("%H:%M:%S"), data_hora_atual.strftime("%d/%m/%Y %H:%M:%S"))
    time.sleep(2)