import numpy as np
from scipy.optimize import approx_fprime
import math

def newton_multidimensional(f, df, x0, max_iter=100, tol=1e-10):
    
    x = np.array(x0, dtype=float)
    aproximaciones = [x.copy()]
    
    print(f"Iteración 0: x = {x}")
    print(f"F(x) = {f(x)}")
    print(f"||F(x)|| = {np.linalg.norm(f(x)):.7f}\n")
    
    for i in range(max_iter):
        # Evaluar la función en el punto actual
        fx = f(x)
        
        # Verificar criterio de convergencia
        if np.linalg.norm(fx) < tol:
            print(f"Convergencia alcanzada en {i} iteraciones")
            break
        
        # Calcular el Jacobiano
        J = df(x)
        
        # Verificar que el Jacobiano no sea singular
        if np.linalg.det(J) == 0:
            print("Jacobiano singular - no se puede continuar")
            break
        
        # Resolver el sistema lineal J * delta_x = -F(x)
        try:
            delta_x = np.linalg.solve(J, -fx)
        except np.linalg.LinAlgError:
            print("Error al resolver el sistema lineal")
            break
        
        # Actualizar x
        x_nuevo = x + delta_x
        
        print(f"Iteración {i+1}:")
        print(f"J(x) = \n{J}")
        print(f"delta_x = {delta_x}")
        print(f"x = {x_nuevo}")
        print(f"F(x) = {f(x_nuevo)}")
        print(f"||F(x)|| = {np.linalg.norm(f(x_nuevo)):.7f}\n")
        
        x = x_nuevo
        aproximaciones.append(x.copy())
        
    else:
        print(f"Máximo número de iteraciones ({max_iter}) alcanzado")
    
    return aproximaciones, x

# Definir el sistema de ecuaciones del problema
def sistema_ecuaciones(vars):
    x, y, z = vars
    
    f1 = 3*x - math.cos(y*z) - 0.5
    f2 = x**2 - 81*(y + 0.1)**2 + math.sin(z) + 1.06
    f3 = math.exp(-x*y) + 20*z + (10*math.pi - 3)/3
    
    return np.array([f1, f2, f3])

def jacobiano_sistema(vars):
    x, y, z = vars
    
    # Derivadas parciales de f1
    df1_dx = 3
    df1_dy = z * math.sin(y*z)
    df1_dz = y * math.sin(y*z)
    
    # Derivadas parciales de f2
    df2_dx = 2*x
    df2_dy = -162*(y + 0.1)
    df2_dz = math.cos(z)
    
    # Derivadas parciales de f3
    df3_dx = -y * math.exp(-x*y)
    df3_dy = -x * math.exp(-x*y)
    df3_dz = 20
    
    J = np.array([
        [df1_dx, df1_dy, df1_dz],
        [df2_dx, df2_dy, df2_dz],
        [df3_dx, df3_dy, df3_dz]
    ])
    
    return J

# Resolver el sistema con punto inicial [0, 0, 0]
print("Sistema de ecuaciones:")
print("3x - cos(yz) - 1/2 = 0")
print("x² - 81(y + 0.1)² + sin(z) + 1.06 = 0")
print("e^(-xy) + 20z + (10π - 3)/3 = 0")
print("\nPunto inicial: [0, 0, 0]")


# Punto inicial
x0 = [0, 0, 0]

# Resolver con tolerancia de 7 cifras decimales
aproximaciones, solucion = newton_multidimensional(
    sistema_ecuaciones, 
    jacobiano_sistema, 
    x0, 
    max_iter=100, 
    tol=1e-7
)

print("RESULTADOS FINALES:")
print(f"Solución encontrada: x* = {solucion}")
print(f"F(x*) = {sistema_ecuaciones(solucion)}")
print(f"||F(x*)|| = {np.linalg.norm(sistema_ecuaciones(solucion)):.10f}")
print(f"Número de iteraciones: {len(aproximaciones) - 1}")

# Mostrar todas las aproximaciones
print("\nTodas las aproximaciones:")
for i, aprox in enumerate(aproximaciones):
    print(f"x_{i} = {aprox}")