import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import export_graphviz
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import pickle

dataset = pd.read_csv("data/decisionTree/data.csv")

# przypisuję do zmiennej wszystkie kolumny tabeli oprócz "wybucha"
X = dataset.drop(["explode"], axis=1)
# przypisuję kolumnę "wybucha"
y = dataset["explode"]
# podział na zbiór uczący i testowy
X_train, X_test, y_train, y_test = train_test_split(X, y)

klasyfikator = DecisionTreeClassifier(criterion="entropy")
#trenowanie drzewa decyzyjnego
klasyfikator.fit(X=X_train, y=y_train)

#wypisanie raportu
predictions = klasyfikator.predict(X_test)
print(classification_report(y_test, predictions))

#zapisanie drzewa decyzyjnego do pliku
pickle.dump(klasyfikator, open('data/decisionTree/decisionTreeExplode.sav', "wb"))

export_graphviz(klasyfikator, out_file='data/decisionTree/treeExplode.dot')