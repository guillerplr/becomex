# 📦 Projeto (projetocbx)

Pipeline de Dados e API para Monitoramento de Empresas (CNPJ

---

## 📌 Visão Geral

Pipeline de dados desenvolvido para coletar, processar e disponibilizar dados públicos de empresas a partir da base da Receita Federal.

A solução automatiza a identificação de empresas relevantes por segmento (CNAE) e disponibiliza os dados via API para consumo por sistemas externos.

## 🎯 Problema

Empresas que dependem de dados atualizados de mercado precisam lidar com:

- Bases públicas extremamente grandes (milhões de registros)  
- Dados fragmentados em múltiplas tabelas  
- Dificuldade de identificar empresas relevantes rapidamente  

## 💡 Solução

Desenvolvimento de um pipeline ETL que:

- Realiza download automatizado da base pública de CNPJs  
- Filtra empresas por CNAE (segmentação de mercado)  
- Integra múltiplas fontes de dados (empresas, sócios, CNAE, etc.)  
- Disponibiliza os dados através de API REST com autenticação  

## 🏗️ Arquitetura

ETL dividido em 3 etapas:

- **Extract:** download dos dados públicos da Receita Federal  
- **Transform:** limpeza, padronização e integração das tabelas  
- **Load:** armazenamento em SQL Server e exposição via API  

## ⚙️ Tecnologias Utilizadas

- Python  
- SQL Server  
- APIs REST  
- JWT (autenticação)  
- Docker  

## 🚀 Funcionalidades

- Listagem de empresas  
- Busca por CNPJ  
- Filtro por data de atividade  
- Integração com sistemas externos via API  
- Autenticação com JWT  

## 📡 Exemplo de Resposta

```json
{
  "cnpj": "12345678901234",
  "razaoSocial": "Empresa Exemplo LTDA",
  "municipio": "São Paulo",
  "cnaePrincipal": "6201500"
}
```

## ⚠️ Desafios Técnicos
- Processamento de bases com dezenas de milhões de registros
- Otimização de performance com filtragem por CNAE
- Integração eficiente de múltiplas tabelas relacionais

## 📈 Resultado
- Automação completa do processo de coleta e análise de dados
- Redução de trabalho manual
- Dados estruturados prontos para consumo


▶️ Como rodar rapidamente

```git clone <repo>
cd cnpj-data-pipeline-api

docker run -e "ACCEPT_EULA=Y" --name db_bcx -e "MSSQL_SA_PASSWORD=SuaSenha" -p 1433:1433 -d mcr.microsoft.com/mssql/server:2022-latest

pip install -r requirements.txt
python main.py
```
---
# ⚙️ Configuração

## 📌 Pré-requisitos

- **Python 3.10+**
- **Docker instalado e funcionando**
- **Git instalado**

## 🧪 1. Subindo o SQL Server com Docker

O projeto depende de uma instância SQL Server. Use o comando abaixo para baixar a imagem e subir o container:

```bash
docker run -e "ACCEPT_EULA=Y" --name db_bcx -e "MSSQL_SA_PASSWORD=D3v5fs4df4fs0123" -p 1433:1433 -d mcr.microsoft.com/mssql/server:2022-latest
```

Após o container estar rodando, é necessário executar o script SQL localizado na pasta scripts/ para criar as tabelas e dados iniciais.

⚠️ Atenção: Certifique-se de que o banco foi criado corretamente antes de rodar o projeto.

## 🔐 2. Configuração de Ambiente

**Crie um ambiente virtual e ative:** (recomendado):
```bash
# Linux/macOS
python3 -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate
```

## ⚙️ 3. Instalando as dependências do projeto

***Com o ambiente virtual ativado, instale as bibliotecas necessárias com o comando abaixo:***

```bash
 pip install -r requirements.txt
```

## 📩 4. Configurando credenciais de e-mail

Renomeie arquivo chamado  `env` para `.env` na raiz do projeto e adicione suas credenciais de envio de e-mail no seguinte formato:

```env
SMTP_SERVER = smtp.gmail.com
SMTP_PORT = 587
SMTP_USERNAME = seu_email@gmail.com
SMTP_PASSWORD = 'senha'
```
