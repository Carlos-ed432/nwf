# 📁 Organizador Automático de Arquivos (Python)

[![Python Version](https://shields.io)](https://python.org)
[![License: MIT](https://shields.io)](https://opensource.org)

Uma automação em Python desenvolvida para **dar fim à bagunça em pastas do sistema operacional** (como a pasta de *Downloads* ou *Imagens*). O script categoriza e move arquivos automaticamente para pastas específicas com base em suas extensões, tratando subdiretórios com segurança e rodando em um loop contínuo interativo.

Este projeto foi construído do zero com o objetivo de consolidar conceitos práticos de manipulação do Sistema Operacional (OS), tratamento de fluxos sequenciais e controle de loops de repetição.

---

## ✨ Funcionalidades Práticas

- **Filtro Multi-Extensão Inteligente:** Permite mapear e validar múltiplos formatos de arquivos ao mesmo tempo (ex: `.pdf`, `.deb`, `.webp`, etc.) utilizando buscas performáticas em listas.
- **Estrutura de Caminhos Dinâmica:** Cria e gerencia os diretórios de destino de forma automática sem sobrescrever arquivos existentes ou gerar exceções redundantes (`exist_ok=True`).
- **Blindagem Contra Subpastas:** O script possui um "olho clínico" que identifica subdiretórios no meio do caminho, ignorando-os (`continue`) para focar exclusivamente na manipulação de arquivos reais.
- **Interface de Repetição Interativa:** Utiliza uma estrutura de controle contínuo que permite ao usuário organizar múltiplas pastas em sequência sem precisar reiniciar o programa manualmente.

---

## 🛠️ Tecnologias e Conceitos Utilizados

O desenvolvimento deste script envolveu a aplicação direta de conceitos consolidados do ecossistema Python:

- **Biblioteca `os`:** Utilizada para mapeamento estrutural de diretórios (`os.listdir`), concatenação inteligente de caminhos de arquivos (`os.path.join`) e isolamento preciso de extensões (`os.path.splitext`).
- **Biblioteca `shutil`:** Aplicada na manipulação física dos arquivos do sistema de arquivos de origem para o destino.
- **Tratamento de Exceções (`try-except`):** Fluxos de segurança para garantir a execução do código mesmo diante de arquivos protegidos ou sem permissão de escrita.
- **Laços Finitos vs. Loops Infinitos:** Uso combinado de `for` (garantindo leituras estáticas e seguras da pasta) e `while True` (para a persistência interativa do menu com o usuário).

---

## 🚀 Como Executar o Projeto

### Pré-requisitos
Ter o **Python 3.10 ou superior** instalado na máquina.

### Execução
1. Clone este repositório para sua máquina local:
   ```bash
   git clone https://github.com
   ```
2. Abra o terminal na pasta do projeto e execute o script:
   ```bash
   python osandshutil.py
   ```
3. Digite o endereço do diretório que deseja limpar (ex: `/home/usuario/Downloads`), dê o nome da pasta de destino e assista à mágica acontecer!

---

## 🧠 Demonstração de Estrutura de Código

Abaixo está o trecho principal do laço que executa o filtro multi-verificação sequencial e move cada arquivo individualmente:

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
Desenvolvido com 💻 e muita persistência por **Carlos Eduardo**.
