# -*- coding: utf-8 -*-
#Autor: David Gabriel Gonzalez Galvez
#Fecha: 05/01/2022
#Tema: Manejo de ficheros con horas
#Estudios Superiores: Instituto Tecnologico Nuestra Señora del Rosario
#Nivel: Tecnologo Superior en Analisis de Sistemas
#                             DESARROLLO DEL PROGRAMA
#Este programa se desarrollo con el algoritmo que presento a continuación:

#1 Lectura de fichero
a = open(r"archivo.txt", 'r') # Nos permite abrir el archivo
# Declaramos una variable que nos permita abrir y la lectura del archivo
# open es para abrir y las variables que viene dentro de open "r"
# Sirve para colocar en lectura y permita acceder al fichero .txt

#Lectura de información
RENE= a.readline() #Declaramos las variables que van a estar conectados
ASTRID= a.readline() #Declaramos las variables que van a estar conectados
ANDRES = a.readline()#Declaramos las variables que van a estar conectados
JAVIER= a.readline() #Declaramos las variables que van a estar conectados
VICTOR= a.readline() #Declaramos las variables que van a estar conectados
# Declaramos cada variable con la finalidad que nos permita acceso a las mismas
# mediante la variable declarada anteriormente "a"  uniendo con el código
# readline que nos sirve para leer y analizar de linea a linea


#          DESARROLLO DEL PRIMER GRUPO DE INFORMACIÓN
# En este grupo declaramos las variables únicas que están en todo el
# grupo de datos.
valor1 = "MO10:00-12:00" # Declaramos las variables que vamos a buscar
valor2 = "MO10:15-12:00" # Declaramos las variables que vamos a buscar
valor3 = "TU10:00-12:00" # Declaramos las variables que vamos a buscar
valor4 = "TH12:00-14:00" # Declaramos las variables que vamos a buscar
valor5=  "TH01:00-03:00" # Declaramos las variables que vamos a buscar
valor6 = "SU20:00-21:00" # Declaramos las variables que vamos a buscar
valor7=  "TH13:00-13:15" # Declaramos las variables que vamos a buscar
valor8 = "SA14:00-18:00" # Declaramos las variables que vamos a buscar
# Estas variables nos sirven para comparar con las condicionales y que
# el programa termine buscando los datos y realizando las respectivas
# comparaciones.

#COMPARACIONES DE LOS DATOS Y LAS RESPECTIVAS BUSQUEDAS

# Aquí vamos a comparar las variables  a buscar dentro del fichero.
# Primero de todo declaramos una variable en este caso i que sirve
# para almacenar la cantidad de valores que se repiten entre las
# dos linea del fichero, en este caso RENE y ASTRID.
i=0 # Variable declarada
if valor1 in RENE and valor1 in ASTRID: # SI valor1 ESTA DENTRO DE RENE  Y valor1 ESTA DENTRO DE ASTRID
    i=i+1 # Si se cumple se le suma a i = i +1 En este caso se sumaría 1 a la variable 1
if valor2 in RENE and valor2 in ASTRID: # SI valor1 ESTA DENTRO DE RENE  Y valor1 ESTA DENTRO DE ASTRID
    i=i+1 # Si se cumple se le suma a i = i +1 En este caso se sumaría 1 a la variable 1
if valor3 in RENE and valor3 in ASTRID: # SI valor1 ESTA DENTRO DE RENE  Y valor1 ESTA DENTRO DE ASTRID
    i=i+1 # Si se cumple se le suma a i = i +1 En este caso se sumaría 1 a la variable 1
if valor4 in RENE and valor4 in ASTRID: # SI valor1 ESTA DENTRO DE RENE  Y valor1 ESTA DENTRO DE ASTRID
    i=i+1 # Si se cumple se le suma a i = i +1 En este caso se sumaría 1 a la variable 1
if valor5 in RENE and valor5 in ASTRID: # SI valor1 ESTA DENTRO DE RENE  Y valor1 ESTA DENTRO DE ASTRID
    i=i+1 # Si se cumple se le suma a i = i +1 En este caso se sumaría 1 a la variable 1
if valor6 in RENE and valor6 in ASTRID: # SI valor1 ESTA DENTRO DE RENE  Y valor1 ESTA DENTRO DE ASTRID
    i=i+1 # Si se cumple se le suma a i = i +1 En este caso se sumaría 1 a la variable 1
if valor7 in RENE and valor7 in ASTRID: # SI valor1 ESTA DENTRO DE RENE  Y valor1 ESTA DENTRO DE ASTRID
    i=i+1 # Si se cumple se le suma a i = i +1 En este caso se sumaría 1 a la variable 1
