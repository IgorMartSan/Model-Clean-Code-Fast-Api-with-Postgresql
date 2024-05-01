from db.database import Base
from sqlalchemy import Column, Integer, String, ForeignKey, Float, DateTime, func
import datetime

class Placa(Base):
    __tablename__ = "placa"
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    nome = Column("nome", String, nullable=False)
    comentario = Column("comentario", String, nullable=True)


class Medicao(Base):
    __tablename__ = "medicao"
    id = Column(Integer, primary_key=True, autoincrement=True)
    valor = Column(Float, nullable=False)
    posicao_x= Column(Float, nullable=True)
    posicao_y= Column(Float, nullable=True)
    data = Column(DateTime, server_default=func.now(), nullable=False)
    placa_id = Column(Integer, ForeignKey("placa.id"), nullable=False)



