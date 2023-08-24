'''
Condicionales
Son controles de flujo de ejecución del código.
Si se cumple una condición se ejecuta el código escrito dentro de dicho condicional.
'''

## Condicional if / else

Betis = "Subcampeón"

if "Campeon" in Betis:
    print ("Betis campeón!")
else:
    print ("El Betis no ha sido el campeón.")


total_puntos = 40*3
if total_puntos == 92:
    print ("Se ha llegado a %d puntos."%(total_puntos))
else:
    print ("Solo se ha llegado a %d puntos, insuficientes."%(total_puntos))


if total_puntos > 30 and total_puntos < 100:
    print ("Más de 30 puntos y menos de 100 puntos, tenemos %d puntos."%(total_puntos))
else:
    print ("Tenemos como máximo 30 puntos o más de 100.")


#edad = int(input ("Introduce tu edad: "))
edad = 25
print (type(edad)) # <class 'int'>

if edad < 18:
    print ("Eres menor de edad.")
elif edad >= 18 and edad < 67:
    print ("Mayor de edad y en edad de currar.")
else:
    print ("Ya has luchado bastante. Llegó la hora de jubilarte y disfrutar.")

# Negar la condición. Comprobar si la cadena es vacía y por tanto devuelve False o tiene valor y devuelve True
ciudad = "Sevilla"

if not ciudad:
    print ("La cadena de texto está vacía.")
else:
    print ("La cadena de texto guarda la siguiente cadena: %s"%(ciudad))

print ("Print final")