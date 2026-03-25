# 📦 Projeto (projetocbx)

Repositório contém projetos desenvolvidos para atender demandas práticas da DNC

---

## ⚙️ Pré-requisitos

- **Python 3.10+**
- **Docker instalado e funcionando**
- **Git instalado**

---
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
SMTP_PASSWORD = P55pjNGU7WJp
```

### 🚀 Como clonar o repositório privado

Após aceitar o convite, o colaborador pode clonar o repositório normalmente:

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
```



