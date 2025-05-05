# -*- coding: utf-8 -*-
"""
Created on Sun May  4 23:09:14 2025

@author: k
"""
############## 15: SKOLEMIZACIÓN
############ TEMA: LÓGICA DE PRIMER ORDEN
############ ENFOQUE: LÓGICA

from sympy.logic.boolalg import to_cnf
from sympy.abc import x, y, z
from sympy import symbols, Not, Or, And, Implies, Exists, ForAll

# Fórmula ∀x ∃y P(x,y)
# En lógica de predicados, Skolemizamos ∃y → y = f(x)

print("Skolemización teórica:")
print("Original: ∀x ∃y P(x,y)")
print("Skolemizada: ∀x P(x, f(x))")
