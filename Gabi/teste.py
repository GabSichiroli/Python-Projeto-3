pes={}
i=0
while i<3:
    nome=input("Digite um nome: ")
    nome=nome.upper()
    if nome in pes.keys():
        print(f"\n\t\t=> NOME JÁ EXISTENTE<==\n")
else:
    age=int(input(" Idade: "))
    cidade=input("Cidade: ")
    cidade=cidade.upper()
    pes[nome]=[age,cidade]
    i=i+1
proc=input("Digite o nome a ser procurado: ")
if proc.upper() in pes.keys():
    print(f"\n\t{proc.upper()} possui {pes[proc.upper()][0]} anos")
else:
    print(f"\n\t{proc.upper()} não consta no banco de dados")
#maior idade
    maior=0
for dados in pes.values():
    if maior< dados[0]:
        maior=dados[0]
    print(f"\n\tA maior idade é {maior}")
for p,dados in pes.items():
    print(f"\n\t{p} possui {dados[0]} anos e mora em {dados[1]}")
