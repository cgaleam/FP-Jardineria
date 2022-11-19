from collections import namedtuple
from datetime import datetime
import csv
from convers import *

#ENTREGA 1------------------------------------------------------------------------------------------------------------------------------------------------------------------------
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


#ENTREGA 2------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Bloque 1
def  filtra_por_calle_y_numero(jardineria, num_jardineros, calles):
    res=list()
    for i in jardineria:
        if i.num_jardineros==num_jardineros and i.calle in calles:
            res.append((i.calle, i.numero, i.fecha))
    return res


def calcular_total_contratos(jardineria):
    res=0
    for i in jardineria:
        if i.contrato_mantenimiento==True:
            res+=i.contrato_mantenimiento
    return res


#Bloque 2
def mayor_num_jardineros(jardineria):
    maximo= max(jardineria, key= lambda x:x.num_jardineros)
    res=[i for i in jardineria if i.num_jardineros==maximo.num_jardineros]
    return res


def orden_importes(jardineria):
    conj=set((i.importe, i.calle, i.numero, i.fecha, i.hora,\
             i.num_jardineros, i.trabajos, i.contrato_mantenimiento) for i in jardineria)
    res=list(conj)
    res.sort(reverse=True)
    return res

 
def agrupa_calle_mayor_importe(jardineria):
    res=dict()
    for i in jardineria:
        importe=i.importe
        if importe in res: #la clave ya esta en el diccionario
            res[importe].append(i.calle)
        else: # la clave no esta en el diccionario
            res[importe]= [i.calle]
    return res
