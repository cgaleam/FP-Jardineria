# Proyecto del Primer Cuatrimestre Fundamentos de Programación (Curso  \<XX\>/\<YY\>)
Autor/a: \<Carlos\>   uvus:\<MTD8580\>

Este es mi proyecto, en el cual se han trabajado funciones en varios modulos.
Aquí se describen y nombran los elementos utilizados:


## Estructura de las carpetas del proyecto

* **/src**: Contiene los diferentes módulos de Python que conforman el proyecto.
  * **\<jardineria.py\>**: Este es el módulo principal donde se desarrollrán y llevarán
  a cabo todas las funciones del proyecto que no imprimen nada, solo forman parte del desarrollo.
  * **\<jardineria_test.py\>**: Este módulo está únicamente destinado a probar el correcto
  funcionamiento de las funciones del módulo "jardineria.py"
  * **\<convers.py\>**: Módulo destinado a la conversión de tipos. 
* **/data**: Contiene el dataset o datasets del proyecto
    * **\<jardinería_50.csv\>**: Añade una descripción genérica del dataset.
    
## Estructura del *dataset*

El dataset está compuesto por \<8\> columnas, con la siguiente descripción:

* **\<calle>**: de tipo \<cadena\>, representa la calle
* **\<numero>**: de tipo \<entero\>, representa el numero de la casa
* **\<fecha>**: de tipo \<datetime\>, representa la fecha 
* **\<hora>**: de tipo \<datetime\>, representa la hora
* **\<importe>**: de tipo \<real\>, representa el importe
* **\<Nro.jardineros>**: de tipo \<entero\>, representa el numero de jardineros
* **\<Trabajos realizados>**: de tipo \<cadena\>, representa los trabajos realizados
* **\<Contrato de mantenimiento>**: de tipo \<lógico\>, representa el contrato de mantenimiento

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
* **<contar_calle_por_nombre>**: Calcula el numero de trabajos que se han realizado en cada calle.
* **<calle_mayor_numero_de_jardineros>**: Obtiene la calle con más jardineros(suma de todos los trabajadores).
* **<calles_menor_importe>**: Agrupa las calles con su menor importe respectivamente.
* **<calles_y_sus_importes_ordenados>**: Agrupa las calles con sus importes de menor a mayor.
* **<grafica>**: Gráfica que muestra la evolución de los distintos importes con respecto a los trabajos realizados.


### \<test jardineria\>

* **<test_lee_jardineria>**: verifica el funcionamiento de la función "lee_jardineria".
* **<test_filtra_por_calle_y_numero>**: verifica el funcionamiento de la función "filtra_por_calle_y_numero".
* **<test_calcular_total_contratos>**: verifica el funcionamiento de la función "calcular_total_contratos".
* **<test_mayor_num_jardineros>**: verifica el funcionamiento de la función "mayor_num_jardineros".
* **<test_orden_importes>**: verifica el funcionamiento de la función "orden_importes".
* **<test_agrupa_calle_mayor_importe>**: verifica el funcionamiento de la función "agrupa_calle_mayor_importe".
* **<test_contar_calle_por_nombre>**: verifica el funcionamiento de la función "contar_calle_por_nombre".
* **<test_calle_mayor_numero_de_jardineros>**: verifica el funcionamiento de la función "calle_mayor_numero_de_jardineros".
* **<test_calles_menor_importe>**: verifica el funcionamiento de la función "calles_menor_importe".
* **<test_calles_y_sus_importes_ordenados>**: verifica el funcionamiento de la función "calles_y_sus_importes_ordenados".
* **<test_grafica>**: verifica el funcionamiento de la función "grafica".


### \<convers\>

* **<conv_date>**: convierte la columna fecha(str) a tipo datetime.
* **<conv_hora>**: convierte la columna hora(str) a tipo datetime.
* ...
