a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
soma = 0


for i in range(len(a)):
    if i <= 0:
        soma = a[i]**2
    elif i > 0:
        soma += a[i]**2


print(f'A soma dos quadrados dos valores da lista são: {soma}')