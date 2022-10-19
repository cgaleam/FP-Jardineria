''' Modulo destinado a la conversion de tipos '''

from datetime import datetime

def conv_date(cadena, formato= "%d/%m/%Y"):  #convierte una cadena (str) en una fecha (datetime.date)
     return datetime.strptime(cadena, formato).date()

def conv_hora(cadena, formato= "%H:%M"):  #convierte una cadena (str) en una hora entero (int)
     return datetime.strptime(cadena, formato).time()
