# -*- coding: utf-8 -*-
"""
Created on Sun May  4 21:33:02 2025

@author: k
"""
############## 1: SINTAXIS Y SEMÁNTICA
############ TEMA: LÓGICA PROPOSICIONAL
############ ENFOQUE: PROBABILIDAD (INCERTIDUMBRE)

from itertools import product

# Definimos una proposición lógica: p ∧ q
def evaluate(p, q):
    return p and q

# Generamos la tabla de verdad para p y q
print("p\tq\tp ∧ q")
for p, q in product([True, False], repeat=2):
    print(f"{p}\t{q}\t{evaluate(p, q)}")
