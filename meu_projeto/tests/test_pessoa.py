import pytest
from meu_projeto.models.pessoa import Pessoa
from meu_projeto.models.enums.sexo import Sexo

@pytest.fixture
def pessoa_valida():
    pessoa = Pessoa("LPL", 21, Sexo.MASCULINO)
    return pessoa


def test_pessoa_mudar_nome_valido(pessoa_valida):
    pessoa_valida._nome = "Robson"
    assert pessoa_valida.nome == "Robson"

def test_pessoa_nome_valido(pessoa_valida):
    assert pessoa_valida._nome == "LPL"

def test_pessoa_idade_valida(pessoa_valida):
    assert pessoa_valida._idade == 21


def test_pessoa_idade_negativa(pessoa_valida):
    pessoa_valida.set_idade(-1)
    assert pessoa_valida._idade == 0

