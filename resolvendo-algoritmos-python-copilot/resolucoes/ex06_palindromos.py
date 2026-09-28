"""Exercício 6 - Verificando palíndromos."""
import unicodedata


def normalizar(texto: str) -> str:
    """Minúsculas, sem acentos, espaços e pontuação: 'Ovo!' -> 'ovo'."""
    sem_acentos = unicodedata.normalize("NFKD", texto).encode("ascii", "ignore").decode()
    return "".join(c for c in sem_acentos.lower() if c.isalnum())


def eh_palindromo(texto: str) -> bool:
    """Compara o texto normalizado com ele mesmo invertido ([::-1])."""
    limpo = normalizar(texto)
    return limpo == limpo[::-1]


def main() -> None:
    texto = input("Digite uma palavra ou frase: ")
    resultado = "é" if eh_palindromo(texto) else "não é"
    print(f'"{texto}" {resultado} um palíndromo.')


if __name__ == "__main__":
    main()
