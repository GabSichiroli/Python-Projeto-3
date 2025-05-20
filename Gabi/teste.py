pes = {}
i = 0

while i < 3:
    nome = input("Digite um nome: ").upper()

    if nome in pes:
        print("\n\t\t=> NOME JÁ EXISTENTE <==\n")
    else:
        idade = int(input("Idade: "))
        cidade = input("Cidade: ").upper()
        pes[nome] = [idade, cidade]
        i += 1

proc = input("Digite o nome a ser procurado: ").upper()
if proc in pes:
    print(f"\n\t{proc} possui {pes[proc][0]} anos")
else:
    print(f"\n\t{proc} não consta no banco de dados")

# Maior idade
maior = 0
for dados in pes.values():
    if dados[0] > maior:
        maior = dados[0]

print(f"\n\tA maior idade é {maior}")

# Exibir todos os registros
for nome, dados in pes.items():
    print(f"\n\t{nome} possui {dados[0]} anos e mora em {dados[1]}")
