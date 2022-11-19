# Proyecto del Primer Cuatrimestre Fundamentos de Programación (Curso  \<XX\>/\<YY\>)
Autor/a: \<Carlos\>   uvus:\<MTD8580\>

Aquí debes añadir la descripción del dataset y un enunciado del dominio del proyecto.


## Estructura de las carpetas del proyecto

* **/src**: Contiene los diferentes módulos de Python que conforman el proyecto.
  * **\<jardineria.py\>**: Describe aquí el módulo principal.
  * **\<jardineria_test.py\>**: Describe aquí el módulo de pruebas.
  * **\<convers.py\>**: Módulo destinado a la conversión de tipos. 
* **/data**: Contiene el dataset o datasets del proyecto
    * **\<jardinería_50.csv\>**: Añade una descripción genérica del dataset.
    
## Estructura del *dataset*

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
lee_jardineria--> lee el dataset jardineria_50.csv.
conv_date--> convierte la columna fecha(str) a tipo datetime.
conv_hora--> convierte la columna hora(str) a tipo datetime.
test_lee_jardineria--> verifica el funcionamiento de la función "lee_jardineria".

### \<jardineria\>

* **<lee_jardineria>**: lee el dataset jardineria_50.csv
* **<filtra_por_calle_y_numero>**: Filtra las tuplas segun la calle y numero de jardineros, devuelve calle, numero y fecha .
* **<calcular_total_contratos>**: Calcula el total de contratos de mantenimiento.
* **<mayor_num_jardineros>**: Obtiene las tuplas con el maximo valor en la variable num_jardineros.
* **<orden_importes>**: Ordena las tuplas de tipo jardineria de mayor a menor importe.
* **<agrupa_calle_mayor_importe>**: Agrupa las calles con su importe correspondiente.

### \<test jardineria\>

* **<test_lee_jardineria>**: verifica el funcionamiento de la función "lee_jardineria".
* **<test_filtra_por_calle_y_numero>**: verifica el funcionamiento de la función "filtra_por_calle_y_numero".
* **<test_calcular_total_contratos>**: verifica el funcionamiento de la función "calcular_total_contratos".
* **<test_mayor_num_jardineros>**: verifica el funcionamiento de la función "mayor_num_jardineros".
* **<test_orden_importes>**: verifica el funcionamiento de la función "orden_importes".
* **<test_agrupa_calle_mayor_importe>**: verifica el funcionamiento de la función "agrupa_calle_mayor_importe".
* 
### \<convers\>

* **<conv_date>**: convierte la columna fecha(str) a tipo datetime.
* **<conv_hora>**: convierte la columna hora(str) a tipo datetime.
* ...
