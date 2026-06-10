from src.generador_claves import generar_clave_segura


def test_longitud_clave_generada():
    clave = generar_clave_segura(12)
    assert len(clave) == 12


def test_generar_clave_minima():
    clave = generar_clave_segura(8)
    assert len(clave) == 8
