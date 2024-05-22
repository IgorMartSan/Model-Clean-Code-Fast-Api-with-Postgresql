from fastapi import APIRouter, Depends, HTTPException, File
from fastapi.responses import FileResponse, StreamingResponse
from sqlalchemy.orm import Session
from schemas.medicao import MedicaoSchema, MedicaoUpdateSchema
from use_cases.medicao import MedicaoUseCases
import time
from PIL import Image
import io

router = APIRouter(prefix="/image")

@router.get("/original")
async def get_original_image():
    return FileResponse("fastapi-postgres-model-tdd\\app\\img\\TESTE.jpg")


@router.get("/resized")
async def get_resized_image():
    try:
        # Abrindo a imagem original
        with open("fastapi-postgres-model-tdd\\app\\img\\TESTE.jpg", "rb") as f:
            image = Image.open(io.BytesIO(f.read()))
            # Redimensionando a imagem
            resized_image = image.resize((100, 100))
            # Salvando a imagem redimensionada em um buffer de bytes
            output = io.BytesIO()
            resized_image.save(output, format="JPEG")
            output.seek(0)  # Movendo o cursor para o início do buffer
            # Retornando a imagem redimensionada usando FileResponse
            return FileResponse(output, media_type="image/jpeg")
    except Exception as e:
        return f"Erro ao processar a imagem: {e}"


@router.get("/original1")
async def get_original_image1():
    try:
        with open("fastapi-postgres-model-tdd\\app\\img\\TESTE.jpg", "rb") as f:
            image = Image.open(io.BytesIO(f.read()))
            output = io.BytesIO()
            image.save(output, format="JPEG")
            output.seek(0)
            return StreamingResponse(output, media_type="image/jpeg")
    except Exception as e:
        return f"Erro ao processar a imagem original: {e}"

         

@router.get("/resized1")
async def get_resized_image():
    try:
        with open("fastapi-postgres-model-tdd\\app\\img\\TESTE.jpg", "rb") as f:
            image = Image.open(io.BytesIO(f.read()))
            resized_image = image.resize((100, 100))
            output = io.BytesIO()
            resized_image.save(output, format="JPEG")
            output.seek(0)  # Move o cursor para o início do buffer
            return StreamingResponse(output, media_type="image/jpeg")
    except Exception as e:
        return f"Erro ao processar a imagem: {e}"
