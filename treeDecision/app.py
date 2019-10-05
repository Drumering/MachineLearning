from sklearn import tree, datasets, metrics
import numpy as np

database = datasets.load_iris()

X = database.data
Y = database.target

np.random.seed(0)

n_samples = len(X)

sep = 0.75

order = np.random.permutation(n_samples)

X = X[order]
Y = Y[order]

X_test = X[int(sep*n_samples):]
Y_test = Y[int(sep*n_samples):]

X_train = X[:int(sep*n_samples)]
Y_train = Y[:int(sep*n_samples)]

clf = tree.DecisionTreeClassifier()

clf.fit(X_train,Y_train)

predict = clf.predict(X_test)

taxa = clf.score(X_test,Y_test)

print(taxa)

matrix = metrics.confusion_matrix(Y_test, predict)

for line in matrix:
    print(line)

atributos = ['Comprimento da Sepala', 'Largura da Sepala', 'Comprimento da Petala', 'Largura da Petala']

classes = ['Setosa', 'Versicolor', 'Virginica']

tree.export_graphviz(clf,"grafo.dot", feature_names=atributos, class_names=classes)