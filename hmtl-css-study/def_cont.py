import time
def personalizar():
    print()
    print('FIM')
    print('='*20)


print('='*20)
print('Contagem de 1 até 10 de 1 em 1')
for i in range(1,11):
    print(f"{i}",flush=True,end=" ")
    time.sleep(0.5)
personalizar()



print('Contagem de 10 até 0 de 2 em 2')
for C in range(10,-1,-2):
    print(f"{C}",flush=True,end=" ")
    time.sleep(0.5)
personalizar()


def contador(a,b,c):

    if a>b and c>0:
        print(f"Contagem de {a} a {b} de {1} em {1}")
        for v in range(a,b-1,-1):
            print(f"{v}",flush=True,end=" ")
            time.sleep(0.5)
        print('FIM')
    elif a>b and c<0:
        print(f"Contagem de {a} a {b} de {1} em {1}")
        for v in range(a,b-1,-1):
            print(f"{v}",flush=True,end=" ")
            time.sleep(0.5)
        print('FIM')
    elif a<b and c<0:
        print(f"Contagem de {a} a {b} de {1} em {1}")
        for v in range(a,b+1,1):
            print(f"{v}",flush=True,end=" ")
            time.sleep(0.5)
        print('FIM')
    elif a<b and c<=0 :
        print(f"Contagem de {a} a {b} de {1} em {1}")
        for v in range(a,b+1,1):
            print(f"{v}",flush=True,end=" ")
            time.sleep(0.5)
        print('FIM')
    elif a>b and c<=0:
        print(f"Contagem de {a} a {b} de {1} em {1}")
        for v in range(a,b-1,-1):
            print(f"{v}",flush=True,end=" ")
            time.sleep(0.5)
        print('FIM')

    else:
        print(f"Contagem de {a} a {b} de {c} em {c}")
        for v in range(a,b+1,c):
            print(f"{v}",flush=True,end=" ")
            time.sleep(0.5)
        print('FIM')






print('Agora é sua vez de personalizar a contagem! ')
a = int(input('Início: '))
b = int(input('Fim: '))
c = int(input('Passo: '))
contador(a,b,c)






#"contador feito quando eu estava começando a aprender funções"



