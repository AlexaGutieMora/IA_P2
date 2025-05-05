# -*- coding: utf-8 -*-
"""
Created on Sun May  4 22:35:49 2025

@author: k
"""

############## 8: ALGORTIMOS DE BÚSQUEDA LOCAL
############ TEMA: LÓGICA PROPOSICIONAL
############ ENFOQUE: LÓGICA

import random
# Función que evalúa cuántas cláusulas son verdaderas
def evaluar(asignacion, clausulas):
    return sum(any(asignacion.get(var.strip('-'), False) if '-' not in var else not asignacion.get(var[1:], False)
                   for var in clausula) for clausula in clausulas)

# Clausulas en CNF: (A ∨ ¬B), (¬A ∨ B)
clausulas = [["A", "-B"], ["-A", "B"]]
variables = ["A", "B"]

# Asignación inicial aleatoria
asignacion = {var: random.choice([True, False]) for var in variables}

# Hill Climbing
for _ in range(10):  # 10 iteraciones
    vecinos = []
    for var in variables:
        nuevo = asignacion.copy()
        nuevo[var] = not nuevo[var]
        vecinos.append((nuevo, evaluar(nuevo, clausulas)))

    mejor = max(vecinos, key=lambda x: x[1])
    if evaluar(asignacion, clausulas) >= mejor[1]:
        break
    asignacion = mejor[0]

print(f"Asignación encontrada: {asignacion}")
