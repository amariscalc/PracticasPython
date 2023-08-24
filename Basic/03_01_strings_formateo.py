# Formateo cadenas de texto:

# Inicializar algunas variables
name, surname, age = "Alberto", "Mariscal", 35

'''
Depende del tipo de dato que contenga la variable:
%s string
%d int
%f float
%.NumeroDigitosPuntoFlotante
'''

# Forma simple pero poco optima para el sistema de imprimir un texto con variables.
print ("Hola me llamo "+name+" "+surname+" y tengo "+str(age)+ " años.")

# Imprime texto con las variables formateadas según el tipo de dato.
# Mejor opción junto a la inferencia: print (f"")
print ("Hola me llamo %s %s y tengo %d años."%(name,surname,age))

# Imprime texto sin asegurar el formateo de las variables cada {} corresponde a una variable y se insertarán
# en orden aparecen a final de linea en el paréntesis.
print ("Hola me llamo {} {} y tengo {} años.".format(name,surname,age))

'''
Inferencia de datos
Colocar una "f" antes de las comillas del print.
Es la mejor opción si no vamos a formatear las variablables explicitamente 
'''
print (f"Hola me llamo {name} {surname} y tengo {age} años.")
