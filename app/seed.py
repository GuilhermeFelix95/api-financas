# seed.py - Script pra popular o banco com dados iniciais
# Roda uma vez pra criar categorias padrão no sistema

from app.database import SessionLocal
from app.models import Categoria


def criar_categorias_padrao():
    """Cria categorias comuns de finanças pessoais"""
    db = SessionLocal()

    try:
        # Lista de categorias comuns
        categorias = [
            {"nome": "Alimentação", "descricao": "Supermercado, restaurante, delivery"},
            {"nome": "Transporte", "descricao": "Uber, ônibus, gasolina, estacionamento"},
            {"nome": "Moradia", "descricao": "Aluguel, condomínio, IPTU"},
            {"nome": "Saúde", "descricao": "Plano de saúde, farmácia, consultas"},
            {"nome": "Educação", "descricao": "Curso, livros, assinatura"},
            {"nome": "Lazer", "descricao": "Cinema, streaming, jogos"},
            {"nome": "Salário", "descricao": "Renda mensal"},
            {"nome": "Freelance", "descricao": "Renda extra"},
            {"nome": "Outros", "descricao": "Categoria genérica"},
        ]

        # Verifica se já existe alguma categoria pra não duplicar
        existente = db.query(Categoria).first()
        if existente:
            print("Categorias já existem, pulando seed...")
            return

        # Cria cada categoria
        for cat in categorias:
            nova_categoria = Categoria(nome=cat["nome"], descricao=cat["descricao"])
            db.add(nova_categoria)

        db.commit()
        print(f"{len(categorias)} categorias criadas com sucesso!")

    except Exception as e:
        db.rollback()
        print(f"Erro ao criar categorias: {e}")
    finally:
        db.close()


# Roda o seed se o arquivo for executado diretamente
if __name__ == "__main__":
    criar_categorias_padrao()
