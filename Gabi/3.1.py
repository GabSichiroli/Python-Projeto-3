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
    print("\t\t\n 3- Informações por quantidade de escalas")
    print("\t\t\n 4- Listar Passageiros do Voo")
    print("\t\t\n 5- Venda de passagem")
    print("\t\t\n 6- Cancelamento De Passagem")
    print("\t\t\n 7- Sair")
    x=int(input("Insira a opção:"))
    os.system('cls')
    return x
#Cadastro de Voos

def cadastro_voos(voos,totalvoos):
    print("Cadastro de Voos")
    quant = int(input("Insira a quantidade de voos que deseja cadastrar desta vez: "))
    i = 0
    while i < quant:
        codvoo =int(input("Insira o código do voo: "))
        if codvoo in voos:
            print(f"\n\t\t=> VOO JÁ EXISTENTE <==\n")
        else:
            numerodepassageiros = 0
            capMAX = int(input("Capacidade máxima: "))
            cidadeorigem = input("Cidade de origem: ").upper()
            cidadedestino = input("Cidade de destino: ").upper()
            quantescalas = int(input("Quantidade de escalas, se nenhuma digite 0:"))
            preco=float(input('Insira o preço da passagem do voo: '))
            voos[codvoo] = [cidadeorigem,cidadedestino,quantescalas, preco, capMAX, numerodepassageiros ]
            i += 1
    totalvoos += quant
    return voos, totalvoos

#Consuta de voo por chave
def consuta(voos):
    print("\nVoos cadastrados:")
    for codigo, dados in voos.items():
        print(f"{codigo}: {dados}")
    input("\t\t\n\t PRESIONE ENTRER PARA ENTRAR")
    os.system('cls')

#Menu de buscas de informações de pesquisa de voo
def minimenu():
    print('Como deseja consultar o voo? ')
    print('[1]- Código do Voo')
    print('[2]- Cidade de Origem')
    print('[3]- Cidade de destino')
    print('[4]- Sair')
    x=int(input("Insira a opção:"))
    os.system('cls')
    return x

def codvoo_busca(voos):
    codigo=int(input('Digite o código do voo: '))
    if codigo in voos.keys():
        print(f'Cidade origem: {voos[codigo][0]}')
        print(f'Cidade destino: {voos[codigo][1]}')
        print(f'Número de Escalas: {voos[codigo][2]}')
        print(f'Preço da Passagem: {voos[codigo][3]}')
        print(f"Capacidade maxima: {voos[codigo][4]}")
        print(f"Numero de passageiros:{voos[codigo][5]}")
    else:
        print(f"\n\t{codigo} não consta no banco de dados")
    input("\t\t\n\t PRESIONE ENTRER PARA CONTINUAR")    
    os.system('cls')
def buscaorigem(voos):
    corigem=int(input('Digite o código do voo: '))
    for k,v in voos.items():
        if v[0] == corigem:
            print(f'Código do voo: {k}')
            print(f'Cidade Destino: {[v[1]]}')
            print(f'Preços de Passagem para esse voo: {v[3]}')
    
        
def menorescala ():
    print("Menor escala")
    input("\t\t\n\t PRESIONE ENTRER PARA ENTRAR")
    os.system('cls')

#Listar Passageiros
def listarpassageiros():
    print("Lista")
    input("\t\t\n\t PRESIONE ENTRER PARA ENTRAR")
    os.system('cls')
def vendapassagem():
    print("Venda")
    input("\t\t\n\t PRESIONE ENTRER PARA ENTRAR")
    os.system('cls')

def cancelarvenda():
    print("Cancelar Venda")
    input("\t\t\n\t PRESIONE ENTRER PARA ENTRAR")
    os.system('cls')
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
            dicvoo,totalvoos=cadastro_voos(dicvoo,totalvoos)
            print(f"{totalvoos}")
        case 2:
            while True:
                auxop=minimenu()
                match auxop:
                    case 1:
                        codvoo_busca(dicvoo)
                    case 2:
                        buscaorigem(dicvoo)
                    case 3:
                        print("3")
                    case 4:
                        break
        case 3:
            menorescala()
        case 4:
            listarpassageiros()
            print("ok4")
        case 5:
            vendapassagem()
            print("ok5")
        case 6:
            cancelarvenda()
            print("ok6")
        case 7:
            print("ok7")
            break
        case _:
            print("Opção Invalida")
            escolha()