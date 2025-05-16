#Tabelas do Banco de Dados
#Tabelas do Banco de Dados
from sqlalchemy import Column, Integer, String              # Importa classes do SQLAlchemy para definir colunas e tipos de dados
from sqlalchemy.orm import relationship                     # Importa a classe relationship do SQLAlchemy
from models.base import Base                                # Importa a base declarativa

 #TABELA DE USINAS
class Usina(Base):
    __tablename__ = 'usinas'

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)

    inversores = relationship("Inversor", back_populates="usina") # Uma usina tem vários inversores
