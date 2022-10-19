# Proyecto del Primer Cuatrimestre Fundamentos de Programación (Curso  \<XX\>/\<YY\>)
Autor/a: \<Carlos\>   uvus:\<MTD8580\>

Aquí debes añadir la descripción del dataset y un enunciado del dominio del proyecto.


## Estructura de las carpetas del proyecto

* **/src**: Contiene los diferentes módulos de Python que conforman el proyecto.
  * **\<jardineria.py\>**: Describe aquí el módulo principal.
  * **\<jardineria_test.py\>**: Describe aquí el módulo de pruebas.
  * **\<convers.py\>**: Módulo destinado a la conversión de tipos. 
* **/data**: Contiene el dataset o datasets del proyecto
    * **\<jardineria_50.csv\>**: Añade una descripción genérica del dataset.
    * **\<dataset2.csv\>**: Añade una descripción del resto de datasets que puedas tener.
    
## Estructura del *dataset*

Aquí debes describir la estructura del dataset explicando qué representan los datos que contiene y la descripción de cada una de las columnas.

El dataset está compuesto por \<8\> columnas, con la siguiente descripción:

* **\<columna 1>**: de tipo \<cadena\>, representa la calle
* **\<columna 2>**: de tipo \<entero\>, representa el numero de la casa
* **\<columna 3>**: de tipo \<datetime\>, representa la fecha 
* **\<columna 4>**: de tipo \<datetime\>, representa la hora
* **\<columna 5>**: de tipo \<real\>, representa el importe
* **\<columna 6>**: de tipo \<entero\>, representa el numero de jardineros
* **\<columna 7>**: de tipo \<cadena\>, representa los trabajos realizados
* **\<columna 8>**: de tipo \<lógico\>, representa el contrato de mantenimiento

## Tipos implementados

La namedtuple utilizada es "Jardineria", la cual recoge las columnas del csv.

## Funciones implementadas
lee_jardineria--> lee el dataset jardineria_50.csv
conv_date--> convierte la columna fecha(str) a tipo datetime
conv_hora--> convierte la columna hora(str) a tipo datetime

### \<modulo 1\>

* **<lee_jardineria>**: lee el dataset jardineria_50.csv
* **<funcion 2>**: Descripción de la función 2.
* ...

### \<test modulo 1\>

* **<test_lee_jardineria>**: verifica el funcionamiento de la función "lee_jardineria".
* **<test funcion 2>**: Descripción de las pruebas realizadas a la función 2.
* ...
* 
### \<modulo 2\>

* **<funcion 1>**: Descripción de la función 1.
* **<funcion 2>**: Descripción de la función 2.
* ...
