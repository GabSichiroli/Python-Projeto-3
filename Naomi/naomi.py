import os
def telainicial():
    print('='*40)
    print("Bem vindo ao Gerenciamento de voos! ")
    input( "PRESIONE ENTER PARA ENTRAR>>>>")
    print('='*40)
    os.system('cls')

def escolha():
    print('='*40)
    print(f'\033[1m{'Menu':^40}\033[0m')
    print('[1]- Cadastrar Voo')
    print('[2]- Consultar Voo')
    print('[3]- Voo com Menor Escala')
    print('[4]- Listar Passageiros do Voo')
    print('[5]- Venda de passagem')
    print('[6]- Cancelamento de Passagem')
    print('[7]- Sair')
    print('='*40)
    opcao_escolhida=int(input('Insira a opção: '))
    return opcao_escolhida

def cadrastro_voo(voos):
    quant=int(input('Insira a quantidade de voos que deseja cadastrar: '))
    for i in range(quant):
        numerovoo=input('Informe o número do voo: ')
        while numerovoo in voos:
            print(f'\033[1;31mVOO JÁ EXISTENTE!\033[0m')
            numerovoo=input('Informe outro número de voo: ')

        cidadeorigem=str(input(f'Insira a cidade origem do voo: ')).upper()
        while cidadeorigem.isdigit() or cidadeorigem==' ':
            print(f'\033[1;31mCidade Inválida\033[0m')
            cidadeorigem=str(input(f'Insira novamente a cidade origem do voo: ')).upper()

        cidadedestino=str(input(f'Insira a cidade destino do voo: ')).upper()
        while cidadedestino.isdigit() or cidadedestino==' ':
            print(f'\033[1;31m[Cidade Inválida\033[1;31m')
            cidadeorigem=str(input(f'Insira novamente a cidade origem do voo: ')).upper()

        numescalas=int(input('Insira o número de escalas do voo: '))
        preco=float(input('Insira o preço da passagem do voo: '))
        quant_lugaresdisp=int(input('Informe quantos lugares a disponíveis nesse voo: '))

        voos[numerovoo]=[cidadeorigem,cidadedestino, numescalas,preco, quant_lugaresdisp, []]
        print(voos) #testedainsercao
        print(F'\033[1;32mVOO CADASTRADO COM SUCESSO!\033[0m')
        return voos
    
def menu_consulta():
    print('Como deseja consultar o voo? ')
    print('[1]- Código do Voo')
    print('[2]- Cidade de Origem')
    print('[3]- Cidade de destino')
    print('[4]- Sair')
    escolha_consulta=int(input('Insira a opção: '))
    return escolha_consulta

def consulta_numerovoo(voos):
    codigo=input('Digite o código do voo: ')
    while codigo not in voos:
            print(f'\033[1;31mCódigo NãO ENCONTRADO\033[0m')
            codigo=(input(f'\nDigite outro código do voo: '))
    
    print('-'*40)
    print(f'Cidade origem: {voos[codigo][0]}')
    print(f'Cidade destino: {voos[codigo][1]}')
    print(f'Número de Escalas: {voos[codigo][2]}')
    print(f'Preço da Passagem: {voos[codigo][3]}')
    print(f'A quantidade de lugares disponíveis do voo é {voos[codigo][4]}')
    print('-'*40)

def consulta_origem(voos):
    busca_origem=str(input('Insira a cidade origem do voo: ')).upper()
    for v in voos.values():
        while v[0] != busca_origem.upper():
            print(f'\033[1;31mNão existem voos cadastrados para a cidade {busca_origem}\033[0m')
            busca_origem=str(input('Insira novamente a cidade origem do voo: ')).upper()

    for k,v in voos.items():
        if v[0] == busca_origem.upper():
            print('='*40)
            print(f'Código do voo: {k}')
            print(f'Cidade Destino: {v[1].title()}')
            print(f'Preços de Passagem para esse voo: R${v[3]}') 
            print('='*40)

def consulta_destino(voos):
    busca_destino=str(input('Insira a cidade destino do voo: ')).upper()
    for v in voos.values():
        while v[1]!=busca_destino:
            print(f'\033[1;31mNão existem voos cadastrados que partem da cidade {busca_destino}\033[0m')
            busca_destino=str(input('Insira novamente a cidade destino do voo: ')).upper()
    for k, v in voos.items():
        if v[1] == busca_destino:
            print('='*40)
            print(f'Código do voo: {k}')
            print(f'Cidade Origem: {v[0].title()}')
            print(f'Preços de Passagem para esse voo: R${v[3]}') 
            print('='*40)

