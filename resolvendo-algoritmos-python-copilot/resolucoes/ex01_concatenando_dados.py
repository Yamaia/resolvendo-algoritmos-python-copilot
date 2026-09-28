"""Exercício 1 - Concatenando dados.

Recebe dois dados de tipos diferentes (nome e idade) e os junta em uma única string.
"""
from resolucoes.utils import ler_inteiro


def concatenar_dados(*dados, separador: str = " ") -> str:
    """Converte cada dado para texto e junta todos com o separador."""
    return separador.join(str(dado) for dado in dados)


def main() -> None:
    nome = input("Digite seu nome: ").strip()
    idade = ler_inteiro("Digite sua idade: ")
    print(concatenar_dados(nome, "tem", idade, "anos"))


if __name__ == "__main__":
    main()
