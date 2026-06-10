import math


def conteo_total(tamano_alfabeto, longitud):
    """
    Calcula el número total de claves posibles aplicando
    el principio fundamental del conteo.
    """
    if tamano_alfabeto <= 0 or longitud <= 0:
        raise ValueError("El tamaño del alfabeto y la longitud deben ser positivos.")

    return tamano_alfabeto ** longitud


def permutacion_sin_repeticion(n, r):
    """
    Calcula P(n,r) = n! / (n-r)!.
    """
    if n < 0 or r < 0 or r > n:
        raise ValueError("Valores inválidos para permutación.")

    return math.factorial(n) // math.factorial(n - r)


def combinacion(n, r):
    """
    Calcula C(n,r) = n! / (r!(n-r)!).
    """
    if n < 0 or r < 0 or r > n:
        raise ValueError("Valores inválidos para combinación.")

    return math.factorial(n) // (math.factorial(r) * math.factorial(n - r))


def entropia_combinatoria(tamano_alfabeto, longitud):
    """
    Calcula la entropía combinatoria usando log2(N),
    donde N es el número total de claves posibles.
    """
    total = conteo_total(tamano_alfabeto, longitud)
    return math.log2(total)
