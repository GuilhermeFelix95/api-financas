# API de Finanças Pessoais

API REST para gerenciar receitas e despesas, feita com FastAPI e SQLite.

Este projeto foi feito para meu portfólio e mostra como criar uma API com autenticação JWT, banco de dados e CRUD completo.

## Tecnologias usadas

- Python 3.12
- FastAPI
- SQLAlchemy (ORM)
- SQLite
- Pydantic (validação)
- JWT (autenticação)
- Bcrypt (hash de senha)

## Como rodar

Primeiro instala as dependências:

```
pip install -r requirements.txt
```

Depois roda a API:

```
uvicorn app.main:app --reload
```

A API vai rodar em http://localhost:8000

A documentação automática (Swagger) fica em http://localhost:8000/docs — dá pra testar os endpoints direto pelo navegador.

## O que a API faz

### Autenticação

- `POST /auth/register` — cria uma conta nova
- `POST /auth/login` — faz login e retorna o token JWT
- `GET /auth/me` — mostra os dados do usuário logado (precisa estar autenticado)

### Categorias

- `GET /categories` — lista todas as categorias
- `POST /categories` — cria uma categoria nova
- `PUT /categories/{id}` — atualiza uma categoria
- `DELETE /categories/{id}` — deleta uma categoria

### Transações

Todas as rotas de transação precisam de autenticação (token JWT no header).

- `GET /transactions` — lista as transações do usuário logado. Dá pra filtrar por tipo passando `?tipo=receita` ou `?tipo=despesa`
- `GET /transactions/{id}` — busca uma transação pelo ID
- `POST /transactions` — cria uma transação nova
- `PUT /transactions/{id}` — atualiza uma transação
- `DELETE /transactions/{id}` — deleta uma transação

## Como usar a autenticação

1. Cria uma conta mandando um POST pra `/auth/register` com nome, email e senha
2. Faz login no `/auth/login` com email e senha — vai voltar um token
3. Usa esse token nos próximos requests no header: `Authorization: Bearer <token>`

Ou se preferir, abre o Swagger em `/docs` e clica no cadeado no topo pra colocar o token lá.

## Estrutura do projeto

```
api-financas/
├── app/
│   ├── main.py           # ponto de entrada da API
│   ├── database.py       # configuração do banco de dados
│   ├── models.py         # tabelas (Usuario, Transacao, Categoria)
│   ├── schemas.py        # validação dos dados com Pydantic
│   ├── auth.py           # funções de autenticação JWT
│   ├── seed.py           # script pra criar categorias padrão
│   └── routes/
│       ├── auth.py       # rotas de login e registro
│       ├── transactions.py  # rotas de transações
│       └── categories.py    # rotas de categorias
├── requirements.txt
└── README.md
```

## O que aprendi fazendo esse projeto

- Como criar uma API REST com FastAPI
- Como usar SQLAlchemy pra criar tabelas e fazer queries
- Como funciona autenticação com JWT (criar token, validar, proteger rotas)
- Como hashear senhas com bcrypt
- Como organizar o projeto em arquivos separados (models, schemas, routes)
