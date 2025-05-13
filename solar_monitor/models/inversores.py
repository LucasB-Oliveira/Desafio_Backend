#Tabelas do Banco de Dados
from sqlalchemy import Column, Integer, String         # Importa classes do SQLAlchemy para definir colunas e tipos de dados
from models.base import Base                           # Importa a base declarativa


 #TABELA DE INVERSORES
class Inversor(Base):
    __tablename__ = 'inversores'
    id = Column(Integer, primary_key=True, index=True)
    usina_id = Column(Integer, index=True)
    nome = Column(String, index=True)