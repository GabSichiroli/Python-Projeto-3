#Bibliotecas:

import os

#Tela Inicial (Ainda não finalizada)
def telainicial ():
    print("\t\t\n\n Bem vindo a (EMPRESA FAXADA AQUI HEHE)")
    input("\t\t\n\t PRESIONE ENTRER PARA ENTRAR")
    os.system('cls')

#Escolha de opção dentro do que o usuario
def escolha():
    print("\t\t\n 1- Cadastar Voo")
    print("\t\t\n 2- Consutar Voo")
    print("\t\t\n 3- Informações do Voo")
    print("\t\t\n 4- Listar Passageiros do Voo")
    print("\t\t\n 5- Venda de passagem")
    print("\t\t\n 6- Cancelamento De Passagem")
    print("\t\t\n 7- Sair")
    x=int(input("Insira a opção:"))
    os.system('cls')
    return x

#Cadastro de Voos
def cadastro_voos(voos,totalvoos):
    voos={}
    print("Cadastro")
    quant=int(input("Inira a quantidade de voos que deseja cadastar dessas vez:"))
    attvoos=totalvoos+quant
    input("\t\t\n\t PRESIONE ENTRER PARA ENTRAR")
    os.system('cls')
    return attvoos

#Consuta de voo por chave
def consuta():
    print("consuta")
    input("\t\t\n\t PRESIONE ENTRER PARA ENTRAR")
    os.system('cls')

#Menu de buscas de informações de pesquisa de voo
def minimenu():
    print("\t\t\n\t Como deseja realizar a consuta:")
    print("\t\t\n 1- Cidade de destino")
    print("\t\t\n 2- Menor quantidade de escalas")
    print("\t\t\n 3- Cidade de Origem")
    print("\t\t\n 4- Cidade de Origem ate tal destino")
    x=int(input("Insira a opção:"))
    os.system('cls')
    return x
#Main
dicvoo={}
totalvoos=0
telainicial()
print("ok")
while True:
    op=escolha()
    print(f"{op}")
    match op:
        case 1:
            print("ok1")
            os.system('cls')
            totalvoos=cadastro_voos(dicvoo,totalvoos)
            print(f"{totalvoos}")
        case 2:
            consuta()
        case 3:
            minimenu()
        case 4:
            print("ok4")
        case 5:
            print("ok5")
        case 6:
            print("ok6")
        case 7:
            print("ok7")
            break
        case _:
            print("Opção Invalida")
            escolha()
