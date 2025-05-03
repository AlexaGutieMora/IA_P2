# -*- coding: utf-8 -*-
"""
Created on Sat May  3 16:12:00 2025

@author: k
"""

############## 38. INCERTIDUMBRE
############ TEMA: PROBABILIDAD
############ ENFOQUE: PROBABILIDAD (INCERTIDUMBRE)

import random
# Simulamos una moneda no justa (sesgada) para ilustrar incertidumbre
def lanzar_moneda():
    return "cara" if random.random() < 0.7 else "cruz"  # 70% probabilidad de "cara"

resultados = {"cara": 0, "cruz": 0}
for _ in range(1000):
    resultado = lanzar_moneda()
    resultados[resultado] += 1

print("Resultados después de 1000 lanzamientos:")
print(resultados)
