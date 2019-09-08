from leitor import leitor_matriz

teste = leitor_matriz("D:/pythonProjects/opet/MachineLearning/kNN/teste.data")
treino = leitor_matriz("D:/pythonProjects/opet/MachineLearning/kNN/treino.data")

def manhattan(treino,teste, K):
    c1 = 0
    c2 = 0
    c3 = 0
    somatorio = 0
    vetor = []
    for i in range(len(teste)):
        for j in range(len(treino)):
            for k in range(0,4):
                somatorio =+ abs(teste[i][k] - treino[j][k])
            vetor.append((somatorio, treino[j][4]))
        vetor.sort()
    for h in range(K):
        if vetor[h][1] == 0:
            c1 += 1
        elif vetor[h][1] == 1:
            c2 += 1
        else:
            c3 += 1
    vetor = []

    if c1 > c2 and c1 > c3:
        print('Setosa: ', c1)
    elif c2 > c1 and c2 > c3:
        print('Versicolor: ', c2)
    else:
        print('Verginica: ', c3)

def euclidiana(treino,teste, K):
    c1 = 0
    c2 = 0
    c3 = 0
    somatorio = 0
    vetor = []
    for i in range(len(teste)):
        for j in range(len(treino)):
            for k in range(0,4):
                somatorio =+ (abs(teste[i][k]**2 - treino[j][k]**2)**0.5)
            vetor.append((somatorio, treino[j][4]))
        vetor.sort()
    for h in range(K):
        if vetor[h][1] == 0:
            c1 += 1
        elif vetor[h][1] == 1:
            c2 += 1
        else:
            c3 += 1
    vetor = []

    if c1 > c2 and c1 > c3:
        print('Setosa: ', c1)
    elif c2 > c1 and c2 > c3:
        print('Versicolor: ', c2)
    else:
        print('Verginica: ', c3)

manhattan(treino,teste, 45)
euclidiana(treino,teste, 45)