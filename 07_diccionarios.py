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

# Obtener los objetos. Devuelve algo parecido a un set que contiene una tupla por cada objeto "key,valor".
my_set_item = list ()
my_set_item = my_other_dict.items()
print (type(my_set_item))
print (my_set_item)

# Comprobar si un key existe, en caso positivo, imprimir el valor de dicha key
if "Apellido" in my_other_dict:
    print ("%s" %(my_other_dict["Apellido"]))
else:
    print ("No existe.")

# Update. Actualizar el diccionario con un diccionario o un objeto iterable con "key,valor"
# WARN! Es case sensitive y puede crearnos un nuevo key,valor si la key no coincide exactamente.
print (my_other_dict) # {'Nombre': 'Alberto', 'Apellido': 'Mariscal', 'Edad': 35}
my_other_dict.update({"Edad":40})
print (my_other_dict) # {'Nombre': 'Alberto', 'Apellido': 'Mariscal', 'Edad': 40}

# Eliminar objetos
# pop elimina el objeto indicado
print (my_other_dict) # {'Nombre': 'Alberto', 'Apellido': 'Mariscal', 'Edad': 40}
print (my_other_dict.pop("Edad")) # 40
print (my_other_dict) # {'Nombre': 'Alberto', 'Apellido': 'Mariscal'}

# popitem elimina el último objeto insertado
print (my_other_dict) # {'Nombre': 'Alberto', 'Apellido': 'Mariscal'}
print (my_other_dict.popitem()) # ('Apellido', 'Mariscal')
print (my_other_dict) # {'Nombre': 'Alberto'}

# del sirve para eliminar item o eliminar el diccionario al completo
# podemos eleminar un item, indicando la key
print (my_third_dict) 
del my_third_dict ["CCAA"]
print (my_third_dict) 

# Eliminar el diccionario si solo se indica el nombre del diccionario
del my_third_dict
#print (my_third_dict) # NameError: name 'my_third_dict' is not defined. Did you mean: 'my_other_dict'?

# Clear limpia/vacía el diccionario.
print (my_other_dict) # {'Nombre': 'Alberto'}
my_other_dict.clear()
print (my_other_dict) # {}

# Loop for en un diccionario
coches = dict ()
coches = {
    id : 1,
    "Marca" : "Seat",
    "Modelo": "Ateca",
    "Color" : "Verde",
    "Paquete": "Premium"
}
for x,y in coches.items():
    print ("%s %s"%(x,y))

# Copiar un diccionario
# Copy
vehiculos = coches.copy()
print (type(vehiculos)) # <class 'dict'>
print (vehiculos) # {<built-in function id>: 1, 'Marca': 'Seat', 'Modelo': 'Ateca', 'Color': 'Verde', 'Paquete': 'Premium'}
# Copiar diccionario con dict ()
new_vehiculos = dict (vehiculos)
print (new_vehiculos) # {<built-in function id>: 1, 'Marca': 'Seat', 'Modelo': 'Ateca', 'Color': 'Verde', 'Paquete': 'Premium'}

# Anidación de diccionarios, es cuando un diccionario contiene diccionarios
provincias = dict ()
provincias = {
    "Sevilla" : {
        "Capital":"Sevilla",
        "Habitantes":1947852,
    },
    "Huelva" : {
        "Capital":"Huelva",
        "Habitantes":525835,
    },
    "Cádiz" : {
        "Capital":"Cádiz",
        "Habitantes":1245960,
    }
}
# Recorremos el diccionario y las provincias en una variable
x = ""
y = "" 
for x in provincias.items():
        print ("Provincia ",x[0])
        # Recorremos los values del diccionario y los guardamos en y que será una tupla
        for y in x[1].items():
            print ("\t %s %s. "%(y[0], y[1]))

# fromkeys. Crear diccionario solo con keys y sin valores
datos_personales = dict.fromkeys (("Nombre","Apellido","Edad","Nacionalidad"))
print (datos_personales) # {'Nombre': None, 'Apellido': None, 'Edad': None, 'Nacionalidad': None}

### Crear un diccionario a partir de una lista.
# Creamos una lista vacia
frutas = []
# Aquí podemos ver que efectivamente es de clase list
print (type(frutas)) # <class 'list'>
# Introducimos algunos datos en la lista
frutas = ["Manzana","Platano","Nazanja","Fresa","Melón","Sandía"]
print (frutas) # ['Manzana', 'Platano', 'Nazanja', 'Fresa', 'Melón', 'Sandía']
# Creamos un diccionario
dict_from_list = {}
# Vemos que se se ha creado correctamente
print (type(dict_from_list)) # <class 'dict'>
# Alimentamos el diccionario con los datos de la lista anterior
dict_from_list = dict.fromkeys(frutas)
# Podemos comprobar que aún sigue siendo de clase dict
print (type(dict_from_list)) # <class 'dict'>
print (dict_from_list) # {'Manzana': None, 'Platano': None, 'Nazanja': None, 'Fresa': None, 'Melón': None, 'Sandía': None}

# Crear un diccionario con keys sin valores a partir de otro diccionario
# Primero vamos a poblar un diccionario que usaremos despues de base para crear el nuevo diccionario sin valores, solo keys.
dict_from_list = {
     "Manzana":3,
     "Plátano":4,
     "Naranja":9,
     "Fresa":6,
     "Melón":3,
     "Sandía": 20
}
print (dict_from_list) # {'Manzana': 3, 'Plátano': 4, 'Naranja': 9, 'Fresa': 6, 'Melón': 3, 'Sandía': 20}
new_dict = dict.fromkeys(dict_from_list)
print (new_dict) # {'Manzana': None, 'Plátano': None, 'Naranja': None, 'Fresa': None, 'Melón': None, 'Sandía': None}

# Misma operación el mismo valor para todas las keys
new_dict = dict.fromkeys(dict_from_list,0)
print (new_dict) # {'Manzana': 0, 'Plátano': 0, 'Naranja': 0, 'Fresa': 0, 'Melón': 0, 'Sandía': 0}