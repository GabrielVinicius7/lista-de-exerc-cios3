nome = str(input("Digite seu nome: ").upper().replace(" ", ''))
nome_for = []


for i in range(1, len(nome) + 1, 1):


    nome_for.append(nome[-i])


print(f"Nome em ordem inversa: {nome_for}".replace("['", '').replace("']", '').replace("', '", ''))