import json
from rich import print
from rich.console import Console
from rich.panel import Panel
from datetime import date,timedelta
from time import sleep
from rich.table import Table
from rich import inspect
from rich.traceback import install
install()
def criarjson(nomearq):
    try:
        with open(nomearq,'x',encoding='utf-8') as arqv:
            return arqv
    except FileExistsError:
        pass

def opcoes():
    print(Panel("0 - Listar livros\n1 - Adicionar livro\n2 - Pesquisar livro\n3 - Remover livro\n4 - Pegar livro emprestado\n5 - Devolver livro\n6 - Livros disponíveis\n7 - Livros emprestados\n8 - Estatísticas\n9 - Sair"
,width=30,border_style='green',title='[bold white]Selecione uma opção[/]'))

def loadjson(arqjson):
    """ Função de carregamento de json no modo read
        param - Utilize o arquivo que deseja carregar, desde que ele seja um caminho válido
        Deve-se ser usado apenas em jsons
    """
    try:
        with open(arqjson,'r',encoding='utf-8') as arquivo:
            return json.load(arquivo)
    except json.decoder.JSONDecodeError:
        print("[bold red]Arquivo vazio[/]")


def cadastrarlivro():
    try:
        livro = input("Nome do livro: ")
        Lancamento = input("Lancamento do livro: ")
        Autor = input("Autor do livro: ")
        #Criando a estrutura de dados do json 
        dadoslivrosjson = {"Livro":livro,"Lancamento":Lancamento,"Autor":Autor,"Disponivel":True,"Emprestimo":{"Leitor":None,"Data":None,"Validade":None}}
        arquivo = r"/home/carlos/programação/python/API/manipulandojson/projeta biblioteca v2/Bibliotecav2.json"
        try:
            with open(arquivo,'r',encoding='utf-8') as arqjson:
                lista_livros = json.load(arqjson)
        except json.decoder.JSONDecodeError:
            lista_livros = {"Livros":[]}
        lista_livros["Livros"].append(dadoslivrosjson)
        atualizarjson(lista_livros)
        print("[bold green]Livro adicionado com sucesso[/]!")
    except Exception as e:
        print(f"[bold red]Erro de {e},tente novamente.[/]")


from rich.console import Console
from rich.table import Table

console = Console()

def carregarlivros():
    try:
        livroload = loadjson(arquivo)
        
        # Cria uma tabela única para listar todo o acervo
        tabela = Table(title="📚 Acervo Completo da Biblioteca", header_style="bold green")
        
        # Define as colunas do seu painel antigo
        tabela.add_column("Livro", style="white", width=25)
        tabela.add_column("Autor", style="magenta", width=20)
        tabela.add_column("Lançamento", style="yellow", justify="center", width=12)
        tabela.add_column("Status", justify="center", width=15)
        tabela.add_column("Leitor Atual", style="cyan", width=15)
        
        for livro in livroload["Livros"]:
            # Define o texto e a cor com base na disponibilidade
            if livro["Disponivel"]:
                status = "[bold green]Disponível[/]"
                leitor = "-"
            else:
                status = "[bold red]Emprestado[/]"
                # O .get() evita erros caso a estrutura do JSON varie
                emprestimo = livro.get("Emprestimo", {})
                leitor = emprestimo.get("Leitor", "Não informado") if emprestimo else "Não informado"
            
            # Adiciona a linha na tabela
            tabela.add_row(
                livro["Livro"],
                livro["Autor"],
                str(livro["Lancamento"]),
                status,
                leitor
            )
            
        # Imprime a tabela completa
        print(tabela)
        
    except Exception as e:
        # Uso do console.print para garantir que a cor vermelha funcione
        print(f"[bold red]Erro: {e}. Tente novamente.[/]")


def searchlivro():
            name = input("Livro que deseja encontrar: ")
            arq = loadjson(arquivo)
            exist = False
            disp = ''
            for livro in arq["Livros"]:
                if name.strip().casefold()==livro["Livro"].strip().casefold():
                    if livro['Disponivel']:
                        disp = 'Disponivel'
                    else:
                        disp = 'Emprestado'
                    tabela = Table(title='livro encontrado: ')
                    tabela.add_column('livro')
                    tabela.add_column('autor')
                    tabela.add_column('Status')
                    tabela.add_row(livro['Livro'],livro['Autor'],disp)
                    print(tabela)
                    exist = True   
            if not exist:
                print("[bold red]Livro não encontrado![/]")

