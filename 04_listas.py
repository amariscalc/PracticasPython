# Listas

'''
Una lista es una colección de elementos de un mismo tipo o de diferentes tipos, 
en las listas podemos guardar todo tipo de datos o valores, ya sean str, int, 
float, bool incluso otra lista.
'''

# Crear una lista e inicializarla
my_list = list ()

# Crear una segunda lista e inicializarla
my_other_list = [35,56,78,14,25]

# Mostrar longitud original de las listas
print ("Longitud original de la lista my_list:       %d"%(len(my_list)))
print ("Longitud original de la lista my_other_list: %d"%(len(my_other_list)))










# Recorrer la lista e imprimir por pantalla el item y la posición que ocupa en la lista
for item in my_other_list:
    print ("El objeto es %d en la posición %d " %(item, my_other_list.index(item)))

'''
El print anterior muestra  debe mostrar algo similar a:
El objeto es 35 en la posición 0 
El objeto es 56 en la posición 1 
El objeto es 78 en la posición 2 
El objeto es 14 en la posición 3 
El objeto es 25 en la posición 4
'''