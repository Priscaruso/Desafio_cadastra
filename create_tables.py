from app.database import engine
from app.models import Base

# Cria as tabelas de forma física no banco
def create_tables():
    Base.metadata.create_all(bind=engine)
    print("Tabelas criadas com sucesso!")

if __name__== "__main__":
    create_tables()