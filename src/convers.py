''' Modulo destinado a la conversion de tipos '''

from datetime import datetime

def conv_date(cadena, formato= "%d/%m/%Y"):
     return datetime.strptime(cadena, formato).date()

def conv_hora(cadena, formato= "%H:%M"):
     return datetime.strptime(cadena, formato).time()

def conv_boolean(cadena):
     res= None
     if(cadena=="S"):
          res=True
     else:
          res= False
     return res