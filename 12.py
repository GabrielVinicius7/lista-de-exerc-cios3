numero = int(input("digite um numero: "))
numero_for = []


for i in range(numero):


    numero_for.append(i + 1)


    print(f'{numero_for}'.replace("[", '').replace("]", '').replace(",", ' '))
def calcula_soma(termo_n1, termo_n2, termo_n3):
    soma = termo_n1 + termo_n2 + termo_n3
    return soma



s = calcula_soma(5, 5, 5)


print(s)