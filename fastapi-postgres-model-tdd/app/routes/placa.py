from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas.placa import PlacaSchema, PlacaSchemaUpdate
from use_cases.placa import PlacaUseCases
from db.database import get_db

router = APIRouter(prefix="/placa", tags=["Placa"])


@router.post("/add")
def add_placa(placa: PlacaSchema, db_session: Session = Depends(get_db)):
    try:
        PlacaUseCases.add_placa(placa=placa, db_session=db_session)
        return {"message": "Placa adicionada com sucesso"}
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Erro ao adicionar placa: {str(e)}"
        )


@router.delete("/remove/{placa_id}")
def remove_placa(placa_id: int, db_session: Session = Depends(get_db)):
    try:
        success = PlacaUseCases.remove_by_id(id=placa_id, db_session=db_session)
        if success:
            return {"message": "Placa removida com sucesso"}
        else:
            raise HTTPException(status_code=404, detail="Placa não encontrada")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao remover placa: {str(e)}")


@router.put("/update/{placa_id}")
def update_placa(
    placa_id: int, placa_data: PlacaSchemaUpdate, db_session: Session = Depends(get_db)
):
    try:
        success = PlacaUseCases.update_placa(
            id=placa_id, placa_data=placa_data, db_session=db_session
        )
        if success:
            return {"message": "Placa atualizada com sucesso"}
        else:
            raise HTTPException(status_code=404, detail="Placa não encontrada")
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Erro ao atualizar placa: {str(e)}"
        )


@router.get("/list")
def list_placas(db_session: Session = Depends(get_db)):
    try:
        placas = PlacaUseCases.list_placa(db_session=db_session)
        return {"placas": placas}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao listar placas: {str(e)}")


@router.get("/get/{placa_id}")
def get_one_placa(placa_id: int, db_session: Session = Depends(get_db)):
    try:
        placa = PlacaUseCases.get_one_placa(id=placa_id, db_session=db_session)
        if placa:
            return placa
        else:
            raise HTTPException(status_code=404, detail="Placa não encontrada")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao obter placa: {str(e)}")
    

@router.get("/get/{placa_id}")
def list(placa_id: int, db_session: Session = Depends(get_db)):
    try:
        placa = PlacaUseCases.get_one_placa(id=placa_id, db_session=db_session)
        if placa:
            return placa
        else:
            raise HTTPException(status_code=404, detail="Placa não encontrada")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao obter placa: {str(e)}")
