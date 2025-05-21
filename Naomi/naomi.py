import os
voos={}
numescalas=[]
while True:
    print('='*30)
    print('Bem vindo ao Gerenciamento de voos!')
    print(f'{'Menu':^20}')
    print('[1]- Cadastrar Voo')
    print('[2]- Consultar Voo')
    print('[3]- Informações do Voo')
    print('[4]- Listar Passageiros do Voo')
    print('[5]- Venda de passagem')
    print('[6]- Cancelamento de Passagem')
    print('[7]- Sair')
    print('='*30)
    opcao=int(input('Insira a opção: '))
    os.system('cls')

    match opcao:
        case 1:
            quant=int(input('Insira a quantidade de voos que deseja cadastrar: '))
            for i in range(quant):
                numerovoo=int(input('Informe o número do voo: '))
                cidadeorigem=str(input(f'Insira a cidade origem do voo: '))
                cidadedestino=str(input(f'Insira a cidade destino do voo: '))
                numescalas=int(input('Insira o número de escalas do voo: '))
                preco=float(input('Insira o preço da passagem do voo: '))
                quant_lugaresdisp=int(input('Informe quantos lugares a disponíveis nesse voo: '))
                os.system('cls')
                voos[numerovoo]=[cidadeorigem,cidadedestino, numescalas,preco, quant_lugaresdisp]
                print(voos) #testedainsercao

        case 2:
            print('Como deseja consultar o voo? ')
            print('[1]- Código do Voo')
            print('[2]- Cidade de Origem')
            print('[3]- Cidade de destino')
            print('[4]- Sair')
            while True:
                escolha=int(input('Insira a opção: '))
                match escolha:
                    case 1:
                        codigo=int(input('Digite o código do voo: '))
                        if codigo in voos:
                            print(f'Cidade origem: {voos[codigo][0]}')
                            print(f'Cidade destino: {voos[codigo][1]}')
                            print(f'Número de Escalas: {voos[codigo][2]}')
                            print(f'Preço da Passagem: {voos[codigo][3]}')
                            print(f'A quantidade de lugares disponíveis do voo é {voos[codigo][4]}')
                        
                    case 2:
                        cidadedeorigem=str(input('Insira a cidade origem do voo: '))
                        
                        for k,v in voos.items():
                            if v[0] == cidadedeorigem:
                                print(f'Código do voo: {k}')
                                print(f'Cidade Destino: {[v[1]]}')
                                print(f'Preços de Passagem para esse voo: {v[3]}') 

                    case 3:
                        cidadededestino=str(input('Insira a cidade destino do voo: '))
                        
                        for k, v in voos.items():
                            if v[1] == cidadededestino:
                                print(f'Código do voo: {k}')
                                print(f'Cidade Origem: {[v[0]]}')
                                print(f'Preços de Passagem para esse voo: {v[3]}') 
                    
                    case 4:
                        print(f'\nSaindo...')
                        break
                    
                    case _:
                        print('Opção Inválida')