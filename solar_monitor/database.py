from sqlalchemy import create_engine         # Importa a função para criar o mecanismo de conexão do SQLAlchemy
from sqlalchemy.orm import sessionmaker      # Importa a função para criar sessões (cada sessão faz operações no banco)
from models import Base                      # Importa a base declarada no models.py para criarmos as tabelas


SQLALCHEMY_DATABASE_URL = "sqlite:///./metrics.db"                                                 # Define a URL do banco de dados SQLite (o arquivo metrics.db será criado no diretório atual)

engine = create_engine(SQLALCHEMY_DATABASE_URL,                                                     # Cria o mecanismo de conexão usando a URL acima
    connect_args={"check_same_thread": False                                                        # 'check_same_thread=False' é necessário no SQLite para permitir acesso em múltiplas threads
})         

SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)                         # Cria a fábrica de sessões (SessionLocal) para gerenciar operações com o banco

def init_db():
    Base.metadata.create_all(bind=engine)                                                           # Função que inicializa o banco criando as tabelas, caso não existam ainda


def get_db():                                                                                       #Função de dependência para injeção de sessão no FastAPI
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
