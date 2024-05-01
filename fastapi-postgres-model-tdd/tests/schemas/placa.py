# from app.schemas.placa import Placa
import pytest
import os
# Obtendo o diretório raiz do arquivo atual
diretorio_relativo = os.path.relpath(os.path.dirname(__file__), os.getcwd())

print("Diretório relativo:", diretorio_relativo)


# def test_category_schema():
#     placa = Placa(
#         nome='XPTO',
#         comentario='Placa teste'
#     )

#     assert placa.dict() == {
#         'name':'XPTO',
#         'comentario': 'Placa teste'
#     }

# def test_category_schema_invalid_name():
    
#     with pytest.raises(ValueError):
#         placa = Placa(
#             nome=None,
#             comentario='Placa teste'
#         )

#     with pytest.raises(ValueError):
#         assert placa.model_dump == {
#             'name':'XPTO',
#             'comentario': 'Placa teste'
#         }