# routes/auth.py - Rotas de autenticação

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import Usuario
from app.schemas import UsuarioCreate, UsuarioResponse, LoginRequest, TokenResponse
from app.auth import hash_senha, verificar_senha, criar_token_acesso, pegar_usuario_atual

router = APIRouter(
    prefix="/auth",
    tags=["Autenticação"]
)


# --- POST /auth/register ---
@router.post("/register", response_model=UsuarioResponse, status_code=201)
def registrar_usuario(usuario_data: UsuarioCreate, db: Session = Depends(get_db)):
    """Cria uma nova conta de usuário"""
    # Verifica se já existe usuário com esse email
    usuario_existente = db.query(Usuario).filter(Usuario.email == usuario_data.email).first()

    if usuario_existente:
        raise HTTPException(status_code=400, detail="Email já cadastrado")

    # Cria o usuário com a senha hasheada
    novo_usuario = Usuario(
        nome=usuario_data.nome,
        email=usuario_data.email,
        senha_hash=hash_senha(usuario_data.senha)
    )

    db.add(novo_usuario)
    db.commit()
    db.refresh(novo_usuario)

    return novo_usuario


# --- POST /auth/login ---
@router.post("/login", response_model=TokenResponse)
def fazer_login(login_data: LoginRequest, db: Session = Depends(get_db)):
    """Faz login e retorna um token JWT"""
    # Busca o usuário pelo email
    usuario = db.query(Usuario).filter(Usuario.email == login_data.email).first()

    # Se não achou ou a senha tá errada
    if not usuario or not verificar_senha(login_data.senha, usuario.senha_hash):
        raise HTTPException(status_code=401, detail="Email ou senha incorretos")

    # Cria o token
    token = criar_token_acesso(dados={"sub": usuario.email})

    return {"access_token": token, "token_type": "bearer"}


# --- GET /auth/me ---
@router.get("/me", response_model=UsuarioResponse)
def pegar_meu_perfil(usuario: Usuario = Depends(pegar_usuario_atual)):
    """Retorna os dados do usuário logado"""
    return usuario
