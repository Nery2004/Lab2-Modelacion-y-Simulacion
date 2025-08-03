import matplotlib.pyplot as plt
import numpy as np


def funcion(x):
    return x**3 - 2*x + 2

def derivada(x):
    return 3*x**2 - 2


x_vals = np.linspace(-3, 2, 400)
y_vals = funcion(x_vals)

plt.plot(x_vals, y_vals, label='f(x) = x³ - 2x + 2')
plt.axhline(0, color='gray', linestyle='--')
plt.axvline(0, color='gray', linestyle='--')
plt.title("Gráfica de la función")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid(True)
plt.legend()
plt.show()

# 3. Aplicar Newton-Raphson
def newton_raphson(x0, tolerancia=1e-7, max_iter=100):
    iteracion = 0
    while iteracion < max_iter:
        f_x0 = funcion(x0)
        df_x0 = derivada(x0)

        if df_x0 == 0:
            print("Derivada cero. Método falló.")
            return None, iteracion

        x1 = x0 - f_x0 / df_x0
        print(f"Iteración {iteracion}: x = {x1:.10f}")

        if abs(x1 - x0) < tolerancia:
            return x1, iteracion + 1

        x0 = x1
        iteracion += 1

    print("No se alcanzó la tolerancia requerida.")
    return x1, iteracion

#Llamar al método con x0 = -2 (estrategia adecuada)
raiz, iteraciones = newton_raphson(-2)
print(f"\nRaíz aproximada: {raiz:.10f} encontrada en {iteraciones} iteraciones.")
