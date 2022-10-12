from collections import namedtuple
import csv

from convers import *

Jardineria=namedtuple('Jardineria', 'calle, numero, fecha, hora, importe, num_jardineros, trabajos, contrato_mantenimiento')

def lee_jardineria(nombre_fichero):
    jardineria=[]
    with open(nombre_fichero, encoding='utf-8') as f:
        lector=csv.reader(f,delimiter=";")
        next(lector)
        for calle, numero, fecha, hora, importe, num_jardineros, trabajos, contrato_mantenimiento in lector:
            numero=int(numero)
            fecha=conv_date(fecha)
            hora=conv_hora(hora)
            importe=float(importe)
            num_jardineros=int(num_jardineros)
            contrato_mantenimiento=conv_bool(contrato_mantenimiento)

            tupla=Jardineria(calle, numero, fecha, hora, importe, num_jardineros, trabajos, contrato_mantenimiento)
            jardineria.append(tupla)
    return jardineria