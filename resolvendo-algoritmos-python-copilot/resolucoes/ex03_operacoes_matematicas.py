"""Exercício 3 - Operações matemáticas simples.

Recebe dois números e uma operação (+, -, *, /) e mostra o resultado.
"""
import operator

from resolucoes.utils import formatar_numero, ler_numero

OPERACOES = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv,
}


def calcular(a: float, b: float, operacao: str) -> float:
    """Executa a operação escolhida entre `a` e `b`."""
    if operacao not in OPERACOES:
        raise ValueError(f"Operação inválida: {operacao!r}. Use + - * ou /.")
    if operacao == "/" and b == 0:
        raise ZeroDivisionError("Não é possível dividir por zero.")
    return OPERACOES[operacao](a, b)


def main() -> None:
    a = ler_numero("Primeiro número: ")
    b = ler_numero("Segundo número: ")
    operacao = input("Operação (+, -, *, /): ").strip()
    try:
        resultado = calcular(a, b, operacao)
        print(f"{formatar_numero(a)} {operacao} {formatar_numero(b)} = {formatar_numero(resultado)}")
    except (ValueError, ZeroDivisionError) as erro:
        print(erro)


if __name__ == "__main__":
    main()
