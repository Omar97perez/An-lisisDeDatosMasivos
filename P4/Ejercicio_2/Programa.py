import matplotlib.pyplot as plt
import pandas as pd
import StrategyFile as sf
import StrategyAlgorithm as st
import sys
import string 
import os
import geopandas as gpd
import numpy as np
from sklearn import datasets, linear_model
from sklearn.linear_model import LinearRegression, RANSACRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.neural_network import MLPRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import cross_val_predict, train_test_split
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
from sklearn import model_selection
from pandas.plotting import scatter_matrix


pedirParametros = int(sys.argv[2]) 

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

if(pedirParametros == 1):
    algoritmoSeleccionado = int(input('¿Qué algoritmo quiere ejecutar?: \n\t 1. Clasificación Bayesiana (Aprendizaje supervisado de clasificación). \n\t 2. Aprendizaje supervisado de Regresión. \n\t 3. Aprendizaje no supervisado basado en Clustering. \n  > '))
else:
    algoritmoSeleccionado = int(sys.argv[3]) 

array = df.values
X = (array[:,0:12])
Y = (array[:,12])

# Representamos los valores
if algoritmoSeleccionado == 1:
    graficaFinal = st.BR(X, Y, pedirParametros)
    graficaFinal.grafica()
# elif algoritmoSeleccionado == 2:
#     graficaFinal= st.Barras(X,Y,nombreElementoX,nombreElementoY,nombreFichero)
#     graficaFinal.grafica()
# elif algoritmoSeleccionado == 3:
#     graficaFinal= st.Puntos(X,Y,nombreElementoX,nombreElementoY,nombreFichero)
#     graficaFinal.grafica()
else:
    print("El algoritmo introducido no existe")