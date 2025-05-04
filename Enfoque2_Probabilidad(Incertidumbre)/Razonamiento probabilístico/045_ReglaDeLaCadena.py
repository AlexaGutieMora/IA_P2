# -*- coding: utf-8 -*-
"""
Created on Sat May  3 23:48:28 2025

@author: k
"""
############## 45. REGLA DE LA CADENA
############ TEMA: RAZONAMIENTO PROBABILÍSTICO
############ ENFOQUE: PROBABILIDAD (INCERTIDUMBRE)


# La regla de la cadena: P(A,B,C) = P(A) * P(B|A) * P(C|A,B)
# Supongamos eventos:
P_A = 0.6
P_B_dado_A = 0.7
P_C_dado_AB = 0.8

P_ABC = P_A * P_B_dado_A * P_C_dado_AB
print(f"P(A ∧ B ∧ C) usando regla de la cadena: {P_ABC}")
