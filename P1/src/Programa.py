#-*- coding: utf-8-*-
import matplotlib.pyplot as plt
import pandas as pd
import sys
import Strategy as st

# Pedimos los parámetros que nos van a hacer falta
elementoX = input('Indique el valor del eje X\n > ')
elementoY = input('Indique el valor del eje Y\n > ')
tipoRepresentacion = input('Indique que tipo de representación desea hacer:\n\t 1. Suma \n\t 2. Máximo \n\t 3. Mínimo\n > ')
tipoGrafica = input('Indique que gráfica desea ver:\n\t 1. Gráfica de Líneas.\n\t 2. Gráfica de Barras.\n\t 3. Gráfica de puntos.\n\t 4. Resumen.\n > ')

#Cargamos los datos de un fichero csv
file = './Data/' + sys.argv[1] 
df = pd.read_csv(file)

# Agrupamos los valores por una columna especifica (pasada por linea de comandos)
if tipoRepresentacion == 1:
    df = df.groupby(df.columns[elementoX], as_index=False).sum()
elif tipoRepresentacion == 2:
    df = df.groupby(df.columns[elementoX], as_index=False).max()
else:
    df = df.groupby(df.columns[elementoX], as_index=False).min()

array = df.values
elementoX = 0

# Cogemos las columnas necesarias para las gráficas (pasadas por parámetro)
X = (array[:,elementoX])
Y = (array[:,elementoY])

# Reprenetamos los valores
if tipoGrafica == 1:
    graficaFinal= st.Lineas(X,Y)
    graficaFinal.grafica()
elif tipoGrafica == 2:
    graficaFinal= st.Barras(X,Y)
    graficaFinal.grafica()
elif tipoGrafica == 3:
    graficaFinal= st.Puntos(X,Y)
    graficaFinal.grafica()
else:
    graficaFinal= st.Resumen(X,Y)
    graficaFinal.grafica()