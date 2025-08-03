def funcion(x):
    return x**3 - 2*x + 2

def derivada(x):
    return 3*x**2 - 2

def newton_raphson(x0, tolerancia=1e-7, max_iter=100):
    iteracion = 0
    while iteracion < max_iter:
        f_x0 = funcion(x0)
        df_x0 = derivada(x0)
        if df_x0 == 0:
            print("Error en Newton-Raphson: derivada cero.")
            return None, iteracion

        x1 = x0 - f_x0 / df_x0
        print(f"Iteración {iteracion}: x = {x1:.10f}")
        if abs(x1 - x0) < tolerancia:
            return x1, iteracion + 1

        x0 = x1
        iteracion += 1

    return x1, iteracion

raiz, iteraciones = newton_raphson(0)
print(f"\nRaíz: {raiz}, Iteraciones: {iteraciones}")
