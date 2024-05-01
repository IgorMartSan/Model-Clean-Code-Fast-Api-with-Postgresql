from pydantic import validator, BaseModel, Field
from typing import Optional
import re


class PlacaSchema(BaseModel):
    nome: str = Field(pattern=r"^([a-zA-Z]|-|_)+$")
    comentario: str

class PlacaSchemaUpdate(BaseModel):
    nome: Optional[str] = Field(None, pattern=r"^([a-zA-Z]|-|_)+$")
    comentario: Optional[str] = None
    # @validator('placa')
    # def validate_name(cls,value):
    #     if not re.match('^([a-z]|-|_)+$',value):
    #         raise ValueError('Invalid name')
    #     return value
