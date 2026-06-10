# MATEMATICA_DISCRETA_GRUPO1_CLAVES_SEGURAS

## Descripción del proyecto

Este proyecto corresponde al informe final de la asignatura de Matemática Discreta para Ingeniería de Software. Su propósito es desarrollar un prototipo en Python para la generación, validación y análisis combinatorio de claves seguras, aplicando técnicas formales de conteo.

El sistema permite analizar el número total de claves posibles según la longitud y el tamaño del alfabeto, validar claves de acuerdo con políticas de seguridad y generar claves seguras mediante algoritmos implementados en Python.

## Tema de Matemática Discreta aplicado

El núcleo matemático del proyecto se basa en:

- Principio fundamental del conteo.
- Permutaciones con repetición.
- Combinaciones.
- Principio de inclusión-exclusión.
- Análisis de complejidad algorítmica.

## Aplicación en Ingeniería de Software

El proyecto se aplica al área de seguridad informática, específicamente a la generación y validación de claves seguras. Desde la perspectiva de Ingeniería de Software, permite relacionar la Matemática Discreta con el diseño de algoritmos, validación de entradas, análisis de complejidad y construcción de prototipos funcionales.

## Tecnologías utilizadas

- Python 3
- itertools
- math
- secrets
- pandas
- matplotlib
- pytest
- pytest-cov

## Instalacion

Para instalar las dependencias necesarias del proyecto, ejecutar:
**pip install -r requirements.txt**

## Ejecución del Prototipo

Para ejecutar el sistema principal, se debe ejecutar el siguiente comando:
**python src/main.py**

## Ejecución de Pruebas

Para ejecutar las pruebas automatizadas y obtener la cobertura del código, utilizar:
**pytest --cov=src tests/**

## Estructura del repositorio

```text
MATEMATICA_DISCRETA_GRUPO1_CLAVES_SEGURAS/
│
├── README.md
├── README_EN.md
├── requirements.txt
├── src/
│   ├── __init__.py
│   ├── combinatoria.py
│   ├── validador_claves.py
│   ├── generador_claves.py
│   └── main.py
│
├── tests/
│   ├── test_combinatoria.py
│   ├── test_validador_claves.py
│   └── test_generador_claves.py
│
├── docs/
│   ├── informe_final.pdf
│   └── evidencias/
│
└── resultados/



