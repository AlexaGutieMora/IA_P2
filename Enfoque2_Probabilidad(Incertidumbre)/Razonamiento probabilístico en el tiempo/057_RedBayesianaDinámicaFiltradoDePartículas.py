# -*- coding: utf-8 -*-
"""
Created on Sun May  4 10:42:50 2025

@author: k
"""
############## 57. RED BAYESIANA DINÁMICA: FILTRADO DE PARTÍCULAS
############ TEMA: RAZONAMIENTO PROBABILÍSTICO EN EL TIEMPO 
############ ENFOQUE: PROBABILIDAD (INCERTIDUMBRE)

import numpy as np

# Supongamos que el estado es la posición x en una línea
# x_t = x_{t-1} + ruido

N = 1000  # partículas
x = np.random.normal(0, 1, N)  # inicialización

def transicion(x):
    return x + np.random.normal(0, 1, len(x))

def peso_likelihood(x, z):
    return np.exp(-0.5 * (x - z)**2)

z = 2.5  # observación actual

# Predicción
x_pred = transicion(x)

# Ponderación
pesos = peso_likelihood(x_pred, z)
pesos /= np.sum(pesos)

# Remuestreo
x_resample = np.random.choice(x_pred, size=N, p=pesos)

print(f"Media estimada del estado después del filtrado de partículas: {np.mean(x_resample):.2f}")
