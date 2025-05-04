# -*- coding: utf-8 -*-
"""
Created on Sun May  4 00:25:25 2025

@author: k
"""

############## 50. PONDERACIÓN DE VEROSIMILITUD
############ TEMA: RAZONAMIENTO PROBABILÍSTICO
############ ENFOQUE: PROBABILIDAD (INCERTIDUMBRE)

def muestra_ponderada(evidencia_B=True):
    A = random.random() < 0.6
    peso = 0.8 if A else 0.3  # probabilidad de que B sea True dado A
    return A, peso

total_peso = 0
peso_a_true = 0
for _ in range(10000):
    A, peso = muestra_ponderada()
    total_peso += peso
    if A:
        peso_a_true += peso

P_A_dado_B = peso_a_true / total_peso
print(f"P(A | B=True) usando ponderación de verosimilitud: {P_A_dado_B}")
