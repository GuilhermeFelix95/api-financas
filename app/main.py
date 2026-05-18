# main.py - Ponto de entrada da API
# Aqui a gente cria a aplicação FastAPI e registra todas as rotas

from fastapi import FastAPI
from app.database import engine, Base
from app.models import Usuario, Transacao, Categoria
from app.routes import transactions, categories, auth  # Importa os routers

# Cria as tabelas no banco quando a API inicia
Base.metadata.create_all(bind=engine)

# Cria a instância da aplicação
app = FastAPI(
    title="API de Finanças Pessoais",
    description="Uma API simples para gerenciar suas finanças pessoais",
    version="1.0.0"
)


# Registra os routers na aplicação principal
app.include_router(auth.router)
app.include_router(transactions.router)
app.include_router(categories.router)


# Rota básica só pra testar se a API tá funcionando
@app.get("/")
def root():
    """Rota raiz - só pra confirmar que a API tá no ar"""
    return {"mensagem": "API de Finanças Pessoais funcionando!"}


# Rota de health check
@app.get("/health")
def health_check():
    """Verifica se a API está saudável"""
    return {"status": "ok"}
