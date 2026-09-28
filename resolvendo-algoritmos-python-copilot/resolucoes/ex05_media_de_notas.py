"""Exercício 5 - Calculando a média de três notas."""
from resolucoes.utils import ler_numero


def calcular_media(*notas: float) -> float:
    """Média aritmética das notas informadas (soma / quantidade)."""
    if not notas:
        raise ValueError("Informe pelo menos uma nota.")
    for nota in notas:
        if not 0 <= nota <= 10:
            raise ValueError(f"Nota inválida: {nota}. Use valores entre 0 e 10.")
    return sum(notas) / len(notas)


def main() -> None:
    notas = [ler_numero(f"Digite a nota {i}: ") for i in range(1, 4)]
    try:
        print(f"Média: {calcular_media(*notas):.2f}")
    except ValueError as erro:
        print(erro)


if __name__ == "__main__":
    main()