def removelivro():
    try:
        data = loadjson(arquivo)
        livrodel = input("Livro que deseja remover: ")
        livroexist = False
        for livro in data["Livros"]:
            if livrodel.strip().casefold()==livro["Livro"].strip().casefold():
                while True:
                    decision = input("Tem certeza que deseja remover o livro d biblioteca? press[S/N]: ").upper()
                    if decision =='S':
                        data["Livros"].remove(livro)
                        livroexist=True
                        atualizarjson(data)
                        print("[bold green]Livro removido com sucesso[/]")
                        break
                    elif decision =='N':
                        print(f"[red]Operação cancelada.")
                        livroexist=True
                        break
        if livroexist==False:
            print("[bold red]Livro não encontrado[/]")
    except Exception as e:
        print(f"[bold red]Erro de {e},tente novamente.[/]")
       
def emprestarlivro():
    try:
        dadoss = loadjson(arquivo)
        namelivro = input("Qual livro deseja pegar?: ")
        livroexst = False
        data = f"{date.today().year}-{date.today().month}-{date.today().day:02d}"
        hoje = date.today()
        validade = timedelta(days=30)
        prazo = hoje+validade
        prazformat = prazo.strftime("%Y-%m-%d")

        for livro in dadoss["Livros"]:
            if namelivro.strip().casefold()==livro["Livro"].strip().casefold():
                livroexst = True
            if namelivro.strip().casefold()==livro["Livro"].strip().casefold() and livro["Disponivel"]==True:
                yourname = input("Digite seu nome: ")
                livro["Disponivel"] = False
                livro["Emprestimo"]["Leitor"] = yourname
                livro["Emprestimo"]["Data"] = data
                livro["Emprestimo"]["Validade"] = prazformat
                atualizarjson(dadoss)
                print("[bold green]O livro está disponível![/]")
                print(f"[bold green]Livro {livro["Livro"]} emprestado para {yourname}. Boa leitura![/]")
            else:
                if namelivro.strip().casefold()==livro["Livro"].strip().casefold() and livro["Disponivel"]==False:
                    print("[red]Este livro já foi emprestado.[/]\nPor favor,escolha outro livro")
        if not livroexst:
            print("[bold red]Livro não encontrado!")
    except Exception as e:
        print(f"[bold red]Erro de {e},tente novamente.[/]")

def devolverlivro():
    livross = loadjson(arquivo)
    livrodevol = input("Qual o nome do livro você deseja devolver?: ")
    livroexist = False
    for livro in livross['Livros']:
        if livrodevol.strip().casefold() == livro['Livro'].strip().casefold() and not livro['Disponivel']:
            livroexist = True
            livro['Disponivel'] = True
            livro['Emprestimo']['Leitor'] = None
            livro['Emprestimo']['Leitor']=None
            livro['Emprestimo']['Data'] = None
            livro['Emprestimo']['Validade'] = None
            atualizarjson(livross)
            print(f"[bold green]Livro {livrodevol} devolvido com sucesso![/]")
            
        elif livrodevol.strip().casefold() == livro['Livro'].strip().casefold() and livro['Disponivel']:
            print("[blue]Este livro já está disponível na nossa biblioteca.\n"
            "Não é necessario uma devolução[/]")
            livroexist=True  # para o último if não executar

    if not livroexist:
        print("[bold blue]Este livro não existe na nossa biblioteca.[/]")
from rich.console import Console
from rich.table import Table

console = Console()

def livrodisp():
    dadoslivrr = loadjson(arquivo)
    
    # Criamos a tabela fora e antes do loop para acumular os dados
    tabela = Table(title="📖 Livros Disponíveis", title_style="bold white", header_style="bold cyan")
    tabela.add_column('Livro', style="bold")
    tabela.add_column('Autor', style="magenta")
    tabela.add_column('Lançamento', justify="center", style="green")
    
    # Preenchemos a tabela com as linhas
    for livro in dadoslivrr["Livros"]:
        if livro["Disponivel"]:
            tabela.add_row(livro['Livro'], livro['Autor'], str(livro['Lancamento']))
            
    # Imprimimos o resultado final consolidado
    console.print(tabela)

from rich.console import Console
from rich.table import Table

console = Console()

