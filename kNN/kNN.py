from leitor import leitor_matriz

teste = leitor_matriz("teste.data")
treino = leitor_matriz("treino.data")

def manhattan(treino,teste):
    c1 = 0
    c2 = 0
    c3 = 0
    somatorio = 0
    vetor = []
    for i in range(0,len(teste)):
        for j in range(0,len(treino)):
            for k in range(0,4):
                somatorio =+ abs(teste[i][k] - treino[j][k])
            vetor.append(somatorio)
        pass
    return vetor

distManhattan = manhattan(treino,teste)
print(distManhattan[0])