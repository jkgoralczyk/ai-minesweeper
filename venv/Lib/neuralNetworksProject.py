from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report
import numpy as np
import pandas as pd
import itertools
from PIL import Image
from collections import Iterable
import pickle

X = np.zeros(shape=(3000, 22500))
for i in range(5, 16, 5):
    for j in range(1000):
        img = Image.open('data/neuralNetwork/' + str(i) + '/map' + str(j) + '.png')
        X[(int(i / 2) - 3) * 1000 + j] = list(itertools.chain(*np.asarray(img).tolist()))

y = np.zeros(shape=(3000, 1))
for i in range(5, 16, 5):
    for j in range(1000):
        y[(int(i / 2) - 3) * 1000 + j] = i

X_train, X_test, y_train, y_test = train_test_split(X, y)

scaler = StandardScaler()
scaler.fit(X_train)

X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)

mlp = MLPClassifier(hidden_layer_sizes=(2000, 2000), max_iter=1000)
mlp.fit(X_train, y_train.ravel())

predictions = mlp.predict(X_test)
print(classification_report(y_test, predictions))

filename = 'data/neuralNetwork/neuralNetwork3.sav'
pickle.dump(mlp, open(filename, 'wb'))
    

