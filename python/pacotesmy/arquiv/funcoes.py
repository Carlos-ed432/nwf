from time import sleep
def arquivoexist(nome):
        try:
            a = open(nome,'rt')
            a.close()
        except FileNotFoundError:
            return False
        else:
            return True

        
def criararquivo(nome):
     try:
        a = open(nome,'wt+')# lê o param e cria um arquivo se ele não existir
        a.close()
     except:
         print("Houve um erro na criação")
     else:
        print(f"Arquivo {nome} criado com sucesso")


def lerarquivo(nome):
    try:
        a = open(nome,'rt')
    except:
        print("Erro ao ler arquivo")
    else:
        print(a.readline())


def sleepexit2():
    print('.',end='',flush=True) # função criada para sair como um sistema em sleep 0.5
    sleep(0.5)
    print('.',end='',flush=True)
    sleep(0.5)
    print('.')
    sleep(0.5)


def sleepexit():
    print('.',end='',flush=True) # função criada para sair como um sistema em sleep 0.5
    sleep(0.5)
    print('.',end='',flush=True)
    sleep(0.5)
    print('.')
    sleep(0.5)
    print("\033[32mVolte sempre :)")

def opções():
    print(f"\033[33m1\033[0m - \033[34mVer pessoas cadastradas ")
    print(f"\033[33m2\033[0m - \033[34mCadastrar nova pessoa ")  #função que apresenta as opções
    print(f"\033[33m3\033[0m - \033[34mSair do sistema ")
    print(f"\033[33m4\033[0m - \033[34mLimpar arquivo ")

def visual(a):
    tamanho = len(a)  #função de visual
    tamanho = (f"{'—'*tamanho}")
    return tamanho


