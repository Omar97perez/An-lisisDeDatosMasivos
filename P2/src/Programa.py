#-*- coding: utf-8-*-
import matplotlib.pyplot as plt
import pandas as pd
import sys
import StrategyGraph as st
import StrategyFile as sf
import string 
import os
import sys


pedirParametros = int(sys.argv[2]) 

if(pedirParametros == 1):
    # Pedimos los parámetros que nos van a hacer falta
    elementoX = input('Indique el valor del eje X\n > ')
    elementoY = input('Indique el valor del eje Y\n > ')
    elementoRepresentar = input('Indique los valores del eje X a representar separados por comas. Si desea todos escriba "Todos" o "T". \n > ')
    tipoRepresentacion = input('Indique que tipo de representación desea hacer:\n\t 1. Suma. \n\t 2. Máximo. \n\t 3. Mínimo. \n\t 4. Ninguno. \n  > ')
    tipoGrafica = input('Indique que gráfica desea ver:\n\t 1. Gráfica de Líneas.\n\t 2. Gráfica de Barras.\n\t 3. Gráfica de puntos.\n\t 4. Gráfico Circular.\n\t 5. Gráfico de Escaleras.\n\t 6. Gráfico de Dispersión. \n\t 7. Resumen.\n > ')
    nombreFichero = ""
else:
    # Pedimos los parámetros que nos van a hacer falta
    elementoX = int(sys.argv[3]) 
    elementoY = int(sys.argv[4]) 
    tipoRepresentacion = int(sys.argv[5]) 
    tipoGrafica = int(sys.argv[6]) 
    nombreFichero = sys.argv[7]

if(elementoRepresentar != "Todos" and elementoRepresentar != "T"):
    elementosEjeX = elementoRepresentar.split(",")

print(elementosEjeX)

#Cargamos los datos de un fichero csv
file = sys.argv[1] 
fichero = os.path.splitext(file)
fichero = fichero[0] + ".csv"

if file.endswith('.csv'):
    fileSelected = sf.Csv(file, fichero)
    df = fileSelected.collect()
elif file.endswith('.json'):
    fileSelected= sf.Json(file, fichero)
    df = fileSelected.collect()
elif file.endswith('.xlsx'):
    fileSelected= sf.Xlsx(file, fichero)
    df = fileSelected.collect()
else:
    print("Formato no soportado")
    sys.exit()

nombreElementoX = df.columns[elementoX]
nombreElementoY = df.columns[elementoY]


# Agrupamos los valores por una columna especifica (pasada por linea de comandos)
if tipoRepresentacion == 1:
    df = df.groupby(nombreElementoX, as_index=False).sum()
elif tipoRepresentacion == 2:
    df = df.groupby(nombreElementoX, as_index=False).max()
elif tipoRepresentacion == 3:
    df = df.groupby(nombreElementoX, as_index=False).min()

# Cogemos las columnas necesarias para las gráficas (pasadas por parámetro)
X = df.loc[:,nombreElementoX]
Y = df.loc[:,nombreElementoY]

# Reprenetamos los valores
if tipoGrafica == 1:
    graficaFinal= st.Lineas(X,Y,nombreElementoX,nombreElementoY,nombreFichero)
    graficaFinal.grafica()
elif tipoGrafica == 2:
    graficaFinal= st.Barras(X,Y,nombreElementoX,nombreElementoY,nombreFichero)
    graficaFinal.grafica()
elif tipoGrafica == 3:
    graficaFinal= st.Puntos(X,Y,nombreElementoX,nombreElementoY,nombreFichero)
    graficaFinal.grafica()
elif tipoGrafica == 4:
    graficaFinal= st.Circular(X,Y,nombreElementoX,nombreElementoY,nombreFichero)
    graficaFinal.grafica()
elif tipoGrafica == 5:
    graficaFinal= st.Escalera(X,Y,nombreElementoX,nombreElementoY,nombreFichero)
    graficaFinal.grafica()
elif tipoGrafica == 6:
    graficaFinal= st.DiagramaDispersion(X,Y,nombreElementoX,nombreElementoY,nombreFichero)
    graficaFinal.grafica()
else:
    graficaFinal= st.Resumen(X,Y,nombreElementoX,nombreElementoY,nombreFichero)
    graficaFinal.grafica()