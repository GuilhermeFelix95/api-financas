# auth.py - Funções de autenticação e segurança
# Aqui a gente cuida de hash de senha e geração/validação de tokens JWT

from datetime import datetime, timedelta

from jose import JWTError, jwt
from passlib.context import CryptContext
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import Usuario

# Configurações do JWT
SECRET_KEY = "minha-chave-secreta-super-segura-123"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30  # Token expira em 30 minutos

# Hash de senha com bcrypt
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Esquema de segurança - espera token no header Authorization: Bearer <token>
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")


def hash_senha(senha: str) -> str:
    """Recebe uma senha em texto puro e retorna o hash"""
    return pwd_context.hash(senha)


def verificar_senha(senha_pura: str, senha_hash: str) -> bool:
    """Compara uma senha pura com um hash"""
    return pwd_context.verify(senha_pura, senha_hash)


def criar_token_acesso(dados: dict) -> str:
    """Cria um token JWT com os dados informados"""
    para_copiar = dados.copy()

    # Define quando o token expira (30 minutos)
    expiracao = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    para_copiar.update({"exp": expiracao})

    # Gera o token assinado
    token_codificado = jwt.encode(para_copiar, SECRET_KEY, algorithm=ALGORITHM)
    return token_codificado


def pegar_usuario_atual(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db)
) -> Usuario:
    """
    Dependência que pega o usuário logado pelo token.
    Usa nas rotas que precisam de autenticação.
    """
    try:
        # Decodifica o token
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    except JWTError:
        raise HTTPException(status_code=401, detail="Token inválido")

    # Pega o email do payload
    email = payload.get("sub")
    if email is None:
        raise HTTPException(status_code=401, detail="Token inválido")

    # Busca o usuário no banco
    usuario = db.query(Usuario).filter(Usuario.email == email).first()
    if usuario is None:
        raise HTTPException(status_code=401, detail="Usuário não encontrado")

    return usuario
