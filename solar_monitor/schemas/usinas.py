from pydantic import BaseModel              # Importa BaseModel do Pydantic para criar modelos com validação automática

class UsinaBase(BaseModel):                             
    nome: str


class UsinaCreate(UsinaBase):                           
    pass


class UsinaOut(UsinaBase):                              
    id: int
    class Config:
        from_attributes = True