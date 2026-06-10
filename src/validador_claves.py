import string


def validar_clave(clave, longitud_minima=8):
    """
    Valida si una clave cumple una política básica de seguridad:
    longitud mínima, mayúscula, minúscula, número y símbolo.
    """
    if not isinstance(clave, str):
        raise TypeError("La clave debe ser una cadena de texto.")

    tiene_mayuscula = any(c in string.ascii_uppercase for c in clave)
    tiene_minuscula = any(c in string.ascii_lowercase for c in clave)
    tiene_numero = any(c in string.digits for c in clave)
    tiene_simbolo = any(c in string.punctuation for c in clave)

    return (
        len(clave) >= longitud_minima
        and tiene_mayuscula
        and tiene_minuscula
        and tiene_numero
        and tiene_simbolo
    )
