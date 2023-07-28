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
