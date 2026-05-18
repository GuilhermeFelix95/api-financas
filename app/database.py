# database.py - Configuração do banco de dados
# Aqui a gente configura a conexão com o SQLite usando SQLAlchemy

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# URL do banco de dados - SQLite cria um arquivo local
# O "sqlite:///./financas.db" vai criar o arquivo na raiz do projeto
SQLALCHEMY_DATABASE_URL = "sqlite:///./financas.db"

# Cria o engine - é quem gerencia as conexões com o banco
engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False}  # Precisa disso pro SQLite funcionar com FastAPI
)

# SessionLocal é uma fábrica de sessões
# Cada request vai usar uma sessão diferente
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base é a classe base pros nossos models
Base = declarative_base()


# Função pra pegar a sessão do banco
# Vai ser usada como dependência nas rotas
def get_db():
    """
    Gera uma sessão de banco de dados.
    Usa yield pra garantir que a sessão é fechada depois do request.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()  # Fecha a sessão no final
