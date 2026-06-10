from src.validador_claves import validar_clave


def test_clave_valida():
    assert validar_clave("Abc123$%") is True


def test_clave_sin_simbolo():
    assert validar_clave("Abc12345") is False


def test_clave_corta():
    assert validar_clave("A1$b") is False
