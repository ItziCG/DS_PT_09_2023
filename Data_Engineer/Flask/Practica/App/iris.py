#Crear un modelos de ML KNN con los datos de Iris sin gridsearch
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

iris=load_iris()

print(iris.keys())

X = iris.data
y = iris.target

# Dividir los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Crear el modelo k-NN
knn_model = KNeighborsClassifier()

# Entrenar el modelo
knn_model.fit(X_train, y_train)

# Predecir en el conjunto de prueba
y_pred = knn_model.predict(X_test)

# Calcular la precisión del modelo
accuracy = accuracy_score(y_test, y_pred)
print("Precisión del modelo k-NN:", accuracy)