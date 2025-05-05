# -*- coding: utf-8 -*-
"""
Created on Sun May  4 18:00:19 2025

@author: k
"""
############## 68: FUNCIONES DE ACTIVACIÓN
############ TEMA: REDES NEURONALES
############ ENFOQUE: PROBABILIDAD (INCERTIDUMBRE)

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 100)

# Definimos algunas funciones comunes
sigmoid = 1 / (1 + np.exp(-x))
tanh = np.tanh(x)
relu = np.maximum(0, x)

# Graficamos
plt.plot(x, sigmoid, label="Sigmoid")
plt.plot(x, tanh, label="Tanh")
plt.plot(x, relu, label="ReLU")
plt.legend()
plt.title("Funciones de Activación")
plt.grid()
plt.show()
