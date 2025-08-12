# Importar numpy
import numpy as np

# Calcular la media de una secuencia de números con numpy (funcion "mean" de numpy)
def media_numeros(numeros):
    return np.mean(numeros)

# Crear una lista de números y calcular su media (con la función "media_numeros")
lista_numeros = [1, 2, 3, 4, 5]
resultado = media_numeros(lista_numeros) 

# Imprimir el resultado
print(f"La media de los números {lista_numeros} es: {resultado}")