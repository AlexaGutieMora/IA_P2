# -*- coding: utf-8 -*-
"""
Created on Sat May  3 22:27:01 2025

@author: k
"""



############## 43. REGLA DE BAYES
############ TEMA: PROBABILIDAD
############ ENFOQUE: PROBABILIDAD (INCERTIDUMBRE)

P_enfermo = 0.01
P_sano = 0.99

P_positivo_dado_enfermo = 0.99
P_positivo_dado_sano = 0.05

# P(positivo) = P(positivo|enfermo)*P(enfermo) + P(positivo|sano)*P(sano)
P_positivo = (P_positivo_dado_enfermo * P_enfermo) + (P_positivo_dado_sano * P_sano)

# Bayes
P_enfermo_dado_positivo = (P_positivo_dado_enfermo * P_enfermo) / P_positivo

print(f"Probabilidad de estar enfermo dado un test positivo: {P_enfermo_dado_positivo:.4f}")
