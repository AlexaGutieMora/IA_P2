# -*- coding: utf-8 -*-
"""
Created on Sat May  3 16:52:53 2025

@author: k
"""
############## 41. DISTRIBUCIÓN DE PROBABILIDAD
############ TEMA: PROBABILIDAD
############ ENFOQUE: PROBABILIDAD (INCERTIDUMBRE)

# Distribución discreta de una variable aleatoria (por ejemplo, tiro de un dado)
distribucion_dado = {
    1: 1/6,
    2: 1/6,
    3: 1/6,
    4: 1/6,
    5: 1/6,
    6: 1/6
}

print("Distribución de probabilidad para un dado justo:")
for valor, prob in distribucion_dado.items():
    print(f"Valor: {valor}, Probabilidad: {prob}")
