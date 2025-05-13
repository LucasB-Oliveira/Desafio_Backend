from sqlalchemy.orm import Session                                  # Importa a classe Session do SQLAlchemy
from models import Inversor                                         # Importa a classe Inversor
from schemas import InversorCreate                                  # Importa a classe InversorCreate

def create_inversor(db: Session, inversor: InversorCreate):         # Função para criar um novo inversor
    db_inversor = Inversor(**inversor.dict())
    db.add(db_inversor)
    db.commit()
    db.refresh(db_inversor)
    return db_inversor

def get_inversores(db: Session):                                    # Função para obter todos os inversores
    return db.query(Inversor).all()

def delete_inversor(db: Session, inversor_id: int):                 # Função para deletar um inversor
    db.query(Inversor).filter(Inversor.id == inversor_id).delete()
    db.commit()
