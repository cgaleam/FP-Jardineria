from collections import namedtuple
from datetime import *
import csv
from convers import *
from matplotlib import pyplot as plt

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
            contrato_mantenimiento= conv_boolean(contrato_mantenimiento)

            res.append(Jardineria(calle, numero, fecha, hora, importe, num_jardineros, trabajos, contrato_mantenimiento))
            
    return res


#ENTREGA 2------------------------------------------------------------------------------------------------------------------------------------------------------------------------


#Bloque 1

def  filtra_por_calle_y_num_jardineros(jardineria, num_jardineros, calles):
    
    res= []
    for j in jardineria:
        if j.num_jardineros==num_jardineros and j.calle in calles:
            res.append((j.calle, j.numero, j.fecha))

    return res


def calcular_total_contratos(jardineria):

    res= 0
    for j in jardineria:
        if j.contrato_mantenimiento==True:
            res+=j.contrato_mantenimiento

    return res


#Bloque 2

def mayor_num_jardineros(jardineria):

    maximo= max(jardineria, key= lambda x:x.num_jardineros)
    res=[]
    for j in jardineria:
        if j.num_jardineros==maximo.num_jardineros:
            res.append(j)

    return res
    

def mayores_importes_con_contrato_ordenados(jardineria, n):

    res=[]
    for j in jardineria:
        if(j.contrato_mantenimiento):
            res.append(j)
    
    return sorted(res, key= lambda x:x.importe, reverse=True)[:n]

 
def agrupa_calle_por_importe(jardineria):
    res= dict()
    for j in jardineria:
        clave=j.calle
        if clave in res: 
            res[clave].append(j.importe)
        else: 
            res[clave]= [j.importe]
    
    return res


#ENTREGA 3------------------------------------------------------------------------------------------------------------------------------------------------------------------------


#Bloque 3

def contar_calle_por_nombre(jardineria):

    res= dict()
    for j in jardineria:
         clave=j.calle
         if clave in res: 
            res[clave]= res[clave]+1
         else: 
            res[clave]=1

    return res


def calle_con_mayor_numero_de_jardineros(jardineria):

    res= dict()
    for j in jardineria:
         clave=j.calle
         if clave in res: 
            res[clave]+= j.num_jardineros
         else: 
            res[clave]=j.num_jardineros

    return max(res, key=res.get) #devuelve solo la clave


def calles_menor_importe(jardineria):

    res= dict()
    for j in jardineria:
         clave=j.calle
         if clave in res: 
            res[clave]= min(j.importe, res[clave])
         else: 
            res[clave]=j.importe

    return res 


def calles_y_sus_importes_ordenados(jardineria, n):

    res= dict()
    for j in jardineria:
         clave=j.calle
         if clave in res: 
            res[clave].append(j.importe)
         else: 
            res[clave]=[j.importe]

    dicc_res={clave:sorted(valores, reverse=True)[:n] for clave, valores in res.items()} #ordeno y limito a "n" valores el diccionario.

    return dicc_res 

#Bloque 4

def grafica(jardineria):

    calle = []
    for j in jardineria:
        calle.append(j.calle)
        
    importe=[]
    for j in jardineria:
        importe.append(j.importe)
        max(importe)
        
    # Componemos y visualizamos la gráfica
    plt.title(f"Importe máximo recaudado en cada calle")
    plt.xlabel("Calles")
    plt.ylabel("Importes")
    plt.bar(calle,importe, label='importes', color='grey')#es gráfica de barras
    plt.legend()
    plt.show()

