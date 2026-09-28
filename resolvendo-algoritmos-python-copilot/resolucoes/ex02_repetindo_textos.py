"""Exercício 2 - Repetindo textos.

Recebe uma string e um inteiro e devolve a string repetida essa quantidade de vezes.
"""
from resolucoes.utils import ler_inteiro


def repetir_texto(texto: str, vezes: int, separador: str = "") -> str:
    """Repete `texto` `vezes` vezes, unido por `separador`."""
    if vezes < 0:
        raise ValueError("O número de repetições não pode ser negativo.")
    return separador.join([texto] * vezes)


def main() -> None:
    texto = input("Digite um texto: ")
    vezes = ler_inteiro("Quantas vezes repetir? ")
    try:
        print(repetir_texto(texto, vezes))
    except ValueError as erro:
        print(erro)


if __name__ == "__main__":
    main()
