import random
venceu = 0 # Acumulador onde guardar a quantidade de vez que o usuário venceu a máquina


while True:
   try: # tenta executar sem erros

      print('=======================\nVAMOS JOGAR PAR OU IMPAR\n =======================')
      valor = int(input('Digite um valor: '))
      computador = random.randint(1,100)# "pensa" um número e guarda na variável computador
      Par_ou_impar = input('Você é par ou impar?  [P/I] : ').strip().upper()[0]#remove espaços vazios e deixa o p ou i em maíusculo e pega só a primeira
      #letra da entrada para caso digitem par ou impar completos
      vv = valor+computador

      if vv%2 == 0 and Par_ou_impar == 'P':#Se a soma da entrada valor com o valor da variável for =0, deu par. e se a entrada par_ou_impar
         #f=r = I, o usuário ganha
         print(f'você jogou {valor} e eu joguei {computador}, {vv} é Par. Você ganhou! ')
         venceu+=1
      elif vv%2 == 0 and Par_ou_impar!= 'P':
         print(f'você jogou {valor} e eu joguei {computador}, {vv} é par. Você perdeu')# se não, você perde. 
         print(f'você venceu {venceu} vezes')
         break
      elif vv%2 != 0 and Par_ou_impar =='I':
         print(f'você jogou {valor} e eu joguei {computador}, {vv} é impar. Você ganhou!')
         venceu+=1
      elif vv%2 != 0 and Par_ou_impar!='I':
         print(f'você jogou {valor} e eu joguei {computador}, {vv} é impar. Você perdeu.')
         print(f'você venceu {venceu} vezes')
         break    
   except ValueError:
      print('Digite um número válido')