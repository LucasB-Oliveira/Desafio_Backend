from sqlalchemy.orm import Session                                           # Importa a classe Session do SQLAlchemy
from models import Usina                                                     # Importa a classe Usina
from schemas import UsinaCreate                                              # Importa a classe UsinaCreate

def create_usina(db: Session, usina: UsinaCreate):                           # Função para criar um novo registro
    db_usina = Usina(**usina.dict())
    db.add(db_usina)
    db.commit()
    db.refresh(db_usina)
    return db_usina

def get_usinas(db: Session):                                                # Função para obter todos os registros
    return db.query(Usina).all()

def delete_usina(db: Session, usina_id: int):                               # Função para deletar um registro
    db.query(Usina).filter(Usina.id == usina_id).delete()
    db.commit()
