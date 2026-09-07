import random
import time
from operator import itemgetter
jgdrs = {}
print('Valores sorteados: ')
for j in range(1,5):
   
    jgdrs [f'Jogador {j}'] = random.randint(1,6)
    
# cada chave "jogador" recebe um valor aleatório
    #Jogador {j} é justamente para ser cada chave do dicionário
print('...')
time.sleep(1)
for k,v in jgdrs.items():# para cada chave e valor delas no dicionário jgdrs.items(tudo), mostre o print de cada um como pede abaixo...
    print(f'O jogador {k} jogou {v}')
    time.sleep(1)# K é chave do jogador e V o valor que tem nela

ranking = sorted(jgdrs.items(),key=itemgetter(1),reverse=True)# reverse=true faz ser em ordem descrescente. 
#key=itemgetter(1) fala sobre a chave e o valor que está nela

for i,e in enumerate(ranking):# enumera e deixa a lista limpa
    print(f'{i+1} Lugar {e[0]} que jogou {e[1]}')# i+ é para sair apartir do 1 e não 0. e[0],e[1] é respectivamente chaves e valores dela