def menor_escala(voos):
        origem = input("Digite a cidade de origem: ").upper()
        destino = input("Digite a cidade de destino: ").upper()
        origem_existe= False
        for v in voos.values():
                if v[0].upper()==origem:
                    origem_existe= True
                    break
                if not origem_existe:
                    print(f'\033[1;31mNão existem voos cadastrados que partem da cidade {origem}\033[0m')
                return
        destino_existe = False
        for v in voos.values():
            if v[0].upper() == origem and v[1].upper() == destino:
                destino_existe = True
                break
        if not destino_existe:
            print(f'\033[1;31mNão existem voos cadastrados de {origem} para {destino}\033[0m')
            return
        primeiro = True
        for  v in voos.values():
            if v[0].upper( )== origem and v[1].upper() == destino:
                if primeiro:
                    menor_escalas = v[2]
                    primeiro = False
                else:
                    if v[2] < menor_escalas:
                        menor_escalas = v[2]

        for k, v in voos.items():
            if v[2]==menor_escalas:
                print('='*40)
                print(f"\nVoo com menor número de escalas da cidade {origem} para cidade {destino}:")
                print(f"Código: {k}")
                print(f"Escalas: {v[2]}")
                print(f"Preço: R${v[3]}")
                print('='*40)
                        
def listagem_passageiros(voos, passageiros):
            print('='*40)
            cod_voo=input('Insira o código do voo: ')
            for k in voos.keys():
                if cod_voo == k:
                    print(f'A lista de passageiros do voo de código {cod_voo}: ')
                    for k, v in voos.items():
                        for nome in passageiros.values():
                            if k == cod_voo:
                                print('Passageiros:')
                                print(f'| {nome[0]}', end =' | ')
                                print(f'\nQuantidade de lugares disponíveis: {v[4]}')
                else:
                    print(f'CÓDIGO INVÁLIDO')

def venda_passagem(voos, passageiros):
        print('='*40)
        print('Insira suas informações>>> ')
        cpf=int(input('Digite seu CPF (sem pontos ou traços): '))
        nome=input('Digite seu nome: ').upper()
        for k, v in passageiros.items():
            if passageiros[k][v][0] != nome:
                print(f'\033[1;31mCPF JÁ CADASTRADO COM OUTRO NOME!\033[0m')
                return
        telefone=int(input('Digite seu telefone (sem traços ou espaços): '))
        print('='*40)    

        print('LISTAS DE VOOS DISPONÍVEIS')
        for k,v in voos.items():
            if v[4]>0:
                print('='*40)
                print(f'{k} - Cidade Origem: {v[0].title()}')
                print(f'Cidade Destino: {v[1].title()}')
                print(f'numero de escalas: {v[2]}')
                print(f'Preço da passagem: {v[3]}')
                print(f'Quantidade de lugares disponíveis: {v[4]}')
                print('='*40)
            else:
                print(f'\nNÃO HÁ VOOS DISPONÍVEIS')
                return
        voo_escolhido=(input('Digite o número do voo que deseja comprar: '))
        if voo_escolhido not in voos: 
            print(f'\033[1;31mVOO INEXISTENTE\033[0m')
            return
        
        num_passagens=int(input('Digite o numero de passagens que deseja comprar: '))

        if cpf not in passageiros:
            total_passagens=num_passagens
        else:
            total_passagens+=num_passagens

        if voo_escolhido in voos and voos[voo_escolhido][4] >=num_passagens:
            voos[voo_escolhido][4] -= num_passagens
            passageiros[cpf] = [nome, telefone, total_passagens]
            voos[voo_escolhido][5].append(cpf)
            print(f'\033[1;34mCOMPRA REALIZADA!\033[0m')
        else:
            print(f'\033[1;31m QUANTIDADE DE PASSAGENS ACIMA DO LIMITE \033[0m')
        
        print(passageiros)#teste
        print(voos)

def cancelamento_passagem(voos, passageiros):
        print('='*40)
        codig_voo=input('Digite o código do voo: ')
        while codig_voo not in voos:
            print(f'\033[1;31mCÓDIGO DO VOO INVÁLIDO\033[0m')
            return
        else:
            CPF_cliente=int(input('Digite seu cpf: '))
            while CPF_cliente not in passageiros:
                print(f'\033[1;31mCPF NÃO ENCONTRADO\033[0m')
                return

            if CPF_cliente in voos[codig_voo][5]:
                del passageiros [CPF_cliente]
                voos[codig_voo][4] +=1
                voos[codig_voo][5].remove(CPF_cliente)
        print(voos)
        print(passageiros)
        print(f'\033[1;32mPassagem cancelada com sucesso!\033[0m')

voos={}
passageiros={}
telainicial()
while True:
    opcao=escolha()

    match opcao:
        case 1:
            cadastro=cadrastro_voo(voos)
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
            venda_passagem(voos, passageiros)                        
        case 6:

            cancelamento_passagem(voos,passageiros)

        case 7:
            print('='*40)
            print('Obrigada por usar nosso sistema!')
            print('Até a próxima!')
            print('Saindo...')
            print('='*40)
            break

        case _:
            print('Opção Inválida')