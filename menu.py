
cont = True
cont2 = True

while cont2:
    try:
        c = int(input('Digite o número 1: '))
        d = int(input('Digite o número 2: '))
        cont = True
        while cont:
            menu = int(input('Digite um dos números abaixo que corresponde a ação que você deseja: \n  [1] - somar\n  [2] - multiplicar\n  [3] - maior número\n  [4] - novos números\n  [5] - sair do programa  '))
            if menu == 1:
                print(f'somando {c} + {d} temos {c+d} ')
            elif menu == 2:
                print(f'O resultado da multiplicação é{c*d}')
            elif menu == 3:
                print(f'O maior número é {max(c,d)}')
            elif menu == 4:
                 cont = False
            elif menu == 5:
                cont = False
                cont2 = False
                print('Volte sempre :)')
    except ValueError:
        print('Digite um número válido')
                    

                
       