"""Exercício 4 - Verificando números pares e ímpares."""
from resolucoes.utils import ler_inteiro


def eh_par(numero: int) -> bool:
    """Um inteiro é par quando o resto da divisão por 2 é zero."""
    return numero % 2 == 0


def classificar_paridade(numero: int) -> str:
    return "par" if eh_par(numero) else "ímpar"


def main() -> None:
    numero = ler_inteiro("Digite um número inteiro: ")
    print(f"O número {numero} é {classificar_paridade(numero)}.")


if __name__ == "__main__":
    main()
