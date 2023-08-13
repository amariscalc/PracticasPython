'''
 Diccionarios
 Es una colección ordenada, que acepta cambios y no permite duplicados.
 Los diccionarios están formados por pares key:valor
'''

# Crear diccionario
my_dict = dict ()
my_other_dict = {}
my_third_dict = {}

print (type(my_dict)) # <class 'dict'>
print (type(my_other_dict)) # <class 'dict'>

my_other_dict = { "Nombre" : "Alberto", "Apellido" : "Mariscal", "Edad" : 35 } 
print (my_other_dict) # {'Nombre': 'Alberto', 'Apellido': 'Mariscal', 'Edad': 35}

my_third_dict = {
    "Pais" : "España",
    "CCAA" : {"Madrid", "Andalucia","Cataluña","Comunidad Valenciana","Canarias"},
    "Equipos" : {"Madrid", "Barça","Betis", "Sevilla", "Valencia"},
    "Capital" : 45435
}
print (my_third_dict) 

# Comprobar longitudes de los diccionarios
print (len(my_dict)) # 0
print (len(my_other_dict)) # 3
print (len(my_third_dict)) # 4

# Acceder al valor de una key. Podemos llamar al key entre [] o usar el método get()
print (my_other_dict["Apellido"]) # Mariscal
print (my_other_dict.get("Apellido")) # Mariscal

# Obtener las keys de diccionario
print (my_other_dict.keys()) # dict_keys(['Nombre', 'Apellido', 'Edad'])

# Obtener los valores de un diccionario
print (my_other_dict.values()) # dict_values(['Alberto', 'Mariscal', 35])

# Objeter los objetos. Devuelve algo parecido a un set que contiene una tupla por cada objeto "key,valor".
my_set_item = list ()
my_set_item = my_other_dict.items()
print (type(my_set_item))
print (my_set_item)

# Comprobar si un key existe, en caso positivo, imprimir el valor de dicha key
if "Apellido" in my_other_dict:
    print ("%s" %(my_other_dict["Apellido"]))
else:
    print ("No existe.")
