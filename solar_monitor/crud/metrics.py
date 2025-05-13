from sqlalchemy.orm import Session                                               # Importa a classe Session do SQLAlchemy
from models import Metric                                                        # Importa a classe Metric
from schemas import MetricCreate                                                 # Importa a classe MetricCreate

def create_metric(db: Session, metric: MetricCreate):                           # Função para criar um novo registro
    db_metric = Metric(
        datetime=metric.datetime,
        inversor_id=metric.inversor_id,
        potencia_ativa_watt=metric.potencia_ativa_watt,
        temperatura_celsius=metric.temperatura_celsius
    )
    db.add(db_metric)
    db.commit()
    db.refresh(db_metric)
    return db_metric

def get_metrics(db: Session, skip: int = 0, limit: int = 100):                  # Função para obter todos os registros
    return db.query(Metric).offset(skip).limit(limit).all()

def get_metrics_by_inversor(db: Session, inversor_id: int):                     # Função para obter registros por inversor
    return db.query(Metric).filter(Metric.inversor_id == inversor_id).all()
