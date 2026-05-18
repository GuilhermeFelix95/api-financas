# API de Finanças Pessoais 💰

Uma API REST simples para gerenciar finanças pessoais, construída com Python e FastAPI.

## 📌 Sobre o Projeto

Projeto de portfólio para demonstrar habilidades em:
- APIs REST com FastAPI
- Banco de dados com SQLAlchemy
- Autenticação com JWT
- CRUD completo

## 🛠️ Tecnologias

- **Python 3.11+**
- **FastAPI** — Framework web
- **SQLAlchemy** — ORM
- **SQLite** — Banco de dados
- **Pydantic** — Validação de dados
- **JWT** — Autenticação

## 📁 Estrutura

```
api-financas/
├── app/
│   ├── main.py          # Ponto de entrada
│   ├── database.py      # Configuração do banco
│   ├── models.py        # Tabelas do banco
│   ├── schemas.py       # Validação de dados
│   ├── auth.py          # Autenticação JWT
│   ├── seed.py          # Dados iniciais
│   └── routes/
│       ├── auth.py      # Login e registro
│       ├── transactions.py  # CRUD transações
│       └── categories.py    # CRUD categorias
├── requirements.txt
└── README.md
```

## 🚀 Como Rodar

### 1. Instalar dependências

```bash
pip install -r requirements.txt
```

### 2. Rodar a API

```bash
uvicorn app.main:app --reload
```

### 3. Acessar

- **Swagger UI:** http://localhost:8000/docs
- **ReDoc:** http://localhost:8000/redoc

## 📖 Endpoints

### Autenticação
| Método | Endpoint | Descrição |
|--------|----------|-----------|
| POST | `/auth/register` | Criar conta |
| POST | `/auth/login` | Login |
| GET | `/auth/me` | Meu perfil |

### Categorias
| Método | Endpoint | Descrição |
|--------|----------|-----------|
| GET | `/categories` | Listar todas |
| POST | `/categories` | Criar |
| PUT | `/categories/{id}` | Atualizar |
| DELETE | `/categories/{id}` | Deletar |

### Transações (requer login)
| Método | Endpoint | Descrição |
|--------|----------|-----------|
| GET | `/transactions` | Listar (filtro: `?tipo=receita`) |
| GET | `/transactions/{id}` | Buscar |
| POST | `/transactions` | Criar |
| PUT | `/transactions/{id}` | Atualizar |
| DELETE | `/transactions/{id}` | Deletar |

## 🔐 Como usar

### 1. Criar conta
```json
POST /auth/register
{
  "nome": "João",
  "email": "joao@email.com",
  "senha": "123456"
}
```

### 2. Login
```json
POST /auth/login
{
  "email": "joao@email.com",
  "senha": "123456"
}
```

### 3. Usar token
```
Authorization: Bearer <token>
```

---

Desenvolvido para portfólio pessoal
