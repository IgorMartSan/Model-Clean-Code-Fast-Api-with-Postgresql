from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class MedicaoSchema(BaseModel):
    valor: float
    posicao_x: Optional[float] = None
    posicao_y: Optional[float] = None
    data: Optional[datetime] = None
    placa_id: int

    class Config:
        orm_mode = True

class MedicaoUpdateSchema(BaseModel):
    valor: Optional[float] = None
    posicao_x: Optional[float] = None
    posicao_y: Optional[float] = None
    data: Optional[datetime] = None
    placa_id: int

    class Config:
        orm_mode = True