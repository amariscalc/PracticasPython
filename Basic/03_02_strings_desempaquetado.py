# Cadenas como secuencias de caracteres

# Una variable inicializada con una cadena de texto
equipo = "Betis"

# Creamos variables que van a contener los caracteres de la cadena anterior
a, b, c, d, e = equipo

# Distintas formas de mostrar por pantalla la cadena. Se puede trabajar con toda la cadena o con la parte
# que se necesite.
print (f"{a}{b}{c}{d}{e}")
print (f"{a}-{b}-{c}-{d}-{e}")
print ("{}{}{}{}{}".format(a,b,c,d,e))
print ("%s%s%s%s%s"%(a,b,c,d,e))
for caracter in equipo:
    print("%s"%(caracter))
    