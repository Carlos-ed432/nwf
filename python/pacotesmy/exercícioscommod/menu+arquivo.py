from time import sleep
def sleepexit():
    print('.',end='',flush=True)
    sleep(0.5)
    print('.',end='',flush=True)
    sleep(0.5)
    print('.')

def opções():
    print(f"\033[33m1\033[0m - \033[34mVer pessoas cadastradas[0m ")
    print(f"\033[33m2\033[0m - \033[34mCadastrar nova pessoa[0m ")
    print(f"\033[33m3\033[0m - \033[34mSair do sistema[0m ")

def visual(a):
    tamanho = len(a)
    tamanho = (f"{'—'*tamanho}")
    return tamanho

ab = "        MENU PRINCIPAL       "
print(visual(ab))
print(ab)
print(visual(ab))
opções() 



print(f"\033[37m\033[0m{'—'*29}")



selectopç=int(input("\033[33mSua opção:\033[0m "))
if selectopç==1:
    print("x")
elif selectopç==2:
    nome = input("Nome: ")
    idade = input("Idade: ")
    print(f"Novo registro de {nome} registrado")
elif selectopç==3:
    print("Saindo do sistema")
    sleep(0.5)
    sleepexit()



        
