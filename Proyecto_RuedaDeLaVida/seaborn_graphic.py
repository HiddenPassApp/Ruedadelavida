import seaborn as sns
import matplotlib.pyplot as plt

# Load the Tips dataset
tips = sns.load_dataset("iris")

print(tips.head())

print(tips.describe())

plt.figure(figsize=(12,8))

sns.boxplot(data=tips[['sepal_length', 'sepal_width', 'petal_length', 'petal_width']])
plt.title("Boxplot de la caracteristicas de iris")

tips[['sepal_length', 'sepal_width', 'petal_length', 'petal_width']].hist(bins=15, figsize=(12,10))

sns.pairplot(tips, hue='species')

correlacion_matriz = tips.select_dtypes(include="number").corr()
plt.figure(figsize=(10,8))
sns.heatmap(correlacion_matriz, annot=True, cmap='coolwarm', linewidths=.5)


plt.figure(figsize=(8,6))
sns.boxplot(x='species', y='sepal_length', data=tips)
plt.title("Comparación de la longitud del sepalo por especio")

plt.show()
