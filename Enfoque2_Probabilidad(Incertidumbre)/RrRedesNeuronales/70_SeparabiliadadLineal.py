# -*- coding: utf-8 -*-
"""
Created on Sun May  4 18:13:35 2025

@author: k
"""
############## 70: SEPARABILIDAD LINEAL
############ TEMA: REDES NEURONALES
############ ENFOQUE: PROBABILIDAD (INCERTIDUMBRE)

import matplotlib.pyplot as plt

# Datos XOR (no linealmente separables)
X = np.array([[0,0],[0,1],[1,0],[1,1]])
y = np.array([0,1,1,0])

# Visualización
for i in range(len(X)):
    color = 'red' if y[i] == 1 else 'blue'
    plt.scatter(X[i,0], X[i,1], color=color)

plt.title("Ejemplo de No Separabilidad Lineal (XOR)")
plt.grid()
plt.show()

