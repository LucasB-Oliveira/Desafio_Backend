from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func
from database import get_db
from models import Metric, Inversor
from utils import TimeSeriesValue, calc_inverters_generation


router = APIRouter()

@router.get("/potencia_maxima/")
def potencia_maxima(inversor_id: int, data_inicio: str, data_fim: str, db: Session = Depends(get_db)):
    result = db.query(func.max(Metric.potencia_ativa_watt)) \
        .filter(Metric.inversor_id == inversor_id) \
        .filter(Metric.datetime.between(data_inicio, data_fim)) \
        .scalar()
    return {"potencia_maxima": result}

@router.get("/media_temperatura/")
def media_temperatura(inversor_id: int, data_inicio: str, data_fim: str, db: Session = Depends(get_db)):
    result = db.query(func.avg(Metric.temperatura_celsius)) \
        .filter(Metric.inversor_id == inversor_id) \
        .filter(Metric.datetime.between(data_inicio, data_fim)) \
        .scalar()
    return {"media_temperatura": result}

@router.get("/geracao_usina/")
def geracao_usina(usina_id: int, data_inicio: str, data_fim: str, db: Session = Depends(get_db)):
    inversores = db.query(Inversor.id).filter(Inversor.usina_id == usina_id).subquery().select()
    total = db.query(func.sum(Metric.potencia_ativa_watt)) \
        .filter(Metric.inversor_id.in_(inversores)) \
        .filter(Metric.datetime.between(data_inicio, data_fim)) \
        .scalar()
    return {"geracao_total": total}

@router.get("/geracao_inversor/")
def geracao_inversor(inversor_id: int, data_inicio: str, data_fim: str, db: Session = Depends(get_db)):
    total = db.query(func.sum(Metric.potencia_ativa_watt)) \
        .filter(Metric.inversor_id == inversor_id) \
        .filter(Metric.datetime.between(data_inicio, data_fim)) \
        .scalar()
    return {"geracao_total": total}


@router.get("/geracao_inversor_integrado/")
def geracao_inversor_integrado(inversor_id: int, data_inicio: str, data_fim: str, db: Session = Depends(get_db)):
    
    registros = db.query(Metric) \
        .filter(Metric.inversor_id == inversor_id) \
        .filter(Metric.datetime.between(data_inicio, data_fim)) \
        .order_by(Metric.datetime.asc()) \
        .all()

 
    power_data = [
        TimeSeriesValue(value=r.potencia_ativa_watt, date=r.datetime)
        for r in registros if r.potencia_ativa_watt is not None
    ]

   
    entity = type("InversorSimulado", (), {"power": power_data})()

    
    total_gerado = calc_inverters_generation([entity])

    return {"geracao_kwh_trapezio": total_gerado}

