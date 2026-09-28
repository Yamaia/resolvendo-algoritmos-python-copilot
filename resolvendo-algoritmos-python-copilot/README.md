# 🤖 Resolvendo Algoritmos em Python com o GitHub Copilot

![CI](https://github.com/SEU_USUARIO/resolvendo-algoritmos-python-copilot/actions/workflows/ci.yml/badge.svg)
![Python](https://img.shields.io/badge/python-3.10%2B-blue)

Seis algoritmos em Python resolvidos com apoio de IA, cada um com o **prompt usado**, a **solução**, as **decisões técnicas** e **testes automatizados**.

Projeto do desafio da [DIO](https://www.dio.me/), baseado em [alinealien/resolvendo-codigos-py-copilot](https://github.com/alinealien/resolvendo-codigos-py-copilot).

## Como a IA foi usada
1. Escrevo um comentário ou prompt descrevendo o problema (exemplos abaixo).
2. Reviso a sugestão da IA: o código faz o que foi pedido? Trata entradas inválidas?
3. Refatoro em funções puras (sem `input`/`print`), o que permite testá-las.
4. Cubro os casos normais e os de borda com `pytest`.

> A IA acelera o rascunho, mas revisar, entender e testar continua sendo responsabilidade de quem programa.

## Exercícios

| # | Exercício | Arquivo | Conceitos |
|---|---|---|---|
| 1 | Concatenando dados | [`ex01_concatenando_dados.py`](resolucoes/ex01_concatenando_dados.py) | strings, `input`, `join` |
| 2 | Repetindo textos | [`ex02_repetindo_textos.py`](resolucoes/ex02_repetindo_textos.py) | strings, `int`, repetição |
| 3 | Operações matemáticas | [`ex03_operacoes_matematicas.py`](resolucoes/ex03_operacoes_matematicas.py) | operadores, `operator`, dicionário |
| 4 | Par ou ímpar | [`ex04_par_ou_impar.py`](resolucoes/ex04_par_ou_impar.py) | condicionais, módulo `%` |
| 5 | Média de notas | [`ex05_media_de_notas.py`](resolucoes/ex05_media_de_notas.py) | variáveis, aritmética, validação |
| 6 | Palíndromos | [`ex06_palindromos.py`](resolucoes/ex06_palindromos.py) | slicing `[::-1]`, normalização |

### 1 - Concatenando dados
**Prompt:** `# função que recebe dados de tipos diferentes (nome e idade) e devolve uma única string`
**Decisão:** `str()` em cada item + `join`, o que evita o `TypeError` de somar `str` com `int`.

### 2 - Repetindo textos
**Prompt:** `# função que repete um texto N vezes, com separador opcional`
**Decisão:** `separador.join([texto] * vezes)` permite separar as repetições, e valores negativos levantam `ValueError`.

### 3 - Operações matemáticas simples
**Prompt:** `# calculadora com + - * / usando um dicionário de operações, tratando divisão por zero`
**Decisão:** dicionário de funções do módulo `operator`, sem cadeia de `if/elif`. Para adicionar uma operação basta uma linha nova.

### 4 - Par ou ímpar
**Prompt:** `# função que diz se um inteiro é par ou ímpar usando o operador módulo`
**Decisão:** `numero % 2 == 0`, que também funciona com negativos e zero.

### 5 - Média de notas
**Prompt:** `# função que calcula a média aritmética de notas entre 0 e 10, validando o intervalo`
**Decisão:** aceita `*notas` (qualquer quantidade) e valida cada nota.

### 6 - Palíndromos
**Prompt:** `# função que verifica palíndromo ignorando maiúsculas, acentos, espaços e pontuação`
**Decisão:** `unicodedata` (biblioteca padrão) normaliza o texto antes de comparar com `[::-1]`. Assim "Socorram-me, subi no ônibus em Marrocos" também é reconhecida.

## Como executar
```bash
git clone https://github.com/SEU_USUARIO/resolvendo-algoritmos-python-copilot.git
cd resolvendo-algoritmos-python-copilot

python -m resolucoes.ex01_concatenando_dados
python -m resolucoes.ex06_palindromos

pip install -r requirements-dev.txt
pytest -v
```
Requer Python 3.10+ e nenhuma biblioteca externa além do `pytest` para os testes.

## Estrutura
```
resolucoes/   um módulo por exercício + utils.py (leitura de entradas)
tests/        testes com pytest
```

## Licença
MIT
