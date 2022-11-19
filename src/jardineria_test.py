from jardineria import *
def test_lee_jardineria ():
    print("\nNúmero de registros leidos=", len(datos))
    print("Los tres primeros registros son:", datos[:3])
    print("Los tres ultimos registros son:", datos[-3:])

def test_filtra_por_calle_y_numero():
    num_jardineros=1
    calles={"Codorniz", "Zordal","Gavilán"}
    print("-------------------------------------------------------------")
    print("TEST DE LA FUNCIÓN filtra_por_calle_y_numero:")
    print(f"Las tuplas del numero de jardineros {num_jardineros} de {calles} son: {filtra_por_calle_y_numero(datos,num_jardineros,calles)}")

def test_calcular_total_contratos():
    print("-------------------------------------------------------------")
    print("TEST DE LA FUNCIÓN calcular_total_contratos:")
    print(f"El numero total de contratos de mantenimiento son:{calcular_total_contratos(datos)}")

def test_mayor_num_jardineros():
    print("-------------------------------------------------------------")
    print("TEST DE LA FUNCIÓN mayor_num_jardineros:")
    print(f"Las labores de jardineria con más jardineros son:{mayor_num_jardineros(datos)}")

def test_orden_importes():
    print("-------------------------------------------------------------")
    print("TEST DE LA FUNCIÓN orden_importes:")
    print("Las tareas ordeadas de mayor importe a menor quedarían:")
    print(orden_importes(datos))


def test_agrupa_calle_mayor_importe():
    print("-------------------------------------------------------------")
    print("TEST DE LA FUNCIÓN calle_mayor_importe:")
    print(f"Las calles agrupadas por su importes quedarían:")
    print(agrupa_calle_mayor_importe(datos))



#Principal
datos=lee_jardineria("data/jardinería_50.csv")
test_lee_jardineria()
test_filtra_por_calle_y_numero()
test_calcular_total_contratos()
test_mayor_num_jardineros()
test_orden_importes()
test_agrupa_calle_mayor_importe()
