#Tabelas do Banco de Dados
from sqlalchemy import Column, Integer, String, ForeignKey       # Importa classes do SQLAlchemy para definir colunas e tipos de dados
from sqlalchemy import relationship                              # Importa a classe relationship
from models.base import Base                                     # Importa a base declarativa


 #TABELA DE INVERSORES
class Inversor(Base):
    __tablename__ = 'inversores'

    id = Column(Integer, primary_key=True, index=True)
    usina_id = Column(Integer, ForeignKey("usinas.id"), index=True)         # Define a chave estrangeira para a tabela de usinas
    nome = Column(String, index=True)

    # Relacionamentos ORM
    usina = relationship("Usina", back_populates="inversores")              # Um inversor pertence a uma usina
    metricas = relationship("Metric", back_populates="inversor")            # Um inversor tem várias métricas
