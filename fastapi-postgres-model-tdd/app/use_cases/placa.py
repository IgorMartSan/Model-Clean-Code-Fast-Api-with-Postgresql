from sqlalchemy.orm import Session
from db.model import Placa as PlacaModel
from schemas.placa import PlacaSchema, PlacaSchemaUpdate



class PlacaUseCases:
    @staticmethod
    def add_placa(placa: PlacaSchema, db_session: Session):
        placa_model = PlacaModel(**placa.model_dump())
        db_session.add(placa_model)
        db_session.commit()

    @staticmethod
    def remove_by_id(id: int, db_session: Session):
        placa = db_session.query(PlacaModel).filter(PlacaModel.id == id).first()
        if placa:
            db_session.delete(placa)
            db_session.commit()
            return True
        return False

    @staticmethod
    def update_placa(id: int, placa_data: PlacaSchemaUpdate, db_session: Session):
        placa = db_session.query(PlacaModel).filter(PlacaModel.id == id).first()
        if placa:
            for key, value in placa_data.model_dump().items():
                if value is not None:  # Verifica se o valor não é None
                    setattr(placa, key, value)
            db_session.commit()
            return True
        return False

    @staticmethod
    def list_placa(db_session: Session):
        return db_session.query(PlacaModel).all()

    @staticmethod
    def get_one_placa(id: int, db_session: Session):
        return db_session.query(PlacaModel).filter(PlacaModel.id == id).first()
