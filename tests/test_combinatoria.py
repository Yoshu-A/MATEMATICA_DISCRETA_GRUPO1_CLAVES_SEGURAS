from src.combinatoria import conteo_total, combinacion, permutacion_sin_repeticion


def test_conteo_total():
    assert conteo_total(10, 4) == 10000


def test_combinacion():
    assert combinacion(5, 2) == 10


def test_permutacion_sin_repeticion():
    assert permutacion_sin_repeticion(5, 2) == 20
