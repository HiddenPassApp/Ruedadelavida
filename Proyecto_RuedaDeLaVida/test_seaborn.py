import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Cargar el dataset iris
iris = sns.load_dataset("iris")

# Histograma del largo de los pétalos
sns.histplot(data=iris, x="petal_length")

# Mostrar todo el dataframe sin recortes
pd.set_option("display.max_rows", None)  # Muestra todas las filas
pd.set_option("display.max_columns", None)  # Muestra todas las columnas

print(iris)

print(iris.head())
print(iris.describe())

plt.title("Distribución del largo del pétalo")
plt.xlabel("Largo del pétalo (cm)")
plt.ylabel("Frecuencia")
plt.show()
