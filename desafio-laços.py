import time

#for c in range(11,0,-1):
 #   time.sleep(1)
  #  print(c)
#print('🧨🧨💥💥')

#num = int(input('Digite um número: '))   
#for i in range(1,11):    #variável i repete conforme a sequência do range
 #   print(f' {num} x {i} = {num*i}')   # variável i representa cada número da sequência do range e faz o script ficar limpo

#lis = []
#for i in range(1,7):
   # resp = int(input(f'Digite o número {i}:')) # repete a pergunta no total do range
  #  if resp % 2==0:  - - - verifica se os números do resp é par
 #      lis.append(resp) adiciona eles a lista (lis) se for true com a condição do if
#print(f'A soma total foi de:\n{sum(lis[0:6])}')  soma os valores da lista
cont = True
lista_ano=[]
lista_idade = []

from datetime import date

lista_ano = []
lista_idade = []

for r in range(1,8):
  while True:
    try:
      ano = int(input(f'Digite o ano da {r} pessoa: '))
      lista_ano.append(ano)
      break
    except ValueError:
      print('digite um número válido')

data = date.today().year
for ano in lista_ano:
    idade =  data - ano
    if idade>=18:
      lista_idade.append(idade)
print(f'Apenas {len(lista_idade)} de 7 pessoas são maiores de idade.')