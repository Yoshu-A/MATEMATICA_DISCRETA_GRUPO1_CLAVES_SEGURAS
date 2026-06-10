import secrets
import string


def generar_clave_segura(longitud=12):
    """
    Genera una clave segura usando el módulo secrets de Python.
    """
    if longitud < 8:
        raise ValueError("La longitud mínima recomendada es 8.")

    alfabeto = string.ascii_letters + string.digits + string.punctuation
    return "".join(secrets.choice(alfabeto) for _ in range(longitud))
