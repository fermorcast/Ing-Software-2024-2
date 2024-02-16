import matplotlib.pyplot as plt
import numpy as np

# Definir el rango de valores de x
x = np.linspace(-5, 5, 100)

# Definir la función
def funcion_lineal(x):
    return x

# Calcular los valores de y
y = funcion_lineal(x)

# Graficar la función
plt.plot(x, y)
plt.title('Gráfica de la función lineal $f(x) = x$')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.show()
