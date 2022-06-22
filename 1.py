num_alunos10 = 10
nome = []
nota = []
t1 = media = n_e = nota0 = 0


for i in range(num_alunos10):
    t1 += 1
    media = nota0 = 0


    nome1 = str(input(f'Digite o nome do {t1}º aluno: '))
    nome_vari = nome1


    for e in range(0, 4, 1):
        n_e += 1
        nota1 = float(input(f'Digite a {n_e}º nota do aluno(a) {nome_vari}: '))


        notat = nota0 + nota1
    media = nota0 / 4


    if media >= 7:
        nome.append(nome1)
        nota.append(media)


for a in range(len(nome)):
    print(f"{nome[a], nota[a]}".replace("'", '').replace("'", '')
          .replace("[", '').replace("]", '').replace("(", '')
          .replace(")", '').replace(",", ':').replace(",", ':'))