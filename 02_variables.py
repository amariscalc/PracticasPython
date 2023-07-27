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

#Uso de la función len(), que  devuelve la "longitud" del valor de la variable
print(len(edad), len(nombre))

pi = 3.14219

'''Los tipo float no son compatibles con la función len()
print(len(pi))
'''

#Inicialización variables en una sola línea. No es muy buena práctica.
name, alias, age, city = "Jose Luis", "Joselu", 35, "Utrera" 
print("Me llamo",name,"tengo",age,"años y soy de",city,". Más conocido como",alias)