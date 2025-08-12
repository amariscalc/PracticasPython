# Importar numpy y fetch_openml
import numpy as np
from sklearn.datasets import fetch_openml

# Cargar el dataset de entrenamiento de MNIST
def cargar_mnist():
    mnist = fetch_openml('mnist_784', version=1)
    mnist["data"].values.astype(np.float32), mnist["target"].values.astype(int)



    