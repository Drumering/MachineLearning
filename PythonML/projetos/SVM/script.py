import numpy as np
from sklearn import svm

x = np.array([[-1,-1],[-2,-1],[1,1],[2,1]])
y = np.array([1,1,2,2])

clf = svm.SVC(gamma='auto')

clf.fit(x,y)

print(clf.support_vectors_)
print(clf.n_support_)

V1 = [-2,-2]
V2 = [2,2]

V = [V1,V2]

print(clf.predict(V))