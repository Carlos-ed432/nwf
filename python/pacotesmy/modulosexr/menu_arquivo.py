import sys
from pathlib import Path

# Adiciona a pasta raiz (/programação/python) ao sys.path do Python
sys.path.append(str(Path(__file__).resolve().parent.parent.parent))

from pacotesmy.arquiv import funcoes
from time import sleep

# Sobe um nível a partir de modulosexr para chegar na raiz 'python' e achar o arquivo. arquivo guardado aqui
arq = Path(__file__).resolve().parent.parent / 'Programadecadastro.txt'

if not funcoes.arquivoexist(arq): #verifica se o arquivo existe 
    #if not= e cria um caso não exista 
    funcoes.criararquivo(arq) 
    
cont1 = True
while cont1:
    ab = "        MENU PRINCIPAL       "
    print(funcoes.visual(ab))
    print(ab)
    print(funcoes.visual(ab))
    funcoes.opções()
    cont2 = True
    
    while cont2:
        try:
            selectopç = int(input("\033[33mSua opção:\033[0m "))
        except ValueError:
            print("\033[31mERRO! digite uma opção válida\033[0m")
            print(f"\033[37m\033[0m{'—'*29}")
            continue
            
        if selectopç == 1:
            with open(arq, "r", encoding="utf-8") as arquivo:
                for linha in arquivo:
                    print(f"{linha.strip()}")
            cont2 = False
            
        elif selectopç == 2:
            with open(arq,"a", encoding="utf-8") as arquivo:
                # --- VALIDAÇÃO DO NOME ---
                while True:
                    nome = input("Nome: ").strip()
                    if nome == "":
                        print("\033[31mERRO! O nome não pode ficar em branco.\033[0m")
                    else:
                        break  # Nome válido, sai do laço do nome

                # --- VALIDAÇÃO DA IDADE (TRATAMENTO DE ERRO) ---
                while True:
                    try:
                        idade = int(input("Idade: "))
                        break  # Se digitou um número, o int() funciona e sai do laço da idade
                    except ValueError:
                        # Se digitou letras, o int() joga para cá e repete a pergunta
                        print("\033[31mERRO! Digite uma idade válida (apenas números).\033[0m")

                # --- SALVANDO NO ARQUIVO ---
                with open(arq, "a", encoding="utf-8") as arquivo:
                    arquivo.write(f" {nome:<15} {idade:>2} anos\n")
                    print("Dados salvos!")
                    cont2 = False
                    sleep(1.5)
                    
        elif selectopç == 4:
            while True:
                crtz = input("Tem certeza que deseja limpar todo o arquivo? press [S/N]: ").strip().upper()
                if crtz == 'S':
                    with open(arq, "w", encoding="utf-8"):
                        funcoes.sleepexit2()
                        print("Arquivo limpo com sucesso!")
                        break
                elif crtz == 'N':
                    break
                    
        elif selectopç == 3:
            print("Saindo do sistema")
            sleep(0.5)
            funcoes.sleepexit()
            cont1 = False
            cont2 = False
