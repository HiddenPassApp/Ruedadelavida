from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score
from sklearn.svm import SVC
from sklearn.neural_network import MLPClassifier
from sklearn.ensemble import RandomForestClassifier

# Cargar conjunto de datos
data = load_iris()
x = data.data
y = data.target

y = (y == 0).astype(int)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=.3, random_state=42)

# Crear y entrenar el modelo
model = LogisticRegression()
model.fit(x_train, y_train)

y_pred = model.predict(x_test)

print(f"precisión: {accuracy_score(y_test, y_pred)}")





# Árboles

# Dividir en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
# Crear el modelo de árbol de decisión
model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, y_train)
# Realizar predicciones
y_pred = model.predict(X_test)
# Evaluar el modelo
print(f"Precisión: {accuracy_score(y_test, y_pred)}")


# MAQUINAS SVM

# Dividir en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, 
random_state=42)
# Crear el modelo SVM
model = SVC(kernel='linear')
model.fit(X_train, y_train)
# Realizar predicciones
y_pred = model.predict(X_test)
# Evaluar el modelo
print(f"Precisión: {accuracy_score(y_test, y_pred)}")


# K-Vecinos más Cercanos (KNN)

# Dividir en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
# Crear el modelo KNN
model = KNeighborsClassifier(n_neighbors=3)
model.fit(X_train, y_train)
# Realizar predicciones
y_pred = model.predict(X_test)
# Evaluar el modelo
print(f"Precisión: {accuracy_score(y_test, y_pred)}")



# Redes Neuronales Artificiales (ANN)

# Dividir en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, 
random_state=42)
# Crear el modelo de red neuronal (MLP)
model = MLPClassifier(hidden_layer_sizes=(10,), max_iter=1000, 
random_state=42)
model.fit(X_train, y_train)
# Realizar predicciones
y_pred = model.predict(X_test)
# Evaluar el modelo
print(f"Precisión: {accuracy_score(y_test, y_pred)}")


# Bosque aleatorio

# Dividir en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
# Crear el modelo Random Forest
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)
# Realizar predicciones
y_pred = model.predict(X_test)
# Evaluar el modelo
print(f"Precisión: {accuracy_score(y_test, y_pred)}")

