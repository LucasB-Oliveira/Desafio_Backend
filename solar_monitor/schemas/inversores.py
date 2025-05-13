from pydantic import BaseModel              # Importa BaseModel do Pydantic para criar modelos com validação automática

class InversorBase(BaseModel):
    usina_id: int
    nome: str


class InversorCreate(InversorBase):
    pass


class InversorOut(InversorBase):
    id: int
    class Config:
        from_attributes = True