def loadlivrosemprest():
    data = loadjson(arquivo)
    
    # Criamos a tabela antes do loop para acumular todos os empréstimos
    tabela = Table(title="🤝 Livros Emprestados", title_style="bold green", header_style="bold green")
    
    # Definimos as colunas para organizar os dados do painel antigo
    tabela.add_column("Livro", style="white", width=30)
    tabela.add_column("Leitor", style="magenta", width=20)
    tabela.add_column("Desde", style="yellow", justify="center", width=15)
    
    for livro in data["Livros"]:
        if not livro["Disponivel"]:
            # Adiciona os dados internos do objeto 'Emprestimo' diretamente nas colunas
            tabela.add_row(
                livro['Livro'], 
                livro['Emprestimo']['Leitor'], 
                livro['Emprestimo']['Data']
            )
            
    # Imprime a tabela completa de uma só vez
    console.print(tabela)

            
import json
from rich.console import Console
from rich.table import Table

def estatisticas():
    # ... ( código de processamento de dados ) ...
    data = loadjson(arquivo)
    totallivrosdipp = 0
    livroemprest = 0
    anolivromaisantig = 99**77
    livromaisant = ''
    autordolivro = ''
    totallivros = len(data.get('Livros', None))
    autormaisapara = ''
    numervzs = 0

    for livro in data["Livros"]:
        if livro["Disponivel"]:
            totallivrosdipp += 1
        if not livro['Disponivel']:
            livroemprest += 1

    for autor in data["Livros"]:
        if int(autor['Lancamento']) < anolivromaisantig:
            livromaisant = autor['Livro']
            anolivromaisantig = int(autor['Lancamento'])
            autordolivro = autor['Autor']

    for autor in data["Livros"]:
        if autor["Autor"].strip().casefold() != autormaisapara.strip().casefold():
            autormaisapara = autor["Autor"]
        elif autor["Autor"].strip().casefold() == autormaisapara.strip().casefold():
            numervzs += 1

    # --- Configuração da Tabela Rich ---
    console = Console()
    
    # Cria a tabela com um título e borda estilizada
    tabela = Table(title="📊 Estatísticas da Biblioteca", show_header=True, header_style="bold magenta")
    
    # Define as colunas
    tabela.add_column("Métrica", style="cyan", width=30)
    tabela.add_column("Resultado", style="green", width=40)

    # Adiciona as linhas com os seus dados calculados
    tabela.add_row("Total de livros", f"{totallivros} livros")
    tabela.add_row("Livros disponíveis", f"{totallivrosdipp} livros")
    tabela.add_row("Livros emprestados", f"{livroemprest} livros")
    tabela.add_row("Livros mais antigo", f"[italic]{livromaisant}[/] ({anolivromaisantig}) - {autordolivro}")

    # Imprime a tabela no terminal
    console.print(tabela)


def atualizarjson(dadosparaatualizar):
    try:
        with open(arquivo,'w',encoding='utf-8') as arquivojson:
            json.dump(dadosparaatualizar,arquivojson,indent=4,ensure_ascii=False)
            # Não precisa de return pois não retorna valor para eu usar
            # return significa “a função está entregando um valor de volta para quem a chamou.”
    except Exception as e:
        print(f'Ocorreu um erro de {e}')

def sleepexit():
    print('.',end='')
    sleep(0.7)
    print('.',end='')
    sleep(0.7)
    print('.',end='')

def relatorio():
    relatorio = r"/home/carlos/programação/vs code/hmtl-css-study/Exercícios/manipulandojson/projeta biblioteca v2/Relatório.txt"
    dados = loadjson(arquivo)
    ttlivrempre = 0
    for livro in dados['Livros']:
        if not livro["Disponivel"]:
            ttlivrempre+=1


#criarjson("Bibliotecav2.json")
arquivo = r"/home/carlos/programação/python/API/manipulandojson/projeta biblioteca v2/Bibliotecav2.json"
#Cadastrando novo livro, ao adicionar novo livro ele Define automaticamente Disponivel = True e Leitor = None.
while True:
    opcoes()
    escolha = input("Sua opção: ").upper()
    match escolha.strip():
        case '0':
            carregarlivros()
        case '1':
            cadastrarlivro()
        case '2':
            searchlivro()
        case '3':
            removelivro()
        case '4':
            emprestarlivro()
        case '5':
            devolverlivro()
        case '6':   
            livrodisp()
        case '9':
            sleepexit()
            print("[green]Volte sempre![/]")
            break
        case '7':
            loadlivrosemprest()
        case '8':
            estatisticas()
        case _:
            print("[red]Opção inválida[/]") # se não corresponder a nenhuma das condições execute isso


