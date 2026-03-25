# Exemplos de Uso da API Becomex

## Autenticação

### Login
```http
POST /auth/login
Content-Type: application/json

{
    "email": "usuario@exemplo.com",
    "senha": "senha123"
}
```

**Resposta:**
```json
{
    "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
    "refresh_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
}
```

## Empresas

### Listar Todas as Empresas
```http
GET /empresas/listar
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
```

**Resposta:**
```json
[
    {
        "UF": "SP",
        "cnaePrincipal": "6201500",
        "cnpj": "12345678901234",
        "dataInicioAtividade": "2020-01-01",
        "data_cadastro": "2023-01-01T10:00:00",
        "excluido": false,
        "municipio": "São Paulo",
        "razaoSocial": "Empresa Exemplo LTDA",
        "nomeFantasia": "Empresa Exemplo",
        "socios": [
            {
                "nomeSocio": "João Silva",
                "qualificacao": "Sócio-Administrador",
                "cnpjBasico": "12345678"
            }
        ],
        "cnaes_secundario": [
            {
                "Codigo": "6202300",
                "Descricao": "Desenvolvimento de sistemas"
            }
        ]
    }
]
```

### Buscar Empresa por CNPJ
```http
GET /empresas/listar?cnpj=12345678901234
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
```

### Buscar Empresas por Data de Início
```http
GET /empresas/listar?dataInicioAtividade=2023-01-01
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
```

## E-mails

### Cadastrar Novo E-mail
```http
POST /emails
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
Content-Type: application/json

{
    "email": "contato@empresa.com",
    "nome": "Contato Empresa",
    "telefone": "11999999999"
}
```

**Resposta:**
```json
{
    "id": 1,
    "email": "contato@empresa.com",
    "nome": "Contato Empresa",
    "telefone": "11999999999",
    "data_cadastro": "2024-03-20T10:00:00"
}
```

### Listar E-mails
```http
GET /emails
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
```

## Exemplos de Uso com cURL

### Autenticação
```bash
curl -X POST http://localhost:5000/auth/login \
  -H "Content-Type: application/json" \
  -d '{"email": "usuario@exemplo.com", "senha": "senha123"}'
```

### Listar Empresas
```bash
curl -X GET http://localhost:5000/empresas/listar \
  -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
```

### Buscar Empresa por CNPJ
```bash
curl -X GET "http://localhost:5000/empresas/listar?cnpj=12345678901234" \
  -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
```

### Buscar Empresas por Data
```bash
curl -X GET "http://localhost:5000/empresas/listar?dataInicioAtividade=2023-01-01" \
  -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
```

## Exemplos de Uso com Python (requests)

```python
import requests

# Configuração
base_url = "http://localhost:5000"
headers = {
    "Content-Type": "application/json"
}

# Login
def login(email, senha):
    response = requests.post(
        f"{base_url}/auth/login",
        json={"email": email, "senha": senha}
    )
    return response.json()

# Obter token
auth_data = login("usuario@exemplo.com", "senha123")
headers["Authorization"] = f"Bearer {auth_data['access_token']}"

# Listar empresas
def listar_empresas():
    response = requests.get(
        f"{base_url}/empresas/listar",
        headers=headers
    )
    return response.json()

# Buscar empresa por CNPJ
def buscar_empresa_cnpj(cnpj):
    response = requests.get(
        f"{base_url}/empresas/listar",
        params={"cnpj": cnpj},
        headers=headers
    )
    return response.json()

# Buscar empresas por data
def buscar_empresas_data(data):
    response = requests.get(
        f"{base_url}/empresas/listar",
        params={"dataInicioAtividade": data},
        headers=headers
    )
    return response.json()
```

## Observações Importantes

1. **Autenticação**
   - Todas as rotas (exceto login) requerem token JWT
   - O token deve ser enviado no header `Authorization`
   - Tokens expiram após 24 horas

2. **Formato de Data**
   - Use o formato ISO: YYYY-MM-DD
   - Exemplo: 2023-01-01

3. **Respostas de Erro**
   - 400: Requisição inválida
   - 401: Não autorizado
   - 404: Recurso não encontrado
   - 500: Erro interno do servidor

4. **Limites**
   - Máximo de 1000 registros por página
   - Timeout de 30 segundos por requisição 