import math

def calcular_distancia_tiro_parabolico(h, p1, p2, n):
    PI = 3.14159
    G = 9.80665

    for i in range(n):
        alfa = float(input("Ingrese el ángulo de disparo (α): "))
        v = float(input("Ingrese la velocidad de lanzamiento (V): "))

        alfa = alfa * PI / 180
        Vox = v * math.cos(alfa)
        Voy = v * math.sin(alfa)

        Ts = Voy / G
        H = (Voy*Voy) / (2 * G) + h
        Vfy = math.sqrt(2 * G * H)
        Td = Vfy / G
        Tt = Ts + Td
        D = Vox * Tt

        if p1 < D < p2:
            print('{:.5f} -> !!!!DUCK!!!'.format(D))
        else:
            print('{:.5f} -> NUCK'.format(D))

def main():
    # Solicitar datos al usuario
    h = float(input("Ingrese la altura de la honda: "))
    p1 = int(input("Ingrese el punto de referencia p1: "))
    p2 = int(input("Ingrese el punto de referencia p2: "))
    n = int(input("Ingrese el número de casos de prueba: "))

    # Realizar cálculos y simulación
    calcular_distancia_tiro_parabolico(h, p1, p2, n)

if __name__ == "__main__":
    main()