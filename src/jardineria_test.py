from jardineria import *
def test_lee_jardineria ():
    print("\nNúmero de registros leidos=", len(datos))
    print("Los tres primeros registros son:", datos[:3])
    print("Los tres ultimos registros son:", datos[:-3])



#Principal
datos=lee_jardineria("proyecto_primer_cuatrimestre-cgaleam/data/jardinería_50.csv")
test_lee_jardineria()