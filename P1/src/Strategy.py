import matplotlib.pyplot as plt

class Estrategia:
    def __init__(self,X, Y):
        self.X = X
        self.Y = Y

class GraficaLineas(Estrategia):
  def grafica(self):
    fig = plt.figure()
    fig.suptitle('Grafico de lineas')
    plt.plot(self.X, self.Y)
    plt.show()

class DiagramaBarras(Estrategia):
  def grafica(self):
    plt.suptitle('Diagrama de Barras')
    plt.plot(131)
    plt.bar(self.X, self.Y)
    plt.show()

class GraficaPuntos(Estrategia):
  def grafica(self):
    plt.suptitle('Grafico de Puntos')
    plt.scatter(self.X, self.Y)
    plt.show()

class Resumen(Estrategia):
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