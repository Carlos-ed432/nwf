# 🐍 Meus Estudos de Python

Iniciei meus estudos de Python há quase 2 meses e venho evoluindo através do curso de Python do **Gustavo Guanabara (Curso em Vídeo)**, exercícios práticos e pequenos projetos próprios.

Meu foco neste momento é construir uma base sólida de **lógica de programação**, entendendo o motivo de cada recurso antes de avançar para projetos maiores.

---

## 📚 O que já aprendi

| Conceitos Básicos & Estruturas | Funções, Módulos & Avançado |
| :--- | :--- |
| • Variáveis e tipos de dados<br>• `print()` e `input()`<br>• Conversão de tipos (`int`, `float`, `str`)<br>• Strings e fatiamento<br>• Listas e Estruturas de dados<br>• Algoritmos<br>• Introdução a JSON | • Funções, Parâmetros e Argumentos<br>• Retornos com `return`<br>• Docstrings<br>• Importação de bibliotecas (`random`, `time`)<br>• Criação de módulos próprios, Pacotes e Subpacotes<br>• Uso do `__init__.py`<br>• Organização de código em arquivos |
| **Controle de Fluxo & Erros** | **Versionamento** |
| • Condicionais: `if`, `elif`, `else`<br>• Operadores lógicos: `and`, `or`<br>• Laços de repetição: `while`, `for`<br>• Acumuladores e contadores<br>• Tratamento de erros: `try` e `except`<br>• Tratamento de `ValueError`<br>• Validação de entradas do usuário | • Git e GitHub para versionamento de código |

---

## 🧠 Programas e Projetos

### 🔞 1. Algoritmo para Classificação de Idade
Programa criado para receber sete valores referentes a idades e identificar quantas pessoas são maiores de idade.

* **Objetivo:** Praticar lógica de programação com foco em `while`, `for`, listas, contadores, condições, validação de entrada e tratamento de erros.

O programa foi desenvolvido para evitar problemas causados por entradas inválidas, como espaços vazios ou letras no lugar de números. Foi um dos primeiros exercícios em que comecei a perceber como diferentes estruturas do Python podem trabalhar juntas para controlar o fluxo de um programa.

### 🎲 2. Jogo de Adivinhação
Jogo em que o computador sorteia um número de **1 a 10** e o usuário precisa tentar descobrir qual número foi escolhido. O programa continua perguntando até que o usuário acerte e também contabiliza o número de tentativas.

* **Objetivo:** Praticar `while`, `if/elif/else`, acumuladores, `input()`, conversão de tipos, tratamento de erros e a biblioteca `random`.

Utilizei uma variável para armazenar o número sorteado e depois comparar cada tentativa do usuário com o valor escolhido pela máquina.

### 👥 3. Sistema de Cadastro de Pessoas
Um pequeno sistema inspirado nos exercícios do Curso em Vídeo. O programa possui um menu principal que permite visualizar pessoas cadastradas, cadastrar uma nova pessoa e sair do sistema.

* **Objetivo:** Começar a transformar os conhecimentos de lógica em um programa com uma estrutura mais próxima de um sistema real.

Também pratiquei validação de dados e tratamento de erros durante o cadastro. Esse exercício me fez perceber a importância de organizar o código em funções, em vez de colocar toda a lógica diretamente no programa principal.

### 📦 4. Estudos de Módulos e Pacotes
Durante o estudo de módulos, comecei a separar funções em arquivos diferentes e depois importá-las em outros programas.

Também pratiquei a criação de uma estrutura de pacotes com subpastas:

```text
pacotesmy/
├── __init__.py
├── dados/
│   └── __init__.py
├── números/
│   └── __init__.py
├── string/
│   └── __init__.py
└── validação/
    └── __init__.py
```
