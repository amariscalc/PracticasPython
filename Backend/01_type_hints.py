# Type Hints

nombre = "Alberto"
apellido = "Mariscal"

# Una de las recomendaciones de FastApi es indicar el tipo de dato. Así el propio fastApi puede validar el tipo de dato que le está llegando.
def nombreCompleto (nombre:str,apellido:str):
    print (nombre + " " + apellido)
    print ("Usando nombre variable.title: ") 
    print (nombre.title)

# Imprimir por pantalla mandando las variables para probar la función
nombreCompleto (nombre, apellido)
# Imprimir por pantalla mandando literalmente los string para probar la función
nombreCompleto ("Jose", "Perez")