# -*- coding: utf-8 -*-
"""
Created on Sun May  4 22:09:42 2025

@author: k
"""

############## 5: RESOLUCIÓN Y FORMA NORMAL CONJUNTIVA
############ TEMA: LÓGICA PROPOSICIONAL
############ ENFOQUE: LÓGICA

# Convertimos ¬(p → q) a CNF: ¬(¬p ∨ q) → p ∧ ¬q
from sympy import symbols
from sympy.logic.boolalg import Not, Implies, to_cnf

p, q = symbols('p q')
expresion = Not(Implies(p, q))  # ¬(p → q)
cnf = to_cnf(expresion, simplify=True)

print(f"CNF: {cnf}")
