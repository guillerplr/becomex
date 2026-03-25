# 📦 Projeto (projetocbx)

Pipeline de Dados e API para Monitoramento de Empresas (CNPJ)

---

# 📔 Descrição do Projeto

Desenvolvimento de um pipeline de dados completo (ETL) para coleta, processamento e disponibilização de dados públicos de empresas a partir da base da Receita Federal.

O sistema realiza a extração de grandes volumes de dados (milhões de registros), aplica filtros por CNAE para segmentação de mercado e integra múltiplas tabelas relacionais utilizando o CNPJ como chave principal.

Após o processamento, os dados são disponibilizados por meio de uma API REST autenticada (JWT), permitindo consulta de empresas, busca por CNPJ e integração direta com sistemas externos.

## 🎯 Problema

Empresas que dependem de dados atualizados de mercado precisam lidar com:

bases públicas extremamente grandes (milhões de registros)
dados fragmentados em múltiplas tabelas
dificuldade de identificar empresas relevantes rapidamente

## 💡 Solução

Desenvolvimento de um pipeline ETL que:

realiza download automatizado da base pública de CNPJs
filtra empresas por CNAE (segmentação de mercado)
integra múltiplas fontes de dados (empresas, sócios, CNAE, etc.)
disponibiliza os dados através de API REST com autenticação

## 🏗️ Arquitetura

ETL dividido em 3 etapas:

Extract: Download dos dados públicos da Receita Federal
Transform: Limpeza, padronização e integração das tabelas
Load: Armazenamento em banco SQL Server e exposição via API

## ⚙️ Tecnologias Utilizadas
Python
SQL Server
APIs REST
JWT (autenticação)
Docker

## 🚀 Funcionalidades
Listagem de empresas
Busca por CNPJ
Filtro por data de atividade
Integração com sistemas externos via API
Autenticação com JWT

## ⚠️ Desafios Técnicos
Processamento de bases com dezenas de milhões de registros
Otimização de performance através de filtragem por CNAE
Integração eficiente de múltiplas tabelas relacionais

## 📈 Resultado
Automação completa do processo de coleta e análise de dados
Redução de trabalho manual
Disponibilização de dados estruturados prontos para consumo

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
