import os
def telainicial():
    print('='*40)
    print("Bem vindo ao Gerenciamento de dict_voos! ")
    print('='*40)
    input( "\nPRESIONE ENTER PARA ENTRAR>>>>")
    os.system('cls')

def escolha():
    print('='*40)
    print(f'\t\tMenu')
    print('[1]- Cadastrar Voo')
    print('[2]- Consultar Voo')
    print('[3]- Voo com Menor Escala')
    print('[4]- Listar Passageiros do Voo')
    print('[5]- Venda de passagem')
    print('[6]- Cancelamento de Passagem')
    print('[7]- Sair')
    print('='*40)
    opcao_escolhida=int(input('\t\tInsira a opção: '))
    os.system('cls')
    return opcao_escolhida

def cadastro_voo(dict_voos,listavoos_disponiveis):
    quant=int(input('Insira a quantidade de voos que deseja cadastrar: '))
    for i in range(quant):
        numerovoo=input('Informe o código do voo: ')
        while numerovoo in dict_voos:
            print(f'VOO JÁ EXISTENTE!')
            numerovoo=input('Informe outro código de voo: ')
        cidadeorigem=str(input(f'Insira a cidade origem do voo: ')).upper()
        while cidadeorigem.isdigit() or cidadeorigem.isspace() or cidadeorigem=="":
            print(f'Cidade Inválida')
            cidadeorigem=str(input(f'Insira novamente a cidade origem do voo: ')).upper()
        cidadedestino=str(input(f'Insira a cidade destino do voo: ')).upper()
        while cidadedestino.isdigit() or cidadedestino.isspace() or cidadedestino=="":
            print(f'Cidade Inválida')
            cidadedestino=str(input(f'Insira novamente a cidade destino do voo: ')).upper()
        numescalas=int(input('Insira o número de escalas do voo: '))
        preco=float(input('Insira o preço da passagem do voo: '))
        quant_lugaresdisp=int(input('Informe quantos lugares a disponíveis nesse voo: '))
        dict_voos[numerovoo]=[cidadeorigem,cidadedestino, numescalas,preco, quant_lugaresdisp, []]
        listavoos_disponiveis.append(numerovoo)
        print(F'VOO CADASTRADO COM SUCESSO!')
        input( "\nPRESIONE ENTER PARA CONTINUAR>>>>")
        os.system('cls')
    return dict_voos, listavoos_disponiveis
def menu_consulta():
    print('='*40)
    print('Como deseja consultar o voo? ')
    print('[1]- Código do Voo')
    print('[2]- Cidade de Origem')
    print('[3]- Cidade de destino')
    print('[4]- Sair')
    print('='*40)
    escolha_consulta=int(input('\t\tInsira a opção: '))
    os.system('cls')
    return escolha_consulta

def consulta_numerovoo(dict_voos):
    codigo=input('Digite o código do voo: ')
    while codigo not in dict_voos:
            print(f'CÓDIGO NãO ENCONTRADO')
            codigo=(input(f'\nDigite outro código do voo: '))
    print('='*40)
    print(f'Cidade origem: {dict_voos[codigo][0].title()}')
    print(f'Cidade destino: {dict_voos[codigo][1].title()}')
    print(f'Número de Escalas: {dict_voos[codigo][2]}')
    print(f'Preço da Passagem: {dict_voos[codigo][3]}')
    print(f'A quantidade de lugares disponíveis do voo é {dict_voos[codigo][4]}')
    print('='*40)
    input( "\nPRESIONE ENTER PARA CONTINUAR>>>>")
    os.system('cls')

def consulta_origem(dict_voos):
    busca_origem=str(input('Insira a cidade origem do voo: ')).upper()
    encontrou_origem=False
    for k, v in dict_voos.items():
        if v[0] == busca_origem:
                    encontrou_origem= True
                    print('='*40)
                    print(f'Código do voo: {k}')
                    print(f'Cidade Destino: {v[1].title()}')
                    print(f'Preços de Passagem para esse voo: R${v[3]:.2f}') 
                    print('='*40)
                    input( "\nPRESIONE ENTER PARA CONTINUAR>>>>")
                    os.system('cls')
    if not encontrou_origem:
        print(f'Não existem voos cadastrados para a cidade {busca_origem}')
        print('='*40)
        input( "\nPRESIONE ENTER PARA CONTINUAR>>>>")
        os.system('cls')
