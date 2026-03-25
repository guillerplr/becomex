import os

def dividir_txt_em_partes(caminho_arquivo, destino_pasta, linhas_por_arquivo=100000):
    os.makedirs(destino_pasta, exist_ok=True)

    arquivos = []

    with open(caminho_arquivo, "r", encoding='ISO-8859-1') as arquivo:
        contador = 0
        parte = 1
        linhas = []

        for linha in arquivo:
            linhas.append(linha)
            contador += 1

            if contador >= linhas_por_arquivo:
                nome_txt_arq = salvar_parte(linhas, destino_pasta, parte)
                parte += 1
                linhas = []
                contador = 0
                arquivos.append(nome_txt_arq)
      
        if linhas:
            nome_txt_arq = salvar_parte(linhas, destino_pasta, parte)
            arquivos.append(nome_txt_arq)
    
    print(f"Arquivo dividido em {parte} parte(s).")

    return arquivos

def salvar_parte(linhas, destino_pasta, parte_num):
    nome_arquivo = os.path.join(destino_pasta, f"parte_{parte_num:04d}.txt")
    with open(nome_arquivo, "w", encoding="utf-8") as f:
        f.writelines(linhas)
    print(f"Parte {parte_num} salva: {nome_arquivo}")

    return nome_arquivo

def listar_arquivos(diretorio: str):
    return [f for f in os.listdir(diretorio) if os.path.isfile(os.path.join(diretorio, f))]


