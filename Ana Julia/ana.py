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
    cidadedeorigem=str(input('Insira a cidade origem do voo: '))
    while True:             
        for k,v in voos.items():
            if v[0] == cidadedeorigem:
                print(f'Código do voo: {k}')
                print(f'Cidade Destino: {[v[1]]}')
                print(f'Numeros de Escalas: {[v[2]]}')
                print(f'Preços de Passagem para esse voo: {v[3]}')
                break
            else:
                print("N tem")
          
def menorescala (voos):
    origem = input("Digite a cidade de origem: ").upper()
    destino = input("Digite a cidade de destino: ").upper()
    encontrou = False
    #primeiro voo encontrado com as informações digitadas
    primeiro = True
    for cod in voos:
        #verifica se o voo tem a mesma origem do destino
        if voos[cod][0] == origem and voos[cod][1] == destino:
            if primeiro:
                #recebe o número de escalas desse voo
                menor_escalas = voos[cod][2]
                cod_menor = cod
                #é marcado como falso para comparar os próximos voos
                primeiro = False
                #marca que foi achado um voo válido
                encontrou = True
                #se o voo atual tem menos escalas do que o menor até agora
            elif voos[cod][2] < menor_escalas:
                menor_escalas = voos[cod][2]
                cod_menor = cod
                encontrou = True
    if encontrou:
        print(f"\nVoo com menor número de escalas:")
        print(f"Código: {cod_menor}")
        print(f"Origem: {voos[cod_menor][0]}")
        print(f"Destino: {voos[cod_menor][1]}")
        print(f"Escalas: {voos[cod_menor][2]}")
        print(f"Preço: R${voos[cod_menor][3]}")
    else:
        print("Nenhum voo encontrado entre as cidades informadas.")
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
            menorescala(dicvoo)
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
