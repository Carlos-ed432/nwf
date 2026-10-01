# 📚 Gerenciador de Livros — Python + JSON

Projeto desenvolvido como **exercício de estudo em Python**, com o objetivo de praticar manipulação de arquivos JSON, estruturas de dados, funções, validação de entradas e organização de um pequeno sistema no terminal.

A interface também utiliza a biblioteca **Rich** para melhorar a apresentação das informações no console.

## 🎯 Objetivo

Praticar, através de um projeto pequeno, conceitos que venho estudando em Python e aplicar esses conceitos em um programa com persistência de dados.

O projeto simula um pequeno gerenciador de livros clássicos, permitindo cadastrar, pesquisar, remover e visualizar livros armazenados em um arquivo JSON.

## ⚙️ Funcionalidades

- 📖 Visualizar livros cadastrados
- ➕ Adicionar novos livros
- 🔎 Pesquisar livros
- 🗑️ Remover livros
- 🚫 Impedir o cadastro de livros duplicados
- 💾 Salvar alterações no arquivo JSON
- 🛡️ Tratar entradas inválidas no menu
- 🎨 Utilizar `Rich` para melhorar a interface do terminal

## 🗂️ Estrutura dos dados

Os dados são armazenados em um arquivo `livros.json`.

Exemplo:

```json
{
    "Livros Clássicos": [
        {
            "Livro": "A morte de Ivan Ilitch",
            "Lançamento": "1886",
            "Gênero": "Novela"
        },
        {
            "Livro": "A metamorfose",
            "Lançamento": "1915",
            "Gênero": "Ficção absurda/existencialista"
        }
    ]
}
```

Essa estrutura também foi utilizada como exercício para praticar **listas e dicionários aninhados**.

## 🧠 Conceitos praticados

Durante o desenvolvimento, pratiquei:

- Variáveis e tipos de dados
- `if`, `else` e estruturas de decisão
- `while`
- `for`
- `try/except`
- Funções
- `return`
- Listas
- Dicionários
- Métodos de listas, como `append()` e `remove()`
- Métodos de strings, como `strip()` e `casefold()`
- Leitura de arquivos
- Escrita de arquivos
- Manipulação de JSON
- `json.load()`
- `json.dump()`
- Validação de dados
- Tratamento de entradas inválidas
- Organização e reutilização de código
- Biblioteca `Rich`

## 🔄 Fluxo dos dados

O funcionamento básico do projeto segue este fluxo:

```text
livros.json
     ↓
json.load()
     ↓
Estrutura Python
     ↓
Adicionar / Pesquisar / Remover
     ↓
json.dump()
     ↓
livros.json atualizado
```

Também criei uma função para reutilizar a leitura do JSON:

```python
def loadjson(caminhodoarq):
    with open(caminhodoarq, 'r', encoding='utf8') as arquivo:
        return json.load(arquivo)
```

Isso evita repetir a mesma lógica sempre que preciso carregar os dados.

## 🔎 Validação de livros duplicados

Antes de adicionar um livro, o programa verifica se ele já existe.

Para tornar a comparação mais flexível, utilizo `strip()` e `casefold()`:

```python
if livro.strip().casefold() == liv["Livro"].strip().casefold():
    livroexist = True
```

Assim, diferenças de maiúsculas, minúsculas e espaços nas extremidades não causam cadastros duplicados.

## 🎨 Interface com Rich

O projeto utiliza a biblioteca `Rich` para melhorar a visualização das informações no terminal, utilizando elementos como:

- `Panel`
- Cores
- Formatação de texto
- Mensagens de sucesso e erro

Exemplo de estrutura do menu:

```text
┌──────────────────────────┐
│    Selecione uma opção   │
│                          │
│ 1 - Ver livros           │
│ 2 - Adicionar novo livro │
│ 3 - Pesquisar livro      │
│ 4 - Remover livro        │
│ 5 - Sair                 │
└──────────────────────────┘
```

## 🛠️ Tecnologias utilizadas

- **Python**
- **JSON**
- **Rich**
- **VS Code**

## 📌 Status do projeto

🚧 **Em desenvolvimento**

Este projeto faz parte dos meus estudos de Python e está sendo evoluído aos poucos conforme novos conceitos são aprendidos.

A ideia não é apenas adicionar funcionalidades, mas utilizar o projeto para praticar conceitos, testar possibilidades, encontrar erros e entender como cada parte do código funciona.

## 📚 Próximos passos

Algumas possibilidades para continuar evoluindo o projeto:

- Melhorar a organização do código
- Criar funções específicas para cada operação
- Melhorar o tratamento de erros
- Aprimorar a interface com Rich
- Adicionar edição de livros
- Melhorar a pesquisa
- Organizar o código em módulos
- Continuar praticando persistência de dados

---

### 👨‍💻 Projeto de estudo

Desenvolvido como parte dos meus estudos de **Python e Análise e Desenvolvimento de Sistemas**.

