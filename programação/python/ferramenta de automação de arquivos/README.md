# 📁 Organizador Automático de Arquivos (Python)

Uma automação desenvolvida para organizar pastas do sistema operacional, como **Downloads** e **Imagens**. O script categoriza e move arquivos automaticamente para diretórios específicos de acordo com suas extensões, ignorando subpastas e funcionando em um menu interativo contínuo.

> 🧠 **Propósito do projeto:** consolidar conceitos práticos de manipulação do sistema operacional, processamento sequencial de arquivos e controle de estruturas de repetição.

---

## ✨ Funcionalidades

| Recurso | Descrição |
| :--- | :--- |
| **Filtro inteligente** | Mapeia e valida múltiplos formatos de arquivo por extensão. |
| **Caminhos dinâmicos** | Cria e gerencia os diretórios de destino automaticamente, sem sobrescrever arquivos nem gerar exceções desnecessárias (`exist_ok=True`). |
| **Proteção contra subpastas** | Identifica e ignora diretórios durante a varredura para manipular somente arquivos. |
| **Menu interativo** | Permite organizar várias pastas em sequência sem reiniciar o programa. |

---

## 🛠️ Tecnologias e conceitos utilizados

- **Biblioteca `os`:** usada para listar diretórios (`os.listdir`), montar caminhos (`os.path.join`) e identificar extensões (`os.path.splitext`).
- **Biblioteca `shutil`:** responsável por mover os arquivos com segurança entre a origem e o destino.
- **Tratamento de exceções (`try`/`except`):** mantém o programa em execução mesmo diante de arquivos protegidos ou sem permissão de escrita.
- **Controle de fluxo:** combina `for` para varrer arquivos e `while True` para manter o menu interativo ativo.

---

## 🚀 Como executar

### Pré-requisitos

- Python 3.10 ou superior.
- Linux, Windows ou macOS.

### Passo a passo

1. Clone o repositório:

   ```bash
   git clone <URL_DO_SEU_REPOSITORIO>
   ```

2. Entre na pasta do projeto:

   ```bash
   cd nwf
   ```

3. Execute o script principal:

   ```bash
   python osandshutil.py
   ```

4. Informe o caminho da pasta que deseja organizar — por exemplo, `/home/usuario/Downloads` — e o nome da pasta de destino.

---

## 🧠 Trecho central do código

```python
for item in arquivos:
    caminhoarq = os.path.join(diretório, item)

    # Ignora subpastas e processa somente arquivos.
    if os.path.isdir(caminhoarq):
        continue

    nomeaext, extensao = os.path.splitext(item)
    if extensao.lower() in ['.pdf', '.deb', '.webp', '.jpg', '.png']:
        shutil.move(caminhoarq, destino)
        contador += 1
```

---

## 📝 Próximos passos

- [x] Normalizar extensões com `.lower()` para que arquivos como `.PDF` também sejam reconhecidos.
- [ ] Adicionar monitoramento em segundo plano para executar a organização automaticamente a cada intervalo definido.
- [ ] Criar logs coloridos no terminal com relatórios após cada limpeza.

---

Desenvolvido com 💻 e muita persistência por **Carlos Eduardo**.