if valor8 in RENE and valor8 in ASTRID: # SI valor1 ESTA DENTRO DE RENE  Y valor1 ESTA DENTRO DE ASTRID
    i=i+1 # Si se cumple se le suma a i = i +1 En este caso se sumaría 1 a la variable 1


# Aquí vamos a comparar las variables  a buscar dentro del fichero.
# Primero de todo declaramos una variable en este caso i que sirve
# para almacenar la cantidad de valores que se repiten entre las
# dos linea del fichero, en este caso ASTRID y ANDRES.
j=0 # Variable declarada
if valor1 in ASTRID and valor1 in ANDRES:#SI valor1 ESTA DENTRO DE ASTRID  Y valor1 ESTA DENTRO DE ANDRES
    j=j+1 # Si se cumple se le suma a j = j +1 En este caso se sumaría 1 a la variable j
if valor2 in ASTRID or valor2 in ANDRES: #SI valor1 ESTA DENTRO DE ASTRID  Y valor1 ESTA DENTRO DE ANDRES
    j=j+1# Si se cumple se le suma a j = j +1 En este caso se sumaría 1 a la variable j
if valor3 in ASTRID and valor3 in ANDRES: #SI valor1 ESTA DENTRO DE ASTRID  Y valor1 ESTA DENTRO DE ANDRES
    j=j+1 # Si se cumple se le suma a j = j +1 En este caso se sumaría 1 a la variable j
if valor4 in ASTRID or valor4 in ANDRES: #SI valor1 ESTA DENTRO DE ASTRID  Y valor1 ESTA DENTRO DE ANDRES
    j=j+1 # Si se cumple se le suma a j = j +1 En este caso se sumaría 1 a la variable j
if valor5 in ASTRID and valor5 in ANDRES: #SI valor1 ESTA DENTRO DE ASTRID  Y valor1 ESTA DENTRO DE ANDRES
    j=j+1 # Si se cumple se le suma a j = j +1 En este caso se sumaría 1 a la variable j
if valor6 in ASTRID or valor6 in ANDRES: #SI valor1 ESTA DENTRO DE ASTRID  Y valor1 ESTA DENTRO DE ANDRES
    j=j+1 # Si se cumple se le suma a j = j +1 En este caso se sumaría 1 a la variable j
if valor7 in ASTRID and valor7 in ANDRES: #SI valor1 ESTA DENTRO DE ASTRID  Y valor1 ESTA DENTRO DE ANDRES
    j=j+1 # Si se cumple se le suma a j = j +1 En este caso se sumaría 1 a la variable j
if valor8 in ASTRID or valor8 in ANDRES: #SI valor1 ESTA DENTRO DE ASTRID  Y valor1 ESTA DENTRO DE ANDRES
    j=j+1 # Si se cumple se le suma a j = j +1 En este caso se sumaría 1 a la variable j


# Aquí vamos a comparar las variables  a buscar dentro del fichero.
# Primero de todo declaramos una variable en este caso i que sirve
# para almacenar la cantidad de valores que se repiten entre las
# dos linea del fichero, en este caso RENE y ANDRES.
k=0 # Variable declarada
if valor1 in RENE and valor1 in ANDRES: #SI valor1 ESTA DENTRO DE RENE  Y valor1 ESTA DENTRO DE ANDRES
    k=k+1 # Si se cumple se le suma a k = k +1 En este caso se sumaría 1 a la variable k
if valor2 in RENE and valor2 in ANDRES: #SI valor1 ESTA DENTRO DE RENE  Y valor1 ESTA DENTRO DE ANDRES
    k=k+1 # Si se cumple se le suma a k = k +1 En este caso se sumaría 1 a la variable k
if valor3 in RENE and valor3 in ANDRES: #SI valor1 ESTA DENTRO DE RENE  Y valor1 ESTA DENTRO DE ANDRES
    k=k+1 # Si se cumple se le suma a k = k +1 En este caso se sumaría 1 a la variable k
if valor4 in RENE and valor4 in ANDRES: #SI valor1 ESTA DENTRO DE RENE  Y valor1 ESTA DENTRO DE ANDRES
    k=k+1 # Si se cumple se le suma a k = k +1 En este caso se sumaría 1 a la variable k
if valor5 in RENE and valor5 in ANDRES: #SI valor1 ESTA DENTRO DE RENE  Y valor1 ESTA DENTRO DE ANDRES
    k=k+1 # Si se cumple se le suma a k = k +1 En este caso se sumaría 1 a la variable k
