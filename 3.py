idade = []
idade_inv = []
altura = []
altura_inv = []


n = 0
i = 0


for i in range(0, 5, 1):
    n += 1
    idade += input(f"Digite a idade da {n}º pessoa: ")
    altura += input(f"Digite a altura da {n} pessoa: ")


while i >= 0:
    idade_inv += idade[i]
    altura_inv += altura[i]
    i -= 1


print(f'Idade em ordem inversa: {idade_inv}'.replace(",", '').replace("[", '').replace("'", ''))
print(f'Altura em ordem inversa: {altura_inv}'.replace(",", '').replace("[", '').replace("'", ''))