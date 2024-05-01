from fastapi import FastAPI, Depends, HTTPException, status, Response
from sqlalchemy.orm import Session
import uvicorn
import pytest
from db.database import engine, Base, get_db
import db.model
from  routes.placa import router as routerPlaca
from  routes.medicao import router as routerMedicao


# Executando testes unitarios, lembrando que o pytest procura todos os arquivos iniciados ou finalizado com "test_" ou "_test" respectivamente
# pytest.main(['app/tests', "--capture=sys", "-W", "ignore:Module already imported:pytest.PytestWarning"])

get_db()

Base.metadata.create_all(bind=engine)

app = FastAPI()

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8010, reload=True)

app.include_router(router=routerPlaca)
app.include_router(router=routerMedicao)