if valor6 in RENE and valor6 in ANDRES: #SI valor1 ESTA DENTRO DE RENE  Y valor1 ESTA DENTRO DE ANDRES
    k=k+1 # Si se cumple se le suma a k = k +1 En este caso se sumaría 1 a la variable k
if valor7 in RENE and valor7 in ANDRES: #SI valor1 ESTA DENTRO DE RENE  Y valor1 ESTA DENTRO DE ANDRES
    k=k+1 # Si se cumple se le suma a k = k +1 En este caso se sumaría 1 a la variable k
if valor8 in RENE and valor8 in ANDRES: #SI valor1 ESTA DENTRO DE RENE  Y valor1 ESTA DENTRO DE ANDRES
    k=k+1 # Si se cumple se le suma a k = k +1 En este caso se sumaría 1 a la variable k


# Aquí vamos a comparar las variables  a buscar dentro del fichero.
# Primero de todo declaramos una variable en este caso i que sirve
# para almacenar la cantidad de valores que se repiten entre las
# dos linea del fichero, en este caso JAVIER y VICTOR.
L=0 # Variable declarada
if valor1 in JAVIER and valor1 in VICTOR: #SI valor1 ESTA DENTRO DE JAVIER  Y valor1 ESTA DENTRO DE VICTOR
    L=L+1 # Si se cumple se le suma a L = L +1 En este caso se sumaría 1 a la variable L
if valor2 in JAVIER and valor2 in VICTOR: #SI valor1 ESTA DENTRO DE JAVIER  Y valor1 ESTA DENTRO DE VICTOR
    L=L+1 # Si se cumple se le suma a L = L +1 En este caso se sumaría 1 a la variable L
if valor3 in JAVIER and valor3 in VICTOR: #SI valor1 ESTA DENTRO DE JAVIER  Y valor1 ESTA DENTRO DE VICTOR
    L=L+1 # Si se cumple se le suma a L = L +1 En este caso se sumaría 1 a la variable L
if valor4 in JAVIER and valor4 in VICTOR: #SI valor1 ESTA DENTRO DE JAVIER  Y valor1 ESTA DENTRO DE VICTOR
    L=L+1 # Si se cumple se le suma a L = L +1 En este caso se sumaría 1 a la variable L
if valor5 in JAVIER and valor5 in VICTOR: #SI valor1 ESTA DENTRO DE JAVIER  Y valor1 ESTA DENTRO DE VICTOR
    L=L+1 # Si se cumple se le suma a L = L +1 En este caso se sumaría 1 a la variable L
if valor6 in JAVIER and valor6 in VICTOR: #SI valor1 ESTA DENTRO DE JAVIER  Y valor1 ESTA DENTRO DE VICTOR
    L=L+1 # Si se cumple se le suma a L = L +1 En este caso se sumaría 1 a la variable L
if valor7 in JAVIER and valor7 in VICTOR: #SI valor1 ESTA DENTRO DE JAVIER  Y valor1 ESTA DENTRO DE VICTOR
    L=L+1 # Si se cumple se le suma a L = L +1 En este caso se sumaría 1 a la variable L
if valor8 in JAVIER and valor8 in VICTOR: #SI valor1 ESTA DENTRO DE JAVIER  Y valor1 ESTA DENTRO DE VICTOR
    L=L+1 # Si se cumple se le suma a L = L +1 En este caso se sumaría 1 a la variable L
# Almacena en una lista la información los procesos anteriores

lista1 = ["RENE-ASTRID", i] # declaramos la lista de los resultados
lista2=  ["ASTRID-ANDRES", j] # declaramos la lista de los resultados
lista3 = ["RENE-ANDRES", k] # declaramos la lista de los resultados
lista4 = ["JAVIER-VICTOR", L] # declaramos la lista de los resultados
lista= [lista1, lista2, lista3, lista4] # Almacenamos las variables
#En una variable lista

#En este parámetro se imprime los resultados en forma de lista.A
#Resultados del primer dato
print ("                     RESULTADOS A MOSTRAR") # Titulo
print ("Autor: David Gabriel Gonzalez Galvez") # Autor
print ("Fecha de entrega: 05/01/2022 17:02:00") # Fecha de entrega caratula
print ("") # Espacio
print ("LISTA  DE EMPLEADOS Y HORAS") #Titulo del cuadro
print ("............................") # Linea separadora
print('\n'.join(map(str, lista))) # Imprime la lista
print ("............................") # Linea separadora
# Fin del programa


