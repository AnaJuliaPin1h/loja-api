# 🛒 Loja API

API REST de gerenciamento de produtos construída com **Django REST Framework** e autenticação **JWT**.

## 🚀 Tecnologias

- Python 3.14
- Django 6.0
- Django REST Framework
- Simple JWT
- Gunicorn
- WhiteNoise
- SQLite (desenvolvimento)

## 📦 Instalação local

```bash
# Clone o repositório
git clone https://github.com/AnaJuliaPin1h/loja-api.git
cd loja-api

# Crie e ative o ambiente virtual
python -m venv venv
.\venv\Scripts\Activate.ps1   # Windows
source venv/bin/activate       # Linux/macOS

# Instale as dependências
pip install -r requirements.txt

# Configure as variáveis de ambiente
# Crie um arquivo .env na raiz com:
# SECRET_KEY=sua_secret_key
# DEBUG=True

# Aplique as migrações
python manage.py migrate

# Crie o superusuário
python manage.py createsuperuser

# Rode o servidor
python manage.py runserver
```

## 🌎 API em produção

```
https://loja-api-rz9i.onrender.com
```

## 🔑 Autenticação

A API utiliza JWT. Para acessar os endpoints protegidos:

**1. Gerar o token:**
```http
POST /api/v1/auth/token/
Content-Type: application/json

{
  "username": "seu_usuario",
  "password": "sua_senha"
}
```

**2. Usar o token nas requisições:**
```http
Authorization: Bearer <seu_access_token>
```

## 📋 Endpoints

| Método | Endpoint | Descrição | Auth |
|--------|----------|-----------|------|
| GET | `/` | Página inicial da API | ❌ |
| POST | `/api/v1/auth/token/` | Gera token JWT | ❌ |
| POST | `/api/v1/auth/token/refresh/` | Renova o token | ❌ |
| GET | `/api/v1/products/` | Lista todos os produtos | ✅ |
| POST | `/api/v1/products/` | Cria um produto | ✅ |
| GET | `/api/v1/products/<id>/` | Busca um produto | ✅ |
| PUT | `/api/v1/products/<id>/` | Atualiza um produto | ✅ |
| DELETE | `/api/v1/products/<id>/` | Remove um produto | ✅ |

## 📄 Modelo de Produto

```json
{
  "id": 1,
  "name": "Camiseta Branca",
  "description": "100% algodão tamanho M",
  "price": "49.90",
  "stock": 100,
  "active": true
}
```

## 🗂️ Estrutura do projeto

```
loja_api/
├── store/                  # Configurações do projeto
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── products_api/           # App de produtos
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   └── admin.py
├── manage.py
├── requirements.txt
├── build.sh                # Script de build para o Render
└── .gitignore
```

## ☁️ Deploy

O projeto está configurado para deploy no **Render**. O arquivo `build.sh` executa automaticamente:

1. Instalação das dependências
2. Coleta de arquivos estáticos
3. Aplicação das migrações

## 👩‍💻 Autora

Ana Julia — [github.com/AnaJuliaPin1h](https://github.com/AnaJuliaPin1h)
