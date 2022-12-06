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
    for j in jardineria:
        if j.num_jardineros==num_jardineros and j.calle in calles:
            res.append((j.calle, j.numero, j.fecha))
    return res


def calcular_total_contratos(jardineria):
    res=0
    for j in jardineria:
        if j.contrato_mantenimiento==True:
            res+=j.contrato_mantenimiento
    return res


#Bloque 2

def mayor_num_jardineros(jardineria):
    maximo= max(jardineria, key= lambda x:x.num_jardineros)
    res=[j for j in jardineria if j.num_jardineros==maximo.num_jardineros]
    return res


def orden_importes(jardineria):
    conj=set((j.importe, j.calle, j.numero, j.fecha, j.hora,\
             j.num_jardineros, j.trabajos, j.contrato_mantenimiento) for j in jardineria)
    res=list(conj)
    res.sort(reverse=True)
    return res

 
def agrupa_calle_mayor_importe(jardineria):
    res=dict()
    for j in jardineria:
        importe=j.importe
        if importe in res: #la clave ya esta en el diccionario
            res[importe].append(j.calle)
        else: # la clave no esta en el diccionario
            res[importe]= [j.calle]
    return res


#ENTREGA 3------------------------------------------------------------------------------------------------------------------------------------------------------------------------


#Bloque 3

def contar_calle_por_nombre(jardineria):
    res=dict()
    for j in jardineria:
         clave=j.calle
         if clave in res: 
            res[clave]= res[clave]+1
         else: 
            res[clave]=1
    return res


def calle_con_mayor_numero_de_jardineros(jardineria):
    res=dict()
    for j in jardineria:
         clave=j.calle
         if clave in res: 
            res[clave]+= j.num_jardineros
         else: 
            res[clave]=j.num_jardineros
    return max(res, key=res.get)


def calles_menor_importe(jardineria):
    res=dict()
    for j in jardineria:
         clave=j.calle
         if clave in res: 
            res[clave]= min(j.importe, res[clave])
         else: 
            res[clave]=j.importe
    return res 


def calles_y_sus_importes_ordenados(jardineria):
    res=dict()
    for j in jardineria:
         clave=j.calle
         if clave in res: 
            res[clave].append(j.importe)
         else: 
            res[clave]=[j.importe]
    return res