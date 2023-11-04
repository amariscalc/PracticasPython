#Declaración variables
fibo_elements = 0

# Funcion validación numero elementos:
def numero_valido(numero):

    if numero >= 3 and numero <= 20:
        return True
    else:
        return False

# Funcion para crear una lista con la secuencia fibonacci
def secuencia_fibo(numero):
 
    # Creación array cuya longitud se recibe por parámetro en la función
    list_fibo = [i for i in range(numero)]
    
    for items in list_fibo:
        if items == 0:
            list_fibo[0] = 0
        elif items == 1:
            list_fibo[1] = 1
        else :
            list_fibo[items] = list_fibo[items-2] + list_fibo[items-1]
    return list_fibo

def secuencia_reverse(sec_directo):
    # Crear una nueva lista con la misma longitud que la original
    list_fibo_reverso = [i for i in range(len(sec_directo))]
    i=0

    #Usar loop for para poblar el nuevo array con el orden inverso de los valores
    for items in list_fibo_reverso:
        list_fibo_reverso[items] = sec_directo[len(sec_directo)-1-i]
        i = i+1
    return list_fibo_reverso

def posicion_numero_mas_visto(sec_fibo_inversa):
    # Se inicializan variables
    posicion = 0
    valor = 0
    recuento = 0
    recuento_numeros_unicos = 0

    # Se comprueba cuántos elementos únicos hay en la lista sec_fibo_inversa
    for i in range(len(sec_fibo_inversa)):
        num_unico = True
        for j in range(i):
            if sec_fibo_inversa[i] == sec_fibo_inversa[j]:
                num_unico = False
                break
        if num_unico:
            recuento_numeros_unicos += 1

    # Crear una matriz como una lista de listas ue contiene recuento_numeros_unicos filas, 
    # y cada fila es una lista con dos elementos, ambos inicializados a 0. 
    lista_cont = [[0, 0] for _ in range(recuento_numeros_unicos)]

    # Recorrer el array original y comprobar si se ha añadido al array bidimensional, 
    # en caso negativo lo añadimos
    fila = 0
    for i in range(len(sec_fibo_inversa)):
        existe = False

        for j in range(recuento_numeros_unicos):
            if lista_cont[j][0] == sec_fibo_inversa[i]:
                existe = True
                lista_cont[j][1] += 1
                break
                
        if not existe:
            lista_cont[fila][0] = sec_fibo_inversa[i]
            lista_cont[fila][1] = 1
            fila += 1

    for i in range(fila):
        if lista_cont[i][1] > recuento:
            posicion = i
            valor = lista_cont[i][0]
            recuento = lista_cont[i][1]
    

    if recuento > 1:
        resultado= "El valor " + str(valor) + " se repite " + str(recuento) + " veces según la posicion " + str(posicion) + " del array bidimensional."
    else:
        resultado= "Todos los valores de la secuencia aparecen por igual."
    return resultado

# Pedimos el numero de elementos que de los que se debe sacar la secuencia fibonacci
try:
    fibo_elements = int(input ("Inserta el número elementos de Fibonacci a calcular:"))
except ValueError as error_value:
    print ("its a exception. %s" %(error_value))
except Exception as error_exception:
    print ("its a exception. %s" %(error_exception))
else:
    pass

while not numero_valido(fibo_elements):
    fibo_elements = int(input ("Inserta el número elementos de Fibonacci a calcular:"))

# Se obtiene la secuencia Fibonacci
sec_fibo = secuencia_fibo(fibo_elements)
print (f"Secuencia fibonacci:{sec_fibo}")

# Se obtiene la secuencia Fibonacci invertida
sec_fibo = secuencia_reverse(sec_fibo)
print (f"Secuencia fibonacci invertida:{sec_fibo}")

# Se obtiene la primera posición donde aparece el número que más veces está en el array
print(posicion_numero_mas_visto(sec_fibo))
#posicion_numero_mas_visto(sec_fibo)
