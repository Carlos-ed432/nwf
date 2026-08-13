import random

tentativass = 0
num = random.randint(1,2) # Escolhe um número entre 1 e 2 e guarda na variável num
while True:
    try:
        perg = int(input('Digite o número que estou pensando 😂: ')) #se falhar,ValueError
        #acontece → perg nem recebe aquele valor → pula para except
        tentativass+=1 # Adiciona +1 em tentativas ao responder. Mas se não responder com número ele não adiciona e sim vai para a linha do 
        #except error e volta o laço novamente pro inicio. Só números válidos conseguem chegar até tentativas += 1

        if perg == num and tentativass ==1:
            print(f'Você acertou de primeira!')
            break # se acertar na primeira tentativa já encerra. 
        if perg == num:
            print(f'Você acertou! acertou depois de {tentativass} tentativas') #Mostra certo na tela quando acertar, no caso dessa linha,
            #quando não for de primeira.
            break
    except ValueError:      #Mostra o print e volta o laço se der erro na primeira linha =perg
         print('Digite um número válido') 
