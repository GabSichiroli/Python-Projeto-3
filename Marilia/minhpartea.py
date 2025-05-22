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

#cancelar passagem
def cancelarvenda():
    codvoo=int(input("Digite qual o código do voo:"))
        if codvoo in voos:



        else:
            print("codigo de voo nao encontrado")
    input("\t\t\n\t PRESIONE ENTRER PARA ENTRAR")
    os.system('cls')
