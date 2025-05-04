# -*- coding: utf-8 -*-
"""
Created on Sun May  4 00:19:40 2025

@author: k
"""
############## 48. MUESTREO DIRECTO Y POR RECHAZO
############ TEMA: RAZONAMIENTO PROBABILÍSTICO
############ ENFOQUE: PROBABILIDAD (INCERTIDUMBRE)

import random
def muestreo_directo():
    A = random.random() < 0.6
    B = random.random() < (0.8 if A else 0.3)
    return A, B

# Rechazo: solo contamos los que cumplen con una evidencia (por ejemplo B=True)
aceptados = 0
relevantes = 0
for _ in range(10000):
    A, B = muestreo_directo()
    if B:  # evidencia
        aceptados += 1
        if A:
            relevantes += 1

P_A_dado_B = relevantes / aceptados
print(f"P(A | B=True) usando muestreo por rechazo: {P_A_dado_B}")
