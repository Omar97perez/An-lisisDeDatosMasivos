#-*- coding: utf-8-*-
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
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

class Algorithm:
    def __init__(self, X,Y,pedirParametros):
      self.X = X
      self.Y = Y
      self.pedirParametros = pedirParametros

class BR(Algorithm):
  def grafica(self):
    validation_size = 0.22
    seed = 123
    X_train, X_validation, Y_train, Y_validation = model_selection.train_test_split(self.X, self.Y, test_size=validation_size, random_state=seed)
    model = linear_model.BayesianRidge()
    kfold = model_selection.KFold(n_splits=10, random_state=seed, shuffle=True)
    cv_results = model_selection.cross_val_score(model, X_train, Y_train, cv=kfold)
    msg = "%s (%f)" % ('Clasificador Bayesiano', cv_results.mean())

    model.fit(X_train, Y_train)
    predictions = model.predict(X_validation)

    fig, ax = plt.subplots()
    fig.suptitle( msg)
    ax.scatter(Y_validation, predictions, edgecolors=(0, 0, 0))
    ax.plot([Y_validation.min(), Y_validation.max()], [Y_validation.min(), Y_validation.max()], 'k--', lw=2)
    ax.set_xlabel('Medido')
    ax.set_ylabel('Predecido')
    plt.show()

    if(self.pedirParametros == 1):
        fig = plt.figure()
        fig.suptitle('Diagrama de Cajas y Bigotes para BR')
        ax = fig.add_subplot(111)
        plt.boxplot(cv_results)
        ax.set_xticklabels('BR')
        plt.show()
