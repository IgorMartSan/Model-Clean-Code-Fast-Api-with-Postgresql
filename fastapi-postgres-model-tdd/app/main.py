from fastapi import FastAPI, Depends, HTTPException, status, Response, Request
from sqlalchemy.orm import Session
import uvicorn
import pytest
import time
from db.database import engine, Base, get_db
import db.model
from  routes.placa import router as routerPlaca
from  routes.medicao import router as routerMedicao
from  routes.image import router as routerImage
from colorama import Fore, Style


# Executando testes unitarios, lembrando que o pytest procura todos os arquivos iniciados ou finalizado com "test_" ou "_test" respectivamente
# pytest.main(['app/tests', "--capture=sys", "-W", "ignore:Module already imported:pytest.PytestWarning"])

get_db()

Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.middleware("http")
async def log_request(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    end_time = time.time()
    execution_time = end_time - start_time
    log_message = f"Tempo de execução para {request.method} {request.url.path}: {execution_time} segundos"
    print(f"{Fore.BLUE}INFO: {log_message}{Style.RESET_ALL}")
    return response



if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8010, reload=True)

app.include_router(router=routerPlaca)
app.include_router(router=routerMedicao)
app.include_router(router=routerImage)
