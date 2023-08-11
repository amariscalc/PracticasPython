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
