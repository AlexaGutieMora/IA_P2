# -*- coding: utf-8 -*-
"""
Created on Sun May  4 22:03:39 2025

@author: k
"""

############## 4: EQUIVALENCIA, VALIDEZ Y SATISFACIBILIDAD
############ TEMA: LÓGICA PROPOSICIONAL
############ ENFOQUE: LÓGICA

from itertools import product

def left(p, q): return not (p or q)
def right(p, q): return (not p) and (not q)

equivalente = True
for p, q in product([True, False], repeat=2):
    if left(p, q) != right(p, q):
        equivalente = False

print(f"¿Son equivalentes? {equivalente}")
