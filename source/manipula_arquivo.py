from database import conectar_banco, listar_arquivos_extraidos_sucesso
from extractor import DescompactadorArquivos
from mapeamento_json import mapeamento_arquivos
from utils import limpar_nome_arquivo
from parallel_insert import ParallelInserter
import pandas as pd
from pathlib import Path
import os

DOWNLOAD_DIR = "extraidos"

def processar_arquivos():
    try:
        conn = conectar_banco() 
        descompactador = DescompactadorArquivos(conn)
        descompactador.descompactar_todos()        
    finally:
        conn.close()


def inserir_dados_banco(conn): 
    
    resultado  = recuperar_mapeamento_das_tabelas(conn, mapeamento_arquivos)

    # Ordenar do menor para o maior valor
    dados_ordenados = dict(sorted(resultado.items(), key=lambda item: item[1]['sequencia']))

    lista_cnpj = []  
       
    for _chave, info in dados_ordenados.items():
        arq_extraido = info["arq_extraido"]
        tabela = info["tabela"]
        colunas = info["colunas"]
        filtro_cnpj = info["filtro_cnpj"]
        seq = info["sequencia"]
        
        # Verifica se o caminho existe
        caminho_arq = Path(f'{DOWNLOAD_DIR}/{arq_extraido}')
        if caminho_arq.exists():           
            
            df = pd.read_csv(
                caminho_arq,
                header=None, sep=";",
                dtype=str, 
                encoding='ISO-8859-1', 
                names=colunas,
                on_bad_lines='skip'  # Pula linhas com erro
                )            

            # Verificando se o número de colunas está correto
            numero_colunas_lido = df.shape[1] 

            if numero_colunas_lido != len(colunas):
                raise ValueError(f"Erro: Esperado {len(colunas)} colunas, mas o arquivo possui {numero_colunas_lido}.")
            else:
                print("Arquivo lido com sucesso e número de colunas validado.")
           

            if tabela == 'TabEstabelecimentoArquivo':
                # Lista de cnaes para filtrar
                cnaes = ['5250803', '5231102', '5250804']

                # Criar uma expressão regular juntando os cnaes
                regex = '|'.join(cnaes)

                # Filtrar usando str.contains | # Filtrar por LIKE (conteúdo)
                filtro_like = df['teaCnaeSecundario'].str.contains(regex, case=False, na=False)

                # Filtrar por igualdade exata (igualdade)
                filtro_igualdade = df['teaCnaePrincipal'].isin(cnaes)

                # Combinar os filtros (LIKE ou Igualdade)
                filtro_combinado = filtro_like | filtro_igualdade  # '|' é o operador OR
            
                # Aplicar o filtro
                df = df[filtro_combinado]                          

                # Pegando todos os CNPJs numa lista
                # lista_cnpj.append(df['teaCnpjBasico'].tolist())
                lista_cnpj.extend(df['teaCnpjBasico'].drop_duplicates().tolist())

           
            if filtro_cnpj and len(lista_cnpj) > 0 and tabela == 'TabEmpresaArquivo':
                print('Executando tab: ', tabela, filtro_cnpj, len(lista_cnpj))
                filtro_cnpjs_cnes = df['teoCnpjBasico'].isin(lista_cnpj)                
                df = df[filtro_cnpjs_cnes]   
            elif filtro_cnpj and len(lista_cnpj) > 0 and tabela == 'TabSocioArquivo':                
                filtro_cnpjs_cnes = df['tsaCnpjBasico'].isin(lista_cnpj)                
                df = df[filtro_cnpjs_cnes] 
            elif filtro_cnpj and len(lista_cnpj) > 0 and tabela == 'TabSimplesArquivo':                
                filtro_cnpjs_cnes = df['tssCnpjBasico'].isin(lista_cnpj)                
                df = df[filtro_cnpjs_cnes]            


            inserter = ParallelInserter(
                table_name=tabela,
                df=df,
                clm_table = ', '.join(colunas),
                source_file=caminho_arq,
                batch_size=5000,
                max_threads=5
            )
            inserter.run()

            # os.remove(caminho_arq)

        else:
            print(f"O caminho '{caminho_arq}' não existe.")    

def recuperar_mapeamento_das_tabelas(conn, mapeamento_arquivos):
    arquivos = listar_arquivos_extraidos_sucesso(conn)
    mapeamento_resultante = {}  

    for item in arquivos:
        nome_extraido = item["nome_extraido"]
        nome_zip = item["arquivo_original"]
        nome_chave = limpar_nome_arquivo(nome_zip)        

        if nome_chave in mapeamento_arquivos: 
            info = mapeamento_arquivos[nome_chave]
            nova_chave = nome_chave + '_' + nome_extraido
            mapeamento_resultante[nova_chave] = {                
                "tabela": info["tabela"],
                "colunas": info["colunas"],
                "arq_extraido": nome_extraido,
                "sequencia": info["sequencia"],
                "filtro_cnpj": info["filtroCNPJ"]
            }
            #print(info["tabela"], nome_extraido)
        else:
            print(f"Arquivo não mapeado: {nome_chave}")   

    
    return mapeamento_resultante



