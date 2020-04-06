import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from pandas.plotting import scatter_matrix


elementoX = 1
elementoY = 12

#Cargamos los datos de un fichero csv
file = './TomeCano.csv'
df = pd.read_csv(file)
df = df.groupby(df.columns[elementoX], as_index=False).max()
array = df.values
elementoX = 0


#Imprimimos las 5 primeras filas del fichero
print(df.head(5))

#Cogemos las columnas necesarias X (todas menos la necesaria para estimar) e Y (la columna a estimar)
X = (array[:,elementoX])
Y = (array[:,elementoY])
#Imprimimos el contenido de cada vector
print("X")
print(X)
print("Y")
print(Y)

# Imprimimos por pantalla los resultados de los algoritmos
fig = plt.figure()
fig.suptitle('Gráfico de líneas')
plt.plot(X, Y)
plt.ylabel('some numbers')
plt.show()


# Imprimimos por pantalla los resultados de los algoritmos
plt.suptitle('Gráfico de Barras')
plt.plot(131)
plt.bar(X, Y)
plt.show()

names = ['group_a', 'group_b', 'group_c']
values = [1, 10, 100]

# Imprimimos por pantalla los resultados de los algoritmos
plt.suptitle('Gráfico de Puntos')
plt.scatter(X, Y)
plt.show()

plt.figure(figsize=(9, 3))

plt.subplot(131)
plt.bar(X, Y)
plt.subplot(132)
plt.scatter(X, Y)
plt.subplot(133)
plt.plot(X, Y)
plt.suptitle('Resumen')
plt.show()