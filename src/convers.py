''' Modulo destinado a la conversion de tipos '''

from this import d
from datetime import datetime
import locale

def conv_date(cadena, formato= "%d/%m/%Y"):  #convierte una cadena (str) en una fecha (datetime.date)
     return datetime.strptime(cadena, formato).date()

def conv_hora(cadena, formato= "%H:%M"):  #convierte una cadena (str) en una hora entero (int)
     return datetime.strptime(cadena, formato).time()

def conv_float(cadena):
    locale.setlocale(locale.nombre_fichero, encoding="utf-8")
    "utf-8"
    return locale.atof