def consulta_destino(dict_voos):
    busca_destino=str(input('Insira a cidade destino do voo: ')).upper()
    encontrou_destino= False
    for k, v in dict_voos.items():
        if v[1]==busca_destino:
            encontrou_destino = True
            print('='*40)
            print(f'Código do voo: {k}')
            print(f'Cidade Origem: {v[0].title()}')
            print(f'Preços de Passagem para esse voo: R${v[3]:.2f}') 
            print('='*40)
            input( "\nPRESIONE ENTER PARA CONTINUAR>>>>")
            os.system('cls')
    if not encontrou_destino:
        print(f'Não existem voos cadastrados com destino para a cidade {busca_destino}')
        print('='*40)
        input( "\nPRESIONE ENTER PARA CONTINUAR>>>>")
        os.system('cls')
        

def menor_escala(dict_voos):
        origem = input("Digite a cidade de origem: ").upper()
        destino = input("Digite a cidade de destino: ").upper()
        origem_existe= False
        destino_existe = False
        for v in dict_voos.values():
                if v[0]==origem:
                    origem_existe= True
                    if v[1] == destino:
                        destino_existe = True
                        break
        if not destino_existe:
                print(f'Não existem voos cadastrados de {origem} para {destino}')
                print('='*40)
                input( "\nPRESIONE ENTER PARA CONTINUAR>>>>")
                os.system('cls')
                return
        if not origem_existe:
                print(f'Não existem voos cadastrados que partem da cidade {origem}')
                print('='*40)
                input( "\nPRESIONE ENTER PARA CONTINUAR>>>>")
                os.system('cls')
                return
        primeiro = True
        for  v in dict_voos.values():
            if v[0]== origem and v[1]== destino:
                if primeiro:
                    menorescala_voo = v[2]
                    primeiro = False
                else:
                    if v[2] < menorescala_voo:
                        menorescala_voo = v[2]
        for k, v in dict_voos.items():
            if v[2]==menorescala_voo and v[0]== origem and v[1]==destino:
                print('='*40)
                print(f"Voo com menor número de escalas da cidade {origem} para cidade {destino}:")
                print(f"Código: {k}")
                print(f"Escalas: {v[2]}")
                print(f"Preço: R${v[3]:.2f}")
                print('='*40)
                input( "\nPRESIONE ENTER PARA CONTINUAR>>>>")
                os.system('cls')

def listagem_passageiros(dict_voos, dict_passageiros):
            print('='*40)
            cod_voo=input('Insira o código do voo: ')
            while cod_voo not in dict_voos.keys():
                print(f'CÓDIGO INVÁLIDO')
                cod_voo=(input(f'\nDigite outro código do voo: '))
            else:
                for k, v in dict_voos.items():
                    if cod_voo == k:
                        print('='*40)
                        print(f'A lista de passageiros do voo de código {cod_voo}: ')
                        if len(dict_voos[cod_voo][5]) == 0:
                            print(f'\nAinda não há passageiros cadastrados nesse voo!')
                            print('='*40)
                            input( "\nPRESIONE ENTER PARA CONTINUAR>>>>")
                            os.system('cls')
                        else:
                            print(f'\nPassageiros:')
                            for cpf in dict_voos[cod_voo][5]:
                                    if cpf in dict_passageiros:
                                        print(f'| {dict_passageiros[cpf][0].title()}', end =' | ')
                            print(f'\nQuantidade de lugares disponíveis: {v[4]}')
                            input( "\nPRESIONE ENTER PARA CONTINUAR>>>>")
                            os.system('cls')
                            
