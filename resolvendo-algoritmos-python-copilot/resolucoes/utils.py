"""Funções de entrada reutilizadas pelos exercícios."""


def ler_inteiro(mensagem: str) -> int:
    """Lê um número inteiro, repetindo a pergunta até a entrada ser válida."""
    while True:
        try:
            return int(input(mensagem).strip())
        except ValueError:
            print("Valor inválido. Digite um número inteiro.")


def ler_numero(mensagem: str) -> float:
    """Lê um número real (aceita vírgula como separador decimal)."""
    while True:
        try:
            return float(input(mensagem).strip().replace(",", "."))
        except ValueError:
            print("Valor inválido. Digite um número.")


def formatar_numero(valor: float) -> str:
    """Remove o '.0' de números inteiros: 8.0 -> '8', 2.5 -> '2.5'."""
    return f"{valor:g}" if abs(valor) < 1e15 else str(valor)
