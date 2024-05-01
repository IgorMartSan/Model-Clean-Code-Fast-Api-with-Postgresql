from sqlalchemy.orm import Session
from db.model import Medicao as MedicaoModel
from schemas.medicao import MedicaoSchema, MedicaoUpdateSchema

class MedicaoUseCases:
    @staticmethod
    def add_medicao(medicao: MedicaoSchema, db_session: Session):
        medicao_model = MedicaoModel(**medicao.model_dump())
        db_session.add(medicao_model)
        db_session.commit()

    @staticmethod
    def remove_medicao_by_id(id: int, db_session: Session):
        medicao = db_session.query(MedicaoModel).filter(MedicaoModel.id == id).first()
        if medicao:
            db_session.delete(medicao)
            db_session.commit()
            return True
        return False

    @staticmethod
    def update_medicao_by_id(id: int, medicao_data: MedicaoUpdateSchema, db_session: Session):
        medicao = db_session.query(MedicaoModel).filter(MedicaoModel.id == id).first()
        if medicao:
            for key, value in medicao_data.dict().items():
                if value is not None:  # Verifica se o valor não é None
                    setattr(medicao, key, value)
            db_session.commit()
            return True
        return False

    @staticmethod
    def list_medicoes(db_session: Session):
        return db_session.query(MedicaoModel).all()

    @staticmethod
    def get_medicao_by_id(id: int, db_session: Session):
        return db_session.query(MedicaoModel).filter(MedicaoModel.id == id).first()
