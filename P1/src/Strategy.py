import matplotlib.pyplot as plt

class Grafica:
    def __init__(self,X, Y):
        self.X = X
        self.Y = Y

class Lineas(Grafica):
  def grafica(self):
    fig = plt.figure()
    fig.suptitle('Grafico de lineas')
    plt.plot(self.X, self.Y)
    plt.show()

class Barras(Grafica):
  def grafica(self):
    plt.suptitle('Diagrama de Barras')
    plt.plot(131)
    plt.bar(self.X, self.Y)
    plt.show()

class Puntos(Grafica):
  def grafica(self):
    plt.suptitle('Grafico de Puntos')
    plt.scatter(self.X, self.Y)
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
    plt.show()