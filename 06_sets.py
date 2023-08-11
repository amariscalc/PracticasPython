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