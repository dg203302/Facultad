import matplotlib.pyplot as plt
import numpy as np
def f(x):
    return pow((x-3),2)+2# Ejemplo: función seno
x = np.linspace(-10, 10, 100)  # 100 puntos entre 0 y 10
y = f(x)
plt.plot(x, y, label='Funciones')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Gráfico de la función')
plt.legend()
plt.grid(True)
plt.show()
