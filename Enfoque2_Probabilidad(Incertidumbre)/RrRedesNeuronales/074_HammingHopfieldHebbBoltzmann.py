# -*- coding: utf-8 -*-
"""
Created on Sun May  4 18:41:31 2025

@author: k
"""
############## 74: HAMMING, HOPFIELD, HEBB, BOLTZMANN
############ TEMA: REDES NEURONALES
############ ENFOQUE: PROBABILIDAD (INCERTIDUMBRE)

from scipy.linalg import eigh
import numpy as np

# Patrones de entrenamiento (binarios: -1 y 1)
patterns = np.array([[1, -1, 1, -1],
                     [-1, -1, 1, 1]])

# Matriz de pesos por Hebb
W = np.zeros((4, 4))
for p in patterns:
    W += np.outer(p, p)

np.fill_diagonal(W, 0)

# Recuperar patrón ruidoso
x = np.array([1, -1, -1, -1])
output = np.sign(W @ x)
print("Patrón recuperado:", output)
