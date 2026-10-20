# 📁 Organizador Automático de Arquivos (Python)

![Python Version](https://shields.io)
![License: MIT](https://shields.io)
![OS Compatibility](https://shields.io)

Uma automação robusta desenvolvida para **dar fim à bagunça em pastas do sistema operacional** (como as pastas de *Downloads* ou *Imagens*). O script categoriza e move arquivos automaticamente para pastas específicas com base em suas extensões, tratando subdiretórios com segurança e rodando em um loop contínuo interativo.

> 🧠 **Propósito do Projeto:** Este projeto foi construído do zero com o objetivo de consolidar conceitos práticos de manipulação do Sistema Operacional (OS), tratamento de fluxos sequenciais e controle de loops de repetição.

---

## ✨ Funcionalidades Práticas

| Recurso | Descrição |
| :--- | :--- |
| **Filtro Inteligente** | Permite mapear e validar múltiplos formatos de arquivos ao mesmo tempo utilizando buscas performáticas em listas. |
| **Caminhos Dinâmicos** | Cria e gerencia os diretórios de destino de forma automática sem sobrescrever arquivos existentes ou gerar exceções redundantes (`exist_ok=True`). |
| **Blindagem Contra Subpastas** | Identifica subdiretórios no meio do caminho, ignorando-os (`continue`) para focar exclusivamente na manipulação de arquivos reais. |
| **Menu Interativo** | Estrutura de controle contínuo que permite ao usuário organizar múltiplas pastas em sequência sem precisar reiniciar o programa manualmente. |

---

## 🛠️ Tecnologias e Conceitos Utilizados

O desenvolvimento deste script envolveu a aplicação direta de conceitos consolidados do ecossistema Python:

*   **Biblioteca `os`:** Utilizada para mapeamento estrutural de diretórios (`os.listdir`), concatenação inteligente de caminhos de arquivos (`os.path.join`) e isolamento preciso de extensões (`os.path.splitext`).
*   **Biblioteca `shutil`:** Aplicada na manipulação física e movimentação segura dos arquivos do sistema de origem para o destino.
*   **Tratamento de Exceções (`try-except`):** Criação de fluxos de segurança para garantir a execução contínua do código mesmo diante de arquivos protegidos ou sem permissão de escrita.
*   **Controle de Fluxo Complexo:** Uso combinado de laços finitos (`for` para varredura estática da pasta) e laços infinitos (`while True` para a persistência do menu interativo).

---

## 🚀 Como Executar o Projeto

### Pré-requisitos

*   **Ambiente:** Python 3.10 ou superior instalado na máquina.
*   **SO:** Compatível com ambientes Linux, Windows e macOS.

### Passo a Passo

1. **Clone este repositório para sua máquina local:**
   ```bash
   git clone https://github.com
   ```

2. **Navegue até o diretório do projeto:**
   ```bash
   cd nwf
   ```

3. **Execute o script principal:**
   ```bash
   python osandshutil.py
   ```

4. **Utilize a ferramenta:**
   Insira o endereço do diretório que deseja limpar (ex: `/home/usuario/Downloads`), informe o nome da pasta de destino e assista à organização acontecer em tempo real!

---

## 🧠 Demonstração da Estrutura de Código

Abaixo está o trecho central do laço que executa o filtro sequencial e manipula cada arquivo individualmente:

```python
for item in arquivos:
    caminhoarq = os.path.join(diretório, item)
    
    # Trava de segurança: ignora pastas para focar em arquivos de verdade
    if os.path.isdir(caminhoarq):
        continue
        
    nomeaext, extensao = os.path.splitext(item)
    if extensao.lower() in ['.pdf', '.deb', '.webp', '.jpg', '.png']:
        shutil.move(caminhoarq, destino)
        contador += 1
```

---

## 📝 Próximos Passos (Roadmap de Evolução)

- [ ] Implementar a conversão automática para minúsculas (`.lower()`) nas extensões para evitar que arquivos em caixa alta (ex: `.PDF`) escapem do filtro.
- [ ] Adicionar um monitoramento de eventos em segundo plano para rodar a organização de forma 100% automatizada a cada X segundos.
- [ ] Criar logs customizados no terminal utilizando códigos de cor ANSI estruturados para exibir relatórios dinâmicos pós-limpeza.

---

Desenvolvido com 💻 e muita persistência por **Carlos Eduardo**
