from sklearn import neural_network, datasets, metrics
import numpy as np

# -- Carrega a base --
db = datasets.load_digits()

# -- Atributos --
x = db.data

# -- Classes --
y = db.target

np.random.seed(0)

n_samples = len(x)
particao = 0.75

order = np.random.permutation(n_samples)

x = x[order]
y = y[order]

# -- Separa base de treino
x_treino = x[:int(n_samples * particao)]
y_treino = y[:int(n_samples * particao)]

# -- Separa base de teste
x_teste = x[int(n_samples * particao):]
y_teste = y[int(n_samples * particao):]

clf = neural_network.MLPClassifier(max_iter=2000, hidden_layer_sizes=(10,5,))

clf.fit(x_treino, y_treino)

predicao = clf.predict(x_teste)

matriz = metrics.confusion_matrix(y_teste, predicao)

print(clf.score(x_teste, y_teste))

for linha in matriz:
    print(linha)

# #memoria dos pesos do algoritmo
# print(clf.coefs_)
#
# #memoria do baias
# print(clf.intercepts_)
#
# #memoria dos erros
# print(clf.loss_)