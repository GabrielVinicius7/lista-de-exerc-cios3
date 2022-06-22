def caixa_elegante(linha, coluna):
    resp = False


    while not resp:
        if linha > 20 or linha < 1:
            linha = 20
        if coluna > 20 or coluna < 1:
            coluna = 20
        resp = True


    print('+-' + "-" * linha + '-+')
    for i in range(coluna):
        print("| " + " " * linha + " |")
    print('+-' + "-" * linha + '-+')



print(caixa_elegante(int(input("Digite a largura de sua caixa: ")), int(input('Digite a altura de sua caixa: '))))
print()