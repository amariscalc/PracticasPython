# Strings o cadenas de texto.

# Inicializamos variables pidiendo los valores por teclado
my_name = input ("Introduce tu nombre: ")
my_pets_name= input ('Introduce el nombre de tu mascota: ')

# Podemos obtener la longitud de las cadenas de textos 
print (len(my_name), len (my_pets_name))

# Imprimir por pantalla el mismo texto de dos formas distintas
print ("Te llamas",my_name,"y tu mascota se llama",my_pets_name)
print ("Te llamas "+my_name+" y tu mascota se llama "+my_pets_name)

# Cadenas de texto con símbolos o conjunto de símbolos que funcionan de forma especial
print ("Cadena de texto que llena una barra inclinada y una n \npara hacer un salto de línea.")

# Tabulaciones
print ("\t Cadena de texto con una tabulación al comienzo.")
print ("\t Cadena de texto con una tabulación al comienzo \t y en medio.")

# Cadena de texto con escape de las contrabarras. Es suficiente con añadir otra \
print ("\\t Cadena de texto con una tabulación al comienzo \\t y en medio.")

# División
#Inicializar una variable con una cadena de texto, de la cual posteriormente se extrae una parte total o parcial
my_name = "Alberto"

# En el [:] empieza a imprimir desde la cifra indicada en la izquierda hasta la indicada en la derecha
# si no se indica cifra en derecha o izquierda se considera desde el principio y/o final según corresponda
my_name_slice = my_name [:2]  # Guarda en la variable my_name_slice un string "Al" 
my_name_slice = my_name [1:4] # Guarda en la variable my_name_slice un string "lbe"
my_name_slice = my_name [3:6] # Guarda en la variable my_name_slice un string "ert" 
my_name_slice = my_name [0]   # Guarda en la variable my_name_slice un string "A"
# Especial atención cuando le indicamos posiciones negativas, ya que empieza a contad "desde atrás"
my_name_slice = my_name [-5] # Guarda en la variable my_name_slice un string "b"
print (my_name_slice)

# Reverse
reversed_name = my_name [::-1]
print (reversed_name)

####
# Funciones del sistema

# Longitud len()
print ("My name is %s and this name has %d characters"%(my_name,(len(my_name))))
print ("My name is {} and this name has {} characters".format(my_name,(len(my_name))))

# Primera letra en mayúsculas capitalize (). Podemos corregir la variable guardando el valor en la misma,
# imprimir por pantalla directamente...
surname = "mariscal"
surname = surname.capitalize ()
print (surname)

city = "sevilla"
print (city.capitalize ())

# Toda la cadena en mayúsculas
equipo = "betis"
equipo = equipo.upper ()
print (equipo)

# Toda la cadena en minúsculas
equipo = "SeViLlA"
equipo = equipo.lower ()
print (equipo)

liga = "LigaSantander"
print (liga.upper ())

# Contar cuantos caracteres concretos tiene una cadena. count ()
postre = "Crema Catalana"
print (postre.count ("a")) # Devuelve un 5 (int) que es el número de "a" que tiene el string

# Consultar si es numérico. isnumeric (). En el siguiente ejemplo devuelve true aunque type dice que es str O_o
age = "35"
print (age.isnumeric())
print (type(age))

# Concatenación de varios
#Ejemplo 1.
marca_coche = "seat"
if marca_coche.upper().isupper():
    print ("Se consiguió el upper!")
else:
    print ("No hubo manera de conseguir el upper")

# Ejemplo 2.
grupo_rap = "SFDK"
if grupo_rap.startswith("S"):
    print ("Siempre fuertes de conciencia!!")
else:
    print ("Seguro que es otro buen grupo de rap.")