from jardineria import *


def test_lee_jardineria():
    print("el numero total de registros es:", len(datos))

datos=lee_jardineria("./data/jardinería_50.csv")
test_lee_jardineria