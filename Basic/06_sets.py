# Sets

'''
Tipo que permite almacenar varios elementos y acceder a ellos de una forma muy similar a las listas 
pero con ciertas diferencias: Los elementos de un set son único, 
lo que significa que no puede haber elementos duplicados
'''
my_set = set ()
my_other_set = {}
print (type(my_set)) # <class 'set'>
print (type(my_other_set)) # <class 'dict'>

my_other_set = {"Alberto", "Mariscal", 35, 1.81}
print (type(my_other_set)) # <class 'set'>
print (my_other_set) # {1.81, 35, 'Mariscal', 'Alberto'} El Set es una estructura NO ordenada

# Add
my_other_set.add ("Sevilla")
print (my_other_set) # {1.81, 'Mariscal', 35, 'Sevilla', 'Alberto'}

# Remove. Si el objeto no existe nos arrojará un error.
my_other_set.remove ("Mariscal") # KeyError: 'Marisscal'
print (my_other_set) # {1.81, 35, 'Alberto', 'Sevilla'}

# Discard (). Similar a remove () pero que no arrojará error si el objeto no existe.
my_set_poc = {1,2,True,"Jazmin",3,"Sevilla",5,20,1,"Pepe"}
my_set_poc.discard ("Jazminn") 
print (my_set_poc) # {1, 2, 3, 5, 'Jazmin', 'Sevilla', 20, 'Pepe'}

# Comprobar si un valor está en un set
print ( "Alberto" in my_other_set ) # True

# Eliminar todos los valores / datos del set
my_other_set.clear ()
print (my_other_set) # set()

# Copy. Copiar un set en otro set
my_set = {1,3,5,6,"Sevilla","Madrid","Jerez"}
my_third_set = my_set.copy ()
print (my_third_set) # {1, 3, 5, 'Madrid', 'Jerez', 'Sevilla'}

# Difference. Devuelve un set que contiene las diferencias entre dos sets. El set devuelto 
# contiene objetos que solo existen en el primer set y no en ambos.
my_other_set = { 2,1,4,5,"Sevilla","sevilla","madrid","Madrid"}
my_difference_set = my_set.difference(my_other_set)
print (my_difference_set) # {'Jerez', 3, 6}

# Difference_update. Elimina los objetos que existen en ambos sets. A diferencia del difference() no devuelve
# otro set, sino que se eliminan los objetos sobre el set original
my_difference_update_set = {1,2,3,4,"Sevilla",1.81,25,"Betis","Alberto"}
my_difference_update_set.difference_update(my_other_set) # {3, 1.81, 'Alberto', 'Betis', 25}
print(my_difference_update_set)

# Intersection. Devuelve un nuevo set con los objetos que se encuentran en todos los sets.
a = {1,"Sevilla",3,5,2,"Jacinto",7,5,True, False}
b = {1,2,3,4,5,"Oviedo",6}
c = {"Chocolate",5,2,"Betis",3,"Jaen",4,3.77,6}
d = a.intersection(b,c)
print(type(d)) # <class 'set'>
print(d) # {2, 3, 5}

# Intersection_update. Elimina los objetos que no están presentes en todos los sets.
print (a) # {False, 1, 2, 3, 5, 7, 'Jacinto', 'Sevilla'}
print (type(a)) # <class 'set'>
a.intersection_update(b,c)
print (a) # {2, 3, 5}

# Isdisjoint. Devuelve true si ningun objeto está presente en todos los sets, de lo contrario
# devuelve False.
a = {1,2,3}
b = {2,4,5,6}
print(a.isdisjoint(b)) # False
c = a.isdisjoint(b)
print (c) # False

# Issubset. Devuelve True si todos los objetos del set estan presentes en el otro set.
a = {1,2,3,4}
b = {2,3}
print(a.issubset(b)) # False

# Issuperset. Devuelve True si todos los objetos de un set están presentes en el otro set
print(a.issuperset(b)) #True

# Pop. Elimina un elemento aleatorio del set
print (a) # {1, 2, 3, 4}
x = a.pop()
print (x) # 1
print (a) # {2, 3, 4}

# symmetric_difference. 
# Devuelve un set que contiene todos los objetos salvo los que están presentes en ambos sets
a = {15,";Betis!",3,5,2,True, False,"sevilla", 5,99,0}
b = {2,4,5,7,9,"Sevilla",2.88,4,True}
z = a.symmetric_difference(b)
print(type(z)) # <class 'set'>
print(z) # {False, 2.88, 4, 3, 7, 99, 9, ';Betis!', 15, 'sevilla', 'Sevilla'}

# symmetric_difference_update.
# Elimina los objetos que no están presentes en ambos sets y los inserta en el set que invoca el método
a = {15,";Betis!",3,5,2,True, False,"sevilla", 5,99,0}
b = {2,4,5,7,9,"Sevilla",2.88,4,True}
a.symmetric_difference_update(b)
print (type(a)) # <class 'set'>
print (a) # {';Betis!', 'Sevilla', 3, False, 2.88, 99, 4, 7, 9, 15, 'sevilla'}

# Union. Devuelve un set que contiene los objetos de ambos sets,exceptuando duplicados, por definición
# propia de los sets.
a = {1,2,3,4,5}
b = {6,7,8,9,10}
c = {11,12,13,14,15}

d = a.union(b,c)
print (type(d)) # <class 'set'>
print (d) # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15}

# Update. Actualiza un set añadiendo objetos desde otro set o coleccion de objetos (iterables)
# Si se introduce una única cadena de texto la dividirá en carácteres individuales, tratandolos como
# objetos individuales
y = {"a","b",333, "pepe"}
d.update(y)
print (d) # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 333, 'b', 'a'}

d.update ("Vacaciones")
print (d) #{1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 333, 'a', 'c', 'i', 'V', 'pepe', 'o', 'n', 'e', 'b', 's'}