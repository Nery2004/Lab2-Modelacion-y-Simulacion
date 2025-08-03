def funcion(x):
    return 2*x**5 + 3*x**4 - 3*x**3 - 10*x**2 - 4*x + 4

def derivada(x):
    return 10*x**4 + 12*x**3 - 9*x**2 - 20*x - 4

def biseccion(a, b, tolerancia=1e-6, max_iter=100):
    if funcion(a) * funcion(b) >= 0:
        print("Error: f(a) y f(b) deben tener signos opuestos.")
        return None

    iteracion = 0
    while (b - a) / 2 > tolerancia and iteracion < max_iter:
        c = (a + b) / 2
        fc = funcion(c)

        print(f"Iteración {iteracion + 1}: a = {a}, b = {b}, c = {c}, f(c) = {fc}")

        if fc == 0:
            return c
        elif funcion(a) * fc < 0:
            b = c
        else:
            a = c
        iteracion += 1

    return (a + b) / 2

def secante(x0, x1, tolerancia=1e-6, max_iter=100):
    iteracion = 0

    while iteracion < max_iter:
        f_x0 = funcion(x0)
        f_x1 = funcion(x1)

        if f_x1 - f_x0 == 0:
            print("Error: División por cero.")
            return None

        x2 = x1 - f_x1 * (x1 - x0) / (f_x1 - f_x0)

        print(f"Iteración {iteracion + 1}: x0 = {x0}, x1 = {x1}, x2 = {x2}, f(x2) = {funcion(x2)}")

        if abs(x2 - x1) < tolerancia:
            return x2

        x0, x1 = x1, x2
        iteracion += 1

    print("No se alcanzó la tolerancia en el número máximo de iteraciones.")
    return x2

def newton_raphson(x0, tolerancia=1e-6, max_iter=100):
    iteracion = 0

    while iteracion < max_iter:
        f_x0 = funcion(x0)
        df_x0 = derivada(x0)

        if df_x0 == 0:
            print("Error: Derivada cero. Método no puede continuar.")
            return None

        x1 = x0 - f_x0 / df_x0

        print(f"Iteración {iteracion + 1}: x0 = {x0}, f(x0) = {f_x0}, f'(x0) = {df_x0}, x1 = {x1}")

        if abs(x1 - x0) < tolerancia:
            return x1

        x0 = x1
        iteracion += 1

    print("No se alcanzó la tolerancia en el número máximo de iteraciones.")
    return x1

# =============================
# Menu principal
# =============================

def menu():
    print("\nMétodos para encontrar raíces")
    print("1. Método de Bisección")
    print("2. Método de la Secante")
    print("3. Método de Newton-Raphson")
    opcion = input("Elige una opción (1/2/3): ")

    if opcion == "1":
        a = float(input("Ingrese el valor de a: "))
        b = float(input("Ingrese el valor de b: "))
        raiz = biseccion(a, b)
    elif opcion == "2":
        x0 = float(input("Ingrese el valor de x0: "))
        x1 = float(input("Ingrese el valor de x1: "))
        raiz = secante(x0, x1)
    elif opcion == "3":
        x0 = float(input("Ingrese el valor inicial x0: "))
        raiz = newton_raphson(x0)
    else:
        print("Opción inválida.")
        return

    if raiz is not None:
        print(f"\nRaíz aproximada encontrada: {raiz}")
    else:
        print("\nNo se encontró una raíz con éxito.")

menu()
