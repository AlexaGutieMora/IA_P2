# -*- coding: utf-8 -*-
"""
Created on Sun May  4 22:54:16 2025

@author: k
"""

############## 12: INFERENCIA LÓGICA UNIFICACIÓN 
############ TEMA: LÓGICA DE PRIMER ORDEN
############ ENFOQUE: LÓGICA

# Unificación básica entre términos (p.ej. padre(X, Y) = padre(juan, Y))
def unificar(x, y):
    if x == y:
        return {}
    if isinstance(x, str) and x.isupper():  # Variable
        return {x: y}
    if isinstance(y, str) and y.isupper():
        return {y: x}
    if isinstance(x, tuple) and isinstance(y, tuple) and x[0] == y[0]:
        theta1 = unificar(x[1], y[1])
        return theta1
    return None

# Ejemplo: padre(X, juan) = padre(ana, juan)
resultado = unificar(("padre", "X", "juan"), ("padre", "ana", "juan"))
print(f"Unificación: {resultado}")
