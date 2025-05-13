from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from crud import get_metrics, get_metrics_by_inversor
from schemas import MetricOut

router = APIRouter()

@router.get("/", response_model=list[MetricOut])
def read_metrics(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return get_metrics(db, skip, limit)

@router.get("/inversor/{inversor_id}", response_model=list[MetricOut])
def read_by_inversor(inversor_id: int, db: Session = Depends(get_db)):
    return get_metrics_by_inversor(db, inversor_id)
