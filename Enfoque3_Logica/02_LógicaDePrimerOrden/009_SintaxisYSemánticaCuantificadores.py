# -*- coding: utf-8 -*-
"""
Created on Sun May  4 22:43:24 2025

@author: k
"""

############## 9: SINTAXIS Y SEMÁNTICA CUANTIFICADORES
############ TEMA: LÓGICA DE PRIMER ORDEN
############ ENFOQUE: LÓGICA

# Evaluamos un cuantificador universal y uno existencial sobre un dominio
dominio = [1, 2, 3, 4]

# Cuantificador universal: ∀x (x > 0)
universal = all(x > 0 for x in dominio)
print(f"∀x (x > 0): {universal}")

# Cuantificador existencial: ∃x (x % 2 == 0)
existencial = any(x % 2 == 0 for x in dominio)
print(f"∃x (x es par): {existencial}")


