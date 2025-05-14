#Bibliotecas:

import os
import sys

#Tela Inicial (Ainda não finalizada)
def telainicial ():
    print("\t\t\n\n Bem vindo a (EMPRESA FAXADA AQUI HEHE)")
    input("\t\t\n\t PRESIONE ENTRER PARA ENTRAR")
    os.system('cls')

#Escolha de opção dentro do que o usuario
def escolha():
    print("\t\t\n 1- Cadastar Voo")
    print("\t\t\n 2- Consutar Voo")
    print("\t\t\n 3- Informar o Voo")
    print("\t\t\n 4- Listar Passageiros do Voo")
    print("\t\t\n 5- Venda de passagem")
    print("\t\t\n 6- Cancelamento De Passagem")
    print("\t\t\n 7- Sair")
    x=int(input("Insira a opção:"))
    os.system('cls')
    return x
#Main
telainicial()
print("ok")
op=escolha()
print(f"{op}")
match op:
    case 1:
        print("ok1")
    case 2:
        print("ok2")
    case 3:
        print("ok")
    case 4:
        print("ok4")
    case 5:
        print("ok5")
    case 6:
        print("ok6")
    case 7:
        print("ok7")
        sys.exit(0)