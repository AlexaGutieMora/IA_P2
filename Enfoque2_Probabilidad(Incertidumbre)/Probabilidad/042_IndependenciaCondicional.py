# -*- coding: utf-8 -*-
"""
Created on Sat May  3 17:17:30 2025

@author: k
"""

############## 42. INDEPENDENCIA CONDICIONAL
############ TEMA: PROBABILIDAD
############ ENFOQUE: PROBABILIDAD (INCERTIDUMBRE)

# Si A y B son independientes dado C, entonces: P(A y B | C) = P(A|C) * P(B|C)
P_lluvia = 0.3
P_trafico_dado_lluvia = 0.8
P_retraso_dado_lluvia = 0.7

# Suponemos que tráfico y retraso son condicionalmente independientes dado que llueve
P_trafico_y_retraso_dado_lluvia = P_trafico_dado_lluvia * P_retraso_dado_lluvia

print(f"P(tráfico y retraso | lluvia) bajo independencia condicional: {P_trafico_y_retraso_dado_lluvia}")