def venda_passagem(dict_voos, dict_passageiros,lista_voosdisponiveis):
        print('='*40)
        print('Insira suas informações>>> ')
        cpf=int(input('Digite seu CPF (sem pontos ou traços): '))
        nome=input('Digite seu nome: ').upper()
        if cpf in dict_passageiros:
            if dict_passageiros[cpf][0] != nome:
                    print(f'CPF JÁ CADASTRADO COM OUTRO NOME!')
                    return
        telefone=int(input('Digite seu telefone (sem traços ou espaços): '))
        print('='*40)    
        print('LISTAS DE VOOS DISPONÍVEIS')
        if len(lista_voosdisponiveis)==0:
            print('Não há voos disponiveis')
            print('='*40)
            input( "\nPRESIONE ENTER PARA CONTINUAR>>>>")
            os.system('cls')
            return
        else:
            for k,v in dict_voos.items():
                if v[4]>0:
                    print('='*40)
                    print(f'{k} - Cidade Origem: {v[0].title()}')
                    print(f'Cidade Destino: {v[1].title()}')
                    print(f'numero de escalas: {v[2]}')
                    print(f'Preço da passagem: {v[3]:.2f}')
                    print(f'Quantidade de lugares disponíveis: {v[4]}')
                    print('='*40)
        voo_escolhido=(input('Digite o número do voo que deseja comprar: '))
        while voo_escolhido not in dict_voos: 
            print(f'VOO INEXISTENTE')
            voo_escolhido=(input('Digite o número do voo que deseja comprar: '))
        else:
            num_passagens=int(input('Digite o numero de passagens que deseja comprar: '))
        if cpf not in dict_passageiros:             
            total_passagens=num_passagens
        else:
            total_passagens= dict_passageiros[cpf][2]+num_passagens
        if voo_escolhido in dict_voos and dict_voos[voo_escolhido][4] >=num_passagens:
            dict_voos[voo_escolhido][4] -= num_passagens
            dict_passageiros[cpf] = [nome, telefone, total_passagens]
            if cpf not in dict_voos[voo_escolhido][5]:
                 dict_voos[voo_escolhido][5].append(cpf)
            print(f'COMPRA REALIZADA!')
            input( "\nPRESIONE ENTER PARA CONTINUAR>>>>")
            os.system('cls')
        else:
            print(f'TENTATIVA DE COMPRAS DE PASSAGENS ACIMA DO LIMITE!!!')
            input( "\nPRESIONE ENTER PARA CONTINUAR>>>>")
            os.system('cls')
        if dict_voos[voo_escolhido][4]==0:
            if voo_escolhido in lista_voosdisponiveis:
                lista_voosdisponiveis.remove(voo_escolhido)
def cancelamento_passagem(dict_voos, dict_passageiros,voos_disponiveis):
        print('='*40)
        codig_voo=input('Digite o código do voo: ')
        while codig_voo not in dict_voos:
            print('CÓDIGO DO VOO INVÁLIDO')
            codig_voo=input('Digite o código do voo: ')
        CPF_cliente=int(input('Digite seu cpf: '))
        while CPF_cliente not in dict_passageiros:
            print('CPF NÃO ENCONTRADO')
            CPF_cliente=int(input('Digite seu cpf: '))
        while CPF_cliente not in dict_voos[codig_voo][5]:   
            print('ESSE CPF NÃO ENCONTRADO NESSE VOO')
            print('='*40)
            input( "\nPRESIONE ENTER PARA CONTINUAR>>>>")
            os.system('cls')
            return
        
        confirmacao=input(f'Deseja realmente cancelar sua passagem? [S/N]: ').upper()
        if confirmacao != 'S':
            print('Cancelamento anulado!')
            input( "\nPRESIONE ENTER PARA CONTINUAR>>>>")
            os.system('cls')
            return
        else:
            if dict_voos[codig_voo][4]==0:
                 voos_disponiveis.append(codig_voo)
            if CPF_cliente in dict_voos[codig_voo][5]:
                dict_voos[codig_voo][4] +=1
                
                if dict_passageiros[CPF_cliente][2]!=1:
                    dict_passageiros[CPF_cliente][2]-=1
                else:
                    dict_voos[codig_voo][5].remove(CPF_cliente)
                    del dict_passageiros [CPF_cliente]
        print(f'Passagem cancelada com sucesso!')
        print('='*40)
        input( "\nPRESIONE ENTER PARA CONTINUAR>>>>")
        os.system('cls')
#programa principal
voos={}
passageiros={}
voos_disponiveis=[]
telainicial()
while True:
    opcao=escolha()
    match opcao:
        case 1:
           voos, voos_disponiveis= cadastro_voo(voos, voos_disponiveis)
        case 2:
            while True:
                escolha_consulta=menu_consulta()
                match escolha_consulta:
                    case 1:
                        consulta_numerovoo(voos)
    
                    case 2:
                        consulta_origem(voos)

                    case 3:
                        consulta_destino(voos)

                    case 4:
                        print(f'\nSAINDO...')
                        break
                    
                    case _:
                        print('\nOPÇÃO INVÁLIDA')
        case 3:
            menor_escala(voos)
        case 4:
            listagem_passageiros(voos, passageiros)
        case 5:
            venda_passagem(voos, passageiros, voos_disponiveis)                        
        case 6:
            cancelamento_passagem(voos,passageiros,voos_disponiveis)
        case 7:
            os.system('cls')
            print('='*40)
            print('Obrigada por usar nosso sistema!')
            print('Até a próxima!')
            print('Saindo...')
            print('='*40)
            break
        case _:
            print('Opção Inválida!')