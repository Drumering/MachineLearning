from sklearn import svm, neural_network, metrics, datasets
import numpy as np
from sklearn.model_selection import GridSearchCV
import matplotlib.pyplot as plt

db = datasets.load_boston()

x = db.data
y = db.target

np.random.seed(0)

samples = len(x)
division = 0.75

shuffle = np.random.permutation(samples)

x = x[shuffle]
y = y[shuffle]

x_training = x[:int(samples*division)]
y_training = y[:int(samples*division)]

x_test = x[int(samples*division):]
y_test = y[int(samples*division):]

parameters_svr = {'kernel':('linear','poly','sigmoid','rbf'), 'C':[1,2,3]}

svr = svm.SVR(gamma='scale')

clf = GridSearchCV(svr, parameters_svr, n_jobs=5, verbose=3)

clf.fit(x_training, y_training)

print(clf.best_params_)

predict = clf.predict(x_test)

mse = metrics.mean_squared_error(y_test,predict)

r2 = metrics.r2_score(y_test, predict)

print('SVR')
print('MSE:', mse)
print('R2:', r2)

clf1 = neural_network.MLPRegressor(hidden_layer_sizes=(26,), max_iter=1500)
clf1.fit(x_training, y_training)

predict_rede = clf1.predict(x_test)

mse_rede = metrics.mean_squared_error(y_test, predict_rede)
r2_rede = metrics.r2_score(y_test, predict_rede)

print('MLP')
print('MSE:', mse_rede)
print('R2', r2_rede)

diagonal = list(range(int(min(y_test)),int(max(y_test))))

plt.title('Prediction: SVR')
plt.xlabel('Original')
plt.ylabel('Prediction')

plt.scatter(y_test, predict, label='SVR = {}'.format(r2))
plt.scatter(y_test, predict_rede, label='MLP = {}'.format(r2_rede))
plt.plot(diagonal, diagonal, 'r--', label='Objective')
plt.legend(loc='upper left')

plt.show()