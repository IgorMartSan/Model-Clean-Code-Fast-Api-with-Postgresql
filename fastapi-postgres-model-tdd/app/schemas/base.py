from pydantic import BaseModel

class CustomBaseModel(BaseModel):
    def dict(*args, **kwargs):
     d = super().model_dump(*args,**kwargs)