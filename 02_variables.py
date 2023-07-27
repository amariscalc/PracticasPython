'''
Variables
La convención de nombres de variables de Python establece que lo correcto es que sean minúsculas y en caso
de estar formada por varias palabras, separarlas por guión bajo "_"
'''

#Inicializamos una variables con unos valores
nombre_ciudad = "Sevilla"
edad = 35
nombre = "Alberto"

#Con type() obter el tipo de variable
print (type(nombre_ciudad))
print (type(edad))
print (type(nombre))

#Imprimir por pantalla usando las variables anteriores, de forma concatenada
print ("Me llamo",nombre,"soy de",nombre_ciudad,"y tengo",edad,"años")

#Probar a modificar el tipo de una variable y volver a obtener los tipos
edad = str (edad)
print (type(nombre_ciudad))
print (type(edad))
print (type(nombre))