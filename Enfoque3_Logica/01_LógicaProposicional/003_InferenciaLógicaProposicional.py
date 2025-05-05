# -*- coding: utf-8 -*-
"""
Created on Sun May  4 21:47:10 2025

@author: k
"""

############## 3: INFERENCIA LÓGICA PROPOSICIONAL
############ TEMA: LÓGICA PROPOSICIONAL
############ ENFOQUE: LÓGICA

# Reglas: si A y B entonces C
A = True
B = True
C = None

# Inferencia: modus ponens
if A and B:
    C = True

print(f"C es {C}")
