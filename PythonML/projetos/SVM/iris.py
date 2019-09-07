import numpy as np
from sklearn import svm, datasets, metrics

#iris = datasets.load_iris()

iris = datasets.load_breast_cancer()

X = iris.data
Y = iris.target

np.random.seed(0)

n_amostras = len(X)

ordem = np.random.permutation(n_amostras)

porcentagem = 0.7

X = X[ordem]
Y = Y[ordem]

X_treino = X[:int(porcentagem * n_amostras)]
Y_treino = Y[:int(porcentagem * n_amostras)]

X_teste = X[int(porcentagem*n_amostras):]
Y_teste = Y[int(porcentagem*n_amostras):]

clf = svm.SVC(gamma='scale')

clf.fit(X_treino, Y_treino)

print(clf.support_vectors_)
print(clf.n_support_)

predicao = clf.predict(X_teste)

print(predicao)

taxa_acerto = clf.score(X_teste, Y_teste)
print(taxa_acerto)

matriz = metrics.confusion_matrix(Y_teste,predicao)

for item in matriz:
    print(item)