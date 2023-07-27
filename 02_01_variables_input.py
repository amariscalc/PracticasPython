#Inicializar variables pidiendo información por teclado
print ("Bienvenido/a ")
nombre = input ("Introduce tu nombre: ")
edad = input ("Introduce tu edad: ")
lugar_nacimiento = input ("Introduce tu ciudad natal: ")
ciudad_residencia = input ("Introduce tu localidad actual de residencia: ")

print ("Así que eres",nombre,"y tienes,",edad,"años. Además naciste en",lugar_nacimiento,",")
if lugar_nacimiento == ciudad_residencia :
    print("veo que sigues viviendo en tu ciudad natal.")
else :
    print("y vives actualmente en",ciudad_residencia,".")