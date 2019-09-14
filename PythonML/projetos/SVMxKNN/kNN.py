print(__doc__)

from sklearn import datasets, neighbors
import time

start = time.time()

digits = datasets.load_digits()
X_digits = digits.data / digits.data.max()
y_digits = digits.target

n_samples = len(X_digits)

X_train = X_digits[:int(.9 * n_samples)]
y_train = y_digits[:int(.9 * n_samples)]
X_test = X_digits[int(.9 * n_samples):]
y_test = y_digits[int(.9 * n_samples):]

knn = neighbors.KNeighborsClassifier(n_neighbors=3,p=1,algorithm='brute')

print('KNN score: %f' % knn.fit(X_train, y_train).score(X_test, y_test))

end = time.time()

print('\nThe algorithm kNN has fineshed in:',end - start)