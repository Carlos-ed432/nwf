import os
import shutil

cont = True
while cont:
    caminho = input("Digite o seu diretório: ")
    try:
     arquivos = os.listdir(caminho)
    except:
        print('Digite um diretótio válido!')
        continue
    destino = input("Digite o nome que você quer dar a sua pasta: ")
    while True:
        tipodearquiv = input("Digite o tipo de arquivo com um . ex: .pdf, .png: ").strip()
        if tipodearquiv[0]!='.':
             print('Digite o formato correto')
        else:
             break
    destino = os.path.join(caminho,destino)
    os.makedirs(destino,exist_ok=True)
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

         print(f'Arquivo com fim {tipodearquiv} não encontrado')

    else:
        print(f" \033[32m{contador} arquivos movidos com sucesso!\033[0m")
        cont=False


    continuar = input("Deseja continuar? PRES[S/N]: ").strip().upper()
    if continuar =='S':
        cont=True
    elif continuar=='N':
        cont=False