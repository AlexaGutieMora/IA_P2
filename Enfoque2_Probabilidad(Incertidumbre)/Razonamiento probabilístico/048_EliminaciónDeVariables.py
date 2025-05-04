# -*- coding: utf-8 -*-
"""
Created on Sun May  4 00:15:52 2025

@author: k
"""
############## 48. ELIMINACIÓN DE VARIABLES
############ TEMA: RAZONAMIENTO PROBABILÍSTICO
############ ENFOQUE: PROBABILIDAD (INCERTIDUMBRE)

P_A = 0.6
P_B_dado_A = [0.8, 0.2]  # B=1|A=1, B=1|A=0
P_C_dado_B = [0.9, 0.1]  # C=1|B=1, C=1|B=0

# Eliminamos A y B (marginalizamos)
P_C = (
    P_C_dado_B[0] * (P_B_dado_A[0] * P_A + P_B_dado_A[1] * (1 - P_A)) +
    P_C_dado_B[1] * ((1 - P_B_dado_A[0]) * P_A + (1 - P_B_dado_A[1]) * (1 - P_A))
)

print(f"P(C) después de eliminar A y B: {P_C}")
