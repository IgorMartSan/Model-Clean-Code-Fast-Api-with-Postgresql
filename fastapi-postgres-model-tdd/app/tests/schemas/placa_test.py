import pytest
from schemas.placa import Placa  # Substitua 'my_module' pelo nome do módulo onde está definida a classe Placa

def test_valid_placa():
    placa_data = {"name": "abc-def", "comentario": "Este é um comentário válido"}
    placa = Placa(**placa_data)
    assert placa.model_dump() == {"name": "abc-def", "comentario": "Este é um comentário válido"}

def test_invalid_placa():
    with pytest.raises(ValueError):
        placa_data = {
            'name': 123,
            'comentario': 'Seu comentário aqui'
        }
        placa = Placa(**placa_data)

def test_invalid_comentario_com_none():
    with pytest.raises(ValueError):
        Placa(name="abc-def",comentari=None)



