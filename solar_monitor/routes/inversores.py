from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from crud import create_inversor, get_inversores, delete_inversor
from schemas import InversorCreate, InversorOut

router = APIRouter()

@router.post("/", response_model=InversorOut)
def create_inversor_endpoint(inversor: InversorCreate, db: Session = Depends(get_db)):
    return create_inversor(db, inversor)

@router.get("/", response_model=list[InversorOut])
def get_inversores_endpoint(db: Session = Depends(get_db)):
    return get_inversores(db)

@router.delete("/{inversor_id}")
def delete_inversor_endpoint(inversor_id: int, db: Session = Depends(get_db)):
    delete_inversor(db, inversor_id)
    return {"message": "Inversor deletado"}
