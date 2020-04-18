#-*- coding: utf-8-*-
import matplotlib.pyplot as plt
import numpy as np

class Grafica:
    def __init__(self,X, Y, nombreElementoX, nombreElementoY, nombreFichero):
        self.X = X
        self.Y = Y
        self.nombreElementoX = nombreElementoX
        self.nombreElementoY = nombreElementoY
        self.nombreFichero = nombreFichero

class Lineas(Grafica):
  def grafica(self):
    fig = plt.figure()
    fig.suptitle('Grafico de lineas')
    plt.plot(self.X, self.Y)
    plt.xlabel(self.nombreElementoX)
    plt.ylabel(self.nombreElementoY)
    if self.nombreFichero:
      plt.savefig(self.nombreFichero)
    else:
      plt.show()

class Barras(Grafica):
  def grafica(self):
    plt.suptitle('Diagrama de Barras')
    plt.plot(131)
    plt.bar(self.X, self.Y)
    plt.xlabel(self.nombreElementoX)
    plt.ylabel(self.nombreElementoY)
    if self.nombreFichero:
      plt.savefig(self.nombreFichero)
    else:
      plt.show()

class Puntos(Grafica):
  def grafica(self):
    plt.suptitle('Grafico de Puntos')
    plt.scatter(self.X, self.Y)
    plt.xlabel(self.nombreElementoX)
    plt.ylabel(self.nombreElementoY)
    if self.nombreFichero:
      plt.savefig(self.nombreFichero)
    else:
      plt.show()

class Circular(Grafica):
  def grafica(self):
    plt.pie(self.Y, labels=self.X, autopct='%1.1f%%', shadow=True, startangle=90)
    plt.suptitle('Grafico Circular')
    plt.xlabel(self.nombreElementoX)
    plt.ylabel(self.nombreElementoY)
    if self.nombreFichero:
      plt.savefig(self.nombreFichero)
    else:
      plt.show()

class Escalera(Grafica):
  def grafica(self):
    plt.step(self.X, self.Y)
    plt.suptitle('Grafico de Escaleras')
    plt.xlabel(self.nombreElementoX)
    plt.ylabel(self.nombreElementoY)
    if self.nombreFichero:
      plt.savefig(self.nombreFichero)
    else:
      plt.show()

class DiagramaDispersion(Grafica):
  def grafica(self):
    plt.scatter(self.X, self.Y, s=np.pi*3, alpha=0.5)
    plt.title('Grafico de Dispersion')
    plt.xlabel(self.nombreElementoX)
    plt.ylabel(self.nombreElementoY)
    plt.show()


class Resumen(Grafica):
  def grafica(self):
    plt.figure(figsize=(9, 3))
    plt.subplot(131)
    plt.bar(self.X, self.Y)
    plt.subplot(132)
    plt.scatter(self.X, self.Y)
    plt.subplot(133)
    plt.plot(self.X, self.Y)
    plt.suptitle('Resumen')
    if self.nombreFichero:
      plt.savefig(self.nombreFichero)
    else:
      plt.show()