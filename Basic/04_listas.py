# Listas

'''
Una lista es una colección de elementos de un mismo tipo o de diferentes tipos, 
en las listas podemos guardar todo tipo de datos o valores, ya sean str, int, 
float, bool incluso otra lista.
'''

# Crear una lista
my_list = list ()

# Crear una segunda lista e inicializarla
my_other_list = [35,56,78,14,25]

# Crear una tercera lista e inicializarla
my_third_list = [35, 1.81, "Alberto", "Mariscal"]

# Eliminar elemento de una lista. Elimina por índice. del "nombreLista[índice]"
print (my_other_list)
del my_other_list [2]
print (my_other_list)

# Comprobar el tipo que son estas listas
print (type(my_list))
print (type(my_other_list))
print (type(my_third_list))

# Mostrar longitud original de las listas
print ("Longitud original de la lista my_list:       %d"%(len(my_list)))
print ("Longitud original de la lista my_other_list: %d"%(len(my_other_list)))
print ("Longitud original de la lista my_third_list: %d"%(len(my_third_list)))

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
# Recorrer la lista e imprimir por pantalla el item y la posición que ocupa en la lista
for item in my_third_list:
    print ("El objeto es %s en la posición %d " %(item, my_third_list.index(item)))

# Contar veces que aparece un elemento en una lista
new_list = [1,1,1,11,2,2,1,"Real Betis", False, 1.75]
print (new_list.count(2))

# Inicializar variables a partir de una lista
age, height, name, surname = my_third_list
print ("Nombre: %s Apellido: %s Edad: %d Altura: %.2f"%(name,surname,age,height))
print ("Nombre: {} Apellido: {} Edad: {} Altura: {}".format(name,surname,age,height))

# Concatenar listas
print (my_third_list + new_list)

# Inicializar lista. Añadir elemento al final de la lista con append().
new_list = list ()
new_list.append("Alberto")
print (new_list)
new_list.append("Mariscal")
print (new_list)

'''
 Insertar dato en la posición/indice indicado con inser(indice,valor). 
 No sustituye el valor de que haya en ese indice. Si se le indica una posición superior a la última de la lista,
 coloca el dato en la última posición.
 '''
new_list.insert(6,"Pepe")
print (new_list)
print (len(new_list))

# remove() elimina el primer elemento que coincida con el valor del dato dentro de un índice de la lista.
new_list.remove ("Mariscal")
print (new_list)

'''
Eliminar un dato de un indice de la lista.
Se le puede indicar la posición de la lista. Normalmente usado para desacoplar el último valor de la lista
y retornarlo. pop()
'''
definitive_list = ["Alberto","Mariscal",35,1.81,"Sevilla","Betis"]
print (definitive_list)
print (definitive_list.pop(3))
print (definitive_list)

# Vaciar la lista
definitive_list.clear ()
print (definitive_list)

# Modificar valores en la lista
definitive_list = ["Alberto","Mariscal",35,1.81,"Sevilla","Betis"]
definitive_list [1] = "Casado"
print (definitive_list)

# Copiar listas
copy_definitive_list = definitive_list.copy ()
definitive_list.clear ()
print (definitive_list)
print (copy_definitive_list)

# Reverse 
copy_definitive_list.reverse ()
print (copy_definitive_list)

# Sort
definitive_list.clear ()
definitive_list = [1,2,3,4,3,2,1.3,5.3,8.44,1.77,4444.3,23.5,99.1,0.4]
definitive_list.sort ()
print (definitive_list)

# Sublistas
print (definitive_list[1:3])
print (definitive_list[1::])
