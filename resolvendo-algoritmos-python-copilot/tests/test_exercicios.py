import pytest

from resolucoes.ex01_concatenando_dados import concatenar_dados
from resolucoes.ex02_repetindo_textos import repetir_texto
from resolucoes.ex03_operacoes_matematicas import calcular
from resolucoes.ex04_par_ou_impar import classificar_paridade, eh_par
from resolucoes.ex05_media_de_notas import calcular_media
from resolucoes.ex06_palindromos import eh_palindromo, normalizar
from resolucoes.utils import formatar_numero


def test_concatenar_dados():
    assert concatenar_dados("Ana", "tem", 30, "anos") == "Ana tem 30 anos"
    assert concatenar_dados("a", "b", separador="-") == "a-b"


def test_repetir_texto():
    assert repetir_texto("oi", 3) == "oioioi"
    assert repetir_texto("oi", 3, separador=" ") == "oi oi oi"
    assert repetir_texto("oi", 0) == ""
    with pytest.raises(ValueError):
        repetir_texto("oi", -1)


@pytest.mark.parametrize("a,b,op,esperado", [(6, 3, "+", 9), (6, 3, "-", 3), (6, 3, "*", 18), (6, 3, "/", 2)])
def test_calcular(a, b, op, esperado):
    assert calcular(a, b, op) == esperado


def test_calcular_erros():
    with pytest.raises(ZeroDivisionError):
        calcular(1, 0, "/")
    with pytest.raises(ValueError):
        calcular(1, 2, "%")


def test_formatar_numero():
    assert formatar_numero(8.0) == "8"
    assert formatar_numero(2.5) == "2.5"


@pytest.mark.parametrize("n,par", [(0, True), (2, True), (7, False), (-3, False), (-4, True)])
def test_paridade(n, par):
    assert eh_par(n) is par
    assert classificar_paridade(n) == ("par" if par else "ímpar")


def test_media():
    assert calcular_media(7, 8, 9) == 8
    assert calcular_media(10, 5, 0) == 5
    with pytest.raises(ValueError):
        calcular_media(11, 5, 5)
    with pytest.raises(ValueError):
        calcular_media()


@pytest.mark.parametrize("texto", ["ovo", "Arara", "Anotaram a data da maratona", "Socorram-me, subi no ônibus em Marrocos", "a"])
def test_palindromos_verdadeiros(texto):
    assert eh_palindromo(texto)


@pytest.mark.parametrize("texto", ["python", "copilot"])
def test_palindromos_falsos(texto):
    assert not eh_palindromo(texto)


def test_normalizar():
    assert normalizar("Ovo!") == "ovo"
