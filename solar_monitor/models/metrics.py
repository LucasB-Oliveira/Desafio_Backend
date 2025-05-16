#Tabelas do Banco de Dados
from sqlalchemy import Column, Integer, Float, DateTime, ForeignKey       # Importa classes do SQLAlchemy para definir colunas e tipos de dados
from sqlalchemy.orm import relationship                                   # Importa a classe relationship
from models.base import Base                                              # Importa a base declarativa


#TABELA DE MÉTRICAS
class Metric(Base):                 
    __tablename__ = 'metrics'        

    id = Column(Integer, primary_key=True, index=True)                       # Coluna ID (chave primária), índice para consulta rápida
    datetime = Column(DateTime, index=True)                                  # Data e hora da medição, também indexada para consulta rápida
    inversor_id = Column(Integer, index=True)                                # ID do inversor, indexado
    potencia_ativa_watt = Column(Float)                                      # Potência ativa em watts (float)
    temperatura_celsius = Column(Float)                                      # Temperatura em graus Celsius (float)

    inversor = relationship("Inversor", back_populates="metricas")           # Uma métrica pertence a um inversor
