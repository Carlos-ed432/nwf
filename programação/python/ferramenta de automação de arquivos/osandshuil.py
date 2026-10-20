import os
import shutil

cont = True
while cont:
    caminho = input("Digite o seu diretório: ")
    try:
     arquivos = os.listdir(caminho)
    except:
        print('\033[31mERRO! digite um diretótio válido!\033[0m')
        continue
    destino = input("Digite o nome que você quer dar a sua pasta: ")
    while True:
        tipodearquiv = input("Digite o tipo de arquivo com um . no inicio, ex: .pdf, .png: ").strip()
        if tipodearquiv[0]!='.':
             print('Digite com o formato correto!')
        else:
             break
    destino = os.path.join(caminho,destino)
    os.makedirs(destino,exist_ok=True) # Criando a pasta no endereço certo
    contador=0
    for arq in arquivos:
        caminhoatual = os.path.join(caminho,arq)        
        if os.path.isdir(caminhoatual): # se o caminho levar a uma subpasta, ignore e continue
                continue
        nomedoarq,extensao=os.path.splitext(arq)
        if extensao in tipodearquiv:
            shutil.move(caminhoatual,destino)
            contador+=1

            

    if contador==0:

         print(f'\033[33mArquivo com fim {tipodearquiv} não encontrado\033[0m')

    else:
        print(f" \033[32m{contador} arquivos movidos com sucesso!\033[0m")
        cont=False

    continuar = input("Deseja continuar? PRES[S/N]: ").strip().upper()
    if continuar =='S':
        cont=True
    elif continuar=='N':
        cont=False