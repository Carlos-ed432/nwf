import json
from rich import print
from rich.console import Console
from rich.panel import Panel

def criarq(nome):
    try:
        with open(nome,'x',encoding='utf-8'):
            pass
    except FileExistsError:
        pass

def opções():
    return Panel("1 - [bold blue]Ver livros[/]\n2 - [bold blue]Adicionar novo livro[/]\n3 -[bold blue] Pesquisar livro[/]\n4 - [bold blue]Remover livro[/]\n5 - [bold blue]Sair[/]\n",width=30,title="[white] Selecione uma opção[/]",border_style="bold blue")
def loadjson(caminhodoarq):
    with open(caminhodoarq,'r',encoding='utf8') as arquivo:
        return json.load(arquivo)

cont = True
#criarq("livros.json")
while True:
    print(opções())
    arquivo = r"/home/carlos/programação/vs code/hmtl-css-study/Exercícios/manipulandojson/livros.json"
    data =loadjson(arquivo)
    print('')
    try:
        opç = int(input("Sua opção: "))
    except ValueError:
        print("[bold red]Selecione uma opção válida[/]")
    else:
        if opç==1:
            for livr in data["Livros Clássicos"]:
                print(Panel(f"Nome do livro: {livr["Livro"]}\nData de lançamento: {livr["Lançamento"]}\nAutor: {livr["Autor"]}",width=30,border_style="green"))
            print(' ============================')

        elif opç==2:
            livro = input("Nome do livro: ")
            lançamento = input("Data de lançamento do livro: ")
            Autor = input("Autor do livro: ")
            dadoslivro = {"Livro":livro,"Lançamento":lançamento,"Autor":Autor}
            try:
                with open(arquivo,'r',encoding='utf-8') as livr:
                    dadosjson = json.load(livr)
            except:
                dadosjson = {"Livros Clássicos":[]}
            with open(arquivo,'r',encoding='utf-8') as livross:
                livross = json.load(livross)
                livroexist = False
                for liv in livross["Livros Clássicos"]:
                    if livro.strip().casefold() == liv["Livro"].strip().casefold():
                        livroexist = True
                        print("[bold red]O livro já existe na lista[/]")
                if livroexist == False:
                    dadosjson["Livros Clássicos"].append(dadoslivro)
                    with open(arquivo,'w',encoding='utf-8') as arqlivr:
                        json.dump(dadosjson,arqlivr,indent=4,ensure_ascii=False)
                        print("[bold green]Livro adicionado com sucesso[/]")
        elif opç==3:
            search = input("Digite o nome do livro que quer encontrar: ")
            dadoslivr = loadjson(arquivo)
            for i in dadoslivr["Livros Clássicos"]:
                if search.strip().casefold() == i["Livro"].strip().casefold():
                    print(Panel(f"Nome do livro: {i["Livro"]}\nLançamento: {i["Lançamento"]}\nAutor: {i["Autor"]}",width=30,border_style="green"))
                    break
            else:
                print("[bold red]Livro não encontrado[/]")
        
        elif opç==4:
            livrodel = input("Digite o nome do livro que deseja remover: ")
            while cont:
                crtz = input(f"Tem certeza que deseja remover o livro {livrodel} ? press [S/N]").strip().upper()
                if crtz not in ["S","N"]:
                    print("[bold red]Digite uma opção válida.[/]")
                    cont=True
                else:
                    cont=False
            dadosdel = loadjson(arquivo)
            for livrr in dadosdel["Livros Clássicos"]:
                if livrodel.strip().casefold()==livrr["Livro"].strip().casefold():
                    dadosdel["Livros Clássicos"].remove(livrr)
                    print("[bold green]Livro removido com sucesso![/]")
                    break
            else:
                print("[bold red]Livro não encontrado![/]")
            with open(arquivo,'w',encoding='utf-8') as ffinaly:
                json.dump(dadosdel,ffinaly,indent=4,ensure_ascii=False)
        else:
            print("[bold red]Selecione uma opção válida[/]")


