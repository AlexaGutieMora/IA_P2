# -*- coding: utf-8 -*-
"""
Created on Sun May  4 00:05:01 2025

@author: k
"""

############## 47. INFERENCIA POR ENUMERACIÓN
############ TEMA: RAZONAMIENTO PROBABILÍSTICO
############ ENFOQUE: PROBABILIDAD (INCERTIDUMBRE)

# Enumeración para calcular la probabilidad de un evento en una red pequeña
from itertools import product

# P(A) = 0.6, P(B|A) = 0.8, P(B|¬A) = 0.3
# Queremos P(B)
P_A = 0.6
P_B_dado_A = 0.8
P_B_dado_no_A = 0.3

# Enumeramos sobre A
P_B = (P_B_dado_A * P_A) + (P_B_dado_no_A * (1 - P_A))
print(f"P(B) calculado por enumeración: {P_B}")
