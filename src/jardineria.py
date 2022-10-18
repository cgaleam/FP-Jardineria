from collections import namedtuple
import csv
from convers import *

Jardineria=namedtuple('jardineria', 'calle, numero, fecha, hora, importe, num_jardineros, trabajos, contrato_mantenimiento')

def lee_jardineria(nombre_fichero):
    res=[]
    with open(nombre_fichero,"rt", encoding='utf-8') as f:
        lector=csv.reader(f,delimiter=";")
        next(lector)
        for calle, numero, fecha, hora, importe, num_jardineros, trabajos, contrato_mantenimiento in lector:
            numero=int(numero)
            fecha=conv_date(fecha)
            hora=conv_hora(hora)
            importe=float(importe.replace(",","."))
            num_jardineros=int(num_jardineros)
            if contrato_mantenimiento=='S':
                 contrato_mantenimiento=True
            else:
                contrato_mantenimiento=False

            res.append(Jardineria(calle, numero, fecha, hora, importe, num_jardineros, trabajos, contrato_mantenimiento))
            
    return res