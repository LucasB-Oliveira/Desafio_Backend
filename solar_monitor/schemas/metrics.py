from pydantic import BaseModel              # Importa BaseModel do Pydantic para criar modelos com validação automática
from datetime import datetime               # Importa datetime do Python para lidar com datas e horas
from typing import Optional                 # Importa Optional do Python para lidar com valores opcionais

# Metricas
class MetricBase(BaseModel):
    datetime: datetime                                  # Data e hora da medição
    inversor_id: int                                    # ID do inversor
    potencia_ativa_watt: Optional [float]               # Potência ativa medida em watts
    temperatura_celsius: Optional [float]               # Temperatura medida em graus Celsius

class MetricCreate(MetricBase):                         # Modelo para criação de registros (usa os mesmos campos do MetricBase)
        pass                                            # Apenas herda os campos, não precisa adicionar nada

class MetricOut(MetricBase):                            # Modelo para resposta da API, incluindo o ID gerado pelo banco
        id: int                                         # ID único do registro no banco

        class Config:
            from_attributes = True                      #Permite que FastAPI converta modelos SQLAlchemy automaticamente em JSON