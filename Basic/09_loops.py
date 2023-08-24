# Loops / Bucles

'''
Son mecanismo o estructuras que nos permiten iterar de forma reiterada.
Son sirve para pasar por el mismo código varias veces. 
'''

### While ###
i = 0
while i < 10:
    print ("Bucle while con i valor %d"%(i))
    i +=1

print ("Fin del bucle While.")

# While con else
i = 11
while i < 10:
    print ("Bucle while con i valor %d"%(i))
    i +=1
else:
    print ("El else es compatible tambien en el while :-) ")

# Detener bucle con un break
i = 0
while i < 20:
    print ("Bucle while con i valor %d"%(i))
    if (i == 15):
        print ("i vale 15, hacemos break")
        break
    i +=1

### For ###
my_list = [3,4,56,"Sevilla","Galicia",1.81,"Betis","Melón"]

for elements in my_list:
    print (elements)

# Recorrer list,tupla,set y diccionario
my_list = [1,2,3,4,5,"a","b","c","d"]
my_tuple = (1,"Huelva",5.40,3,"Jaen")
my_set = {"Alberto","Sevilla","Python"}
my_dict = {"Marca":"Opel","Modelo":"Corsa","Matrícula":"0123DMZ","Km":1100}

print (type(my_list)) # <class 'list'>
print (type(my_tuple)) # <class 'tuple'>
print (type(my_set)) # <class 'set'>
print (type(my_dict)) # <class 'dict'>

for items_list in my_list:
    print ("valor de my_list: %s"%(items_list))

for items_tuple in my_tuple:
    print ("valor de my_tuple: %s"%(items_tuple))

for items_set in my_set:
    print ("valor de my_set: %s"%(items_set))

for items_keys,items_values in my_dict.items():
    print ("valor de my_dict: %s %s"%(items_keys,items_values))

# for con else
for items_list in my_list:
    print ("valor de my_list: %s"%(items_list))
else:
    print ("Valor fuera de la lista.")

# Detener for con un break
for items_list in my_list:
    print ("valor de my_list: %s"%(items_list))
    if items_list == "b":
        print ("Hemos encontrado el valor %s, salimos del bucle"%(items_list))
        break

print ("Valor fuera de la lista con break.")

for items_keys,items_values in my_dict.items():
    print ("valor de my_dict: %s %s"%(items_keys,items_values))
    if items_values =="Corsa":
        print ("Hemos encontrado el coche {} {}" .format(my_dict["Marca"],items_values))
        break

print ("Valor fuera del dict con break.")

# Detener una iteracción for concreta y continuar con dicho for
# El siguiente modelo con "continue" evitaremos imprimir "items" cuando su valor sea "Modelo" y seguirá
# ejecutandose ese mismo for.
for items in my_dict:
    if items == "Modelo":
        continue
    print(items)