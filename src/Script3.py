import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-5, 5, 100)

def funcion_lineal(x):
    return x

y = funcion_lineal(x)

plt.plot(x, y)
plt.title('Gráfica de la función lineal $f(x) = x$')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.show()
