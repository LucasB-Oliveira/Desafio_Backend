from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from crud import create_usina, get_usinas, delete_usina
from schemas import UsinaCreate, UsinaOut

router = APIRouter()

@router.post("/", response_model=UsinaOut)
def create_usina_endpoint(usina: UsinaCreate, db: Session = Depends(get_db)):
    return create_usina(db, usina)

@router.get("/", response_model=list[UsinaOut])
def get_usinas_endpoint(db: Session = Depends(get_db)):
    return get_usinas(db)

@router.delete("/{usina_id}")
def delete_usina_endpoint(usina_id: int, db: Session = Depends(get_db)):
    delete_usina(db, usina_id)
    return {"message": "Usina deletada"}
