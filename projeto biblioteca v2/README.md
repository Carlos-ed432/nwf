# 📚 Sistema de Gerenciamento de Biblioteca CLI (v2)

Um sistema em linha de comando (CLI) moderno e visualmente elegante para gerenciamento de bibliotecas, desenvolvido em **Python** e potencializado pela biblioteca **Rich**. O projeto realiza o CRUD completo de livros, controle rigoroso de empréstimos/devoluções e persistência de dados utilizando arquivos estruturados em **JSON**.

---

## ✨ Funcionalidades Principais

O sistema oferece uma interface robusta baseada em terminal dividida em módulos essenciais:

*   **Gestão de Acervo (CRUD):** Cadastro completo com validações, pesquisa avançada por nome (case-insensitive) e remoção segura de títulos com confirmação do usuário.
*   **Controle de Empréstimos:** Sistema automatizado de prazos de validade com cálculo dinâmico utilizando a biblioteca nativa `datetime` (prazo padrão de 30 dias).
*   **Layouts Avançados (Rich Tables & Panels):** Exibição de relatórios e acervos organizados em formato tabular, com cores intuitivas para sinalizar disponibilidade (Verde) ou empréstimo ativo (Vermelho).
*   **Persistência de Dados Inteligente:** Salvamento automático e tratamento de exceções de arquivos (`JSONDecodeError` e manipulação segura de dicionários aninhados através de `.get()`).

---

## 🛠️ Tecnologias e Bibliotecas Utilizadas

*   **Python 3.10+** (Núcleo do sistema)
*   **JSON** (Persistência e modelagem do banco de dados relacional simulado)
*   **Datetime & Timedelta** (Gerenciamento cronológico de prazos e validades)
*   **Rich (Console, Table, Panel, Traceback)** (Renderização visual avançada e tratamento elegante de erros no terminal)

---

## 📂 Estrutura de Dados do Banco (JSON)

Os dados são armazenados na seguinte estrutura hierárquica dentro do arquivo `.json`:

```json
{
  "Livros": [
    {
      "Livro": "O Hobbit",
      "Lancamento": "1937",
      "Autor": "J.R.R. Tolkien",
      "Disponivel": false,
      "Emprestimo": {
        "Leitor": "Carlos",
        "Data": "2026-10-16",
        "Validade": "2026-11-15"
      }
    }
  ]
}
```

---

## 🚀 Como Executar o Projeto

### Pré-requisitos
Certifique-se de ter o Python instalado na sua máquina e a biblioteca `rich`.

```bash
pip install rich
```


---

## 🧠 Destaques de Código e Aprendizados

### 1. Manipulação Avançada de Tabelas Terminais
Ao migrar layouts repetitivos de loops para objetos consolidados de `Table`, a legibilidade do sistema aumentou drasticamente, reduzindo o consumo de espaço no terminal e facilitando a varredura visual de dados.

### 2. Defesa contra Quebras de Fluxo (`KeyError`)
Implementação de buscas seguras usando dicionários do Python:
```python
# Impede a interrupção abrupta do código caso a estrutura do JSON mude ou esteja nula
emprestimo = livro.get("Emprestimo", {})
leitor = emprestimo.get("Leitor", "Não informado") if emprestimo else "Não informado"
```

---



---
Desenvolvido com 💻 e ☕ por **Carlos Eduardo**. Conecte-se comigo no [LinkedIn](www.linkedin.com/in/carlos-eduardo-9712683a3).
