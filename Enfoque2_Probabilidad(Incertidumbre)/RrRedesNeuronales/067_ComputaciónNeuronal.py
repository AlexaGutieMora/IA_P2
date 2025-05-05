# -*- coding: utf-8 -*-
"""
Created on Sun May  4 17:54:42 2025

@author: k
"""

############## 67: COMPUTACIÓN NEURONAL
############ TEMA: REDES NEURONALES
############ ENFOQUE: PROBABILIDAD (INCERTIDUMBRE)

import numpy as np

# Entradas y pesos
inputs = np.array([1.0, 2.0])
weights = np.array([0.4, -0.6])
bias = 0.1

# Cálculo de salida de la neurona
output = np.dot(inputs, weights) + bias
print("Salida de la neurona:", output)
