# ContadorHorasACME

Autor: David Gabriel Gonzalez Galvez
Fecha: 05/01/2022
Tema: Manejo de ficheros con horas
Estudios Superiores: Instituto Tecnologico Nuestra Señora del Rosario
Nivel: Tecnologo Superior en Analisis de Sistemas
                             DESARROLLO DEL PROGRAMA
La solución de este programa se da haciendo las busquedas y comparaciones
entre dos datos y pues con ello se cuenta el número de horas de cada
individuo que visito las oficinas.
La arquitectura se desarrolla mediante en programa python consola, que usa
instrucciones que ayudan al manejo, se uso como fuente de datos un fichero
en formato .txt. 
El enfoque se basa en la comparación y busqueda de información, que precisa
los datos a buscar.
Este programa se desarrollo con el algoritmo que presento a continuación:

1 Lectura de fichero:
Declaramos una variable que nos permita abrir y la lectura del archivo
open es para abrir y las variables que viene dentro de open "r"
Sirve para colocar en lectura y permita acceder al fichero .txt

2. Declaramos las variables que van a estar conectados

3. Declaramos las variables que vamos a buscar

4. Aquí vamos a comparar las variables  a buscar dentro del fichero. 
Primero de todo declaramos una variable en este caso i que sirve
para almacenar la cantidad de valores que se repiten entre las
dos linea del fichero, en este caso RENE y ASTRID.
i=0 # Variable declarada
SI valor1 ESTA DENTRO DE RENE  Y valor1 ESTA DENTRO DE ASTRID:
   Si se cumple se le suma a i = i +1 En este caso se sumaría 1 a la variable 1
SI valor1 ESTA DENTRO DE RENE  Y valor1 ESTA DENTRO DE ASTRID
    i=i+1 # Si se cumple se le suma a i = i +1 En este caso se sumaría 1 a la variable 1.............

5. Aquí vamos a comparar las variables  a buscar dentro del fichero.
Primero de todo declaramos una variable en este caso i que sirve
para almacenar la cantidad de valores que se repiten entre las
dos linea del fichero, en este caso ASTRID y ANDRES.
j=0 Variable declarada
SI valor1 ESTA DENTRO DE ASTRID  Y valor1 ESTA DENTRO DE ANDRES
     Si se cumple se le suma a j = j +1 En este caso se sumaría 1 a la variable j
SI valor1 ESTA DENTRO DE ASTRID  Y valor1 ESTA DENTRO DE ANDRES
     Si se cumple se le suma a j = j +1 En este caso se sumaría 1 a la variable j.................

6. Aquí vamos a comparar las variables  a buscar dentro del fichero.
Primero de todo declaramos una variable en este caso i que sirve
para almacenar la cantidad de valores que se repiten entre las
dos linea del fichero, en este caso RENE y ANDRES.
k=0 # Variable declarada
SI valor1 ESTA DENTRO DE RENE  Y valor1 ESTA DENTRO DE ANDRES
    Si se cumple se le suma a k = k +1 En este caso se sumaría 1 a la variable k
SI valor1 ESTA DENTRO DE RENE  Y valor1 ESTA DENTRO DE ANDRES
    Si se cumple se le suma a k = k +1 En este caso se sumaría 1 a la variable k.................



7. Aquí vamos a comparar las variables  a buscar dentro del fichero.
Primero de todo declaramos una variable en este caso i que sirve
para almacenar la cantidad de valores que se repiten entre las
dos linea del fichero, en este caso JAVIER y VICTOR.
L=0 # Variable declarada
SI valor1 ESTA DENTRO DE JAVIER  Y valor1 ESTA DENTRO DE VICTOR
     Si se cumple se le suma a L = L +1 En este caso se sumaría 1 a la variable L
SI valor1 ESTA DENTRO DE JAVIER  Y valor1 ESTA DENTRO DE VICTOR
     Si se cumple se le suma a L = L +1 En este caso se sumaría 1 a la variable L................

8. Almacena en una lista la información los procesos anteriores en una variable lista

lista1 = ["RENE-ASTRID", i] # declaramos la lista de los resultados
lista2=  ["ASTRID-ANDRES", j] # declaramos la lista de los resultados
lista3 = ["RENE-ANDRES", k] # declaramos la lista de los resultados
lista4 = ["JAVIER-VICTOR", L] # declaramos la lista de los resultados
lista= [lista1, lista2, lista3, lista4] # Almacenamos las variables


9. En este parámetro se imprime los resultados en forma de lista.A

print ("                     RESULTADOS A MOSTRAR") # Titulo
print ("Autor: David Gabriel Gonzalez Galvez") # Autor
print ("Fecha de entrega: 05/01/2022 17:02:00") # Fecha de entrega caratula
print ("") # Espacio
print ("LISTA  DE EMPLEADOS Y HORAS") #Titulo del cuadro
print ("............................") # Linea separadora
print('\n'.join(map(str, lista))) # Imprime la lista
print ("............................") # Linea separadora
10. Fin del programa


INSTRUCCIONES PARA EL ARCHIVO


1. Descargar programa python: https://www.python.org/downloads/
2. Descarga el  Ninja ID: https://ninja-ide.softfree.eu/es
3. Instalamos los dos programas primero python luego el Ninja ID
4. Luego en inicio, click en open file y abrir
5. Ejecutamos el programa con el simbolo en forma de hoja con una 
flecha verde en la esquina.

NOTA: Podemos también ejecutar directamente con el python y su ID que ya viene
en la instalación solo da clic derecho y da clic en "Edit With IDLE" y luego
lo ejecutan en el menú Run y clic en Run Module.
ENTORNO DE EJECUCIÓN: https://colab.research.google.com/drive/1BKqX8NImWLSyvOP5hOmoRDTaafQ-Xjfr?usp=sharing 
