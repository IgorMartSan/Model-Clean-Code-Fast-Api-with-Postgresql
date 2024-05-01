from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas.medicao import MedicaoSchema, MedicaoUpdateSchema
from use_cases.medicao import MedicaoUseCases
from db.database import get_db

router = APIRouter(prefix="/medicao", tags=["Medicao"])

@router.post("/add")
def add_medicao(medicao: MedicaoSchema, db_session: Session = Depends(get_db)):
    try:
        MedicaoUseCases.add_medicao(medicao=medicao, db_session=db_session)
        return {"message": "Medição adicionada com sucesso"}
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Erro ao adicionar medição: {str(e)}"
        )

@router.delete("/remove/{medicao_id}")
def remove_medicao(medicao_id: int, db_session: Session = Depends(get_db)):
    try:
        success = MedicaoUseCases.remove_medicao_by_id(id=medicao_id, db_session=db_session)
        if success:
            return {"message": "Medição removida com sucesso"}
        else:
            raise HTTPException(status_code=404, detail="Medição não encontrada")
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Erro ao remover medição: {str(e)}"
        )

@router.put("/update/{medicao_id}")
def update_medicao(
    medicao_id: int, medicao_data: MedicaoUpdateSchema, db_session: Session = Depends(get_db)
):
    try:
        success = MedicaoUseCases.update_medicao_by_id(
            id=medicao_id, medicao_data=medicao_data, db_session=db_session
        )
        if success:
            return {"message": "Medição atualizada com sucesso"}
        else:
            raise HTTPException(status_code=404, detail="Medição não encontrada")
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Erro ao atualizar medição: {str(e)}"
        )

@router.get("/list")
def list_medicoes(db_session: Session = Depends(get_db)):
    try:
        medicoes = MedicaoUseCases.list_medicoes(db_session=db_session)
        return {"medicoes": medicoes}
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Erro ao listar medições: {str(e)}"
        )

@router.get("/get/{medicao_id}")
def get_one_medicao(medicao_id: int, db_session: Session = Depends(get_db)):
    try:
        medicao = MedicaoUseCases.get_medicao_by_id(id=medicao_id, db_session=db_session)
        if medicao:
            return medicao
        else:
            raise HTTPException(status_code=404, detail="Medição não encontrada")
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Erro ao obter medição: {str(e)}"
        )
