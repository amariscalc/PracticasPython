'''
Tuplas
Es una secuencia de valores agrupados. Sirve para agrupar, como si fueran un único valor, varios valores que, 
por su naturaleza, deben ir juntos. El tipo de datos que representa a las tuplas se llama tuple.
'''

my_tuple = tuple ()
my_other_tuple = ()

print (type(my_tuple))
print (type(my_other_tuple))

my_tuple = ("Alberto","Mariscal","Casado",35,1.81,"Sevilla","Dos Hermanas", "Casado", "Sevilla","Betis","Perro","Sevilla")
print (my_tuple.count("Sevilla"))
print (my_tuple.index("Dos Hermanas"))

'''
A diferencia de las Listas, no podemos alterar las tuplas.
Las tuplas son inmutables.
Ejemplo:
my_tuple [1] = "Pepe" # TypeError: 'tuple' object does not support item assignment
'''

my_other_tuple = (0,1,45,67,32,90)

# Sumar tuplas
print (my_tuple + my_other_tuple)

my_third_tuple = my_tuple + my_other_tuple
print (my_third_tuple[3:6])

'''
Si lo que queremos es una """tupla""" mutable, realmente queremos una lista, podemos reasignarla a lista
y hacer las operaciones necesarias, posteriormente reasignar a tupla por seguridad. 
 '''
my_third_tuple = list (my_third_tuple)
print (type (my_third_tuple)) # <class 'list'>

my_third_tuple.insert(0,"Bético")
my_third_tuple = tuple (my_third_tuple)

print (my_third_tuple)
print (type(my_third_tuple)) # <class 'tuple'>
