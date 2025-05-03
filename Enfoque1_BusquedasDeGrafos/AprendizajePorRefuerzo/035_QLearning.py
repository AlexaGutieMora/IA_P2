# -*- coding: utf-8 -*-
"""
Created on Sat May  3 13:13:08 2025

@author: k
"""

############## 35. Q-LEARNING
############ TEMA: APRENDIZAJE POR REFUERZO
############ ENFOQUE: BÚSQUEDA DE GRAFOS

import numpy as np
import random

grid = [
    ['.', '.', '.', 'G'],
    ['.', '#', '.', 'P'],
    ['.', '.', '.', '.']
]

acciones = ['arriba', 'abajo', 'izquierda', 'derecha']
recompensas = {'G': 1.0, 'P': -1.0, '.': -0.04}
estados = [(i, j) for i in range(3) for j in range(4) if grid[i][j] != '#']

def es_terminal(estado):
    i, j = estado
    return grid[i][j] in ['G', 'P']

def mover(estado, accion):
    i, j = estado
    if accion == 'arriba':
        i -= 1
    elif accion == 'abajo':
        i += 1
    elif accion == 'izquierda':
        j -= 1
    elif accion == 'derecha':
        j += 1
    nuevo_estado = (i, j)
    return nuevo_estado if nuevo_estado in estados else estado

Q = {(s, a): 0.0 for s in estados for a in acciones}  # Tabla Q inicial

# Hiperparámetros
alpha = 0.1    # Tasa de aprendizaje
gamma = 0.9    # Factor de descuento
epsilon = 0.2  # Probabilidad de exploración

episodios = 1000

for ep in range(episodios):
    estado = (2, 0)  # Estado inicial

    while not es_terminal(estado):
        # Selección ε-greedy
        if random.random() < epsilon:
            accion = random.choice(acciones)
        else:
            accion = max(acciones, key=lambda a: Q[(estado, a)])

        siguiente_estado = mover(estado, accion)
        recompensa = recompensas[grid[siguiente_estado[0]][siguiente_estado[1]]]
        max_Q_siguiente = max(Q[(siguiente_estado, a)] for a in acciones)

        # Actualización de Q
        Q[(estado, accion)] += alpha * (recompensa + gamma * max_Q_siguiente - Q[(estado, accion)])

        estado = siguiente_estado

politica = {}
for s in estados:
    if es_terminal(s):
        politica[s] = 'T'
    else:
        mejor_accion = max(acciones, key=lambda a: Q[(s, a)])
        politica[s] = mejor_accion

print("Política aprendida mediante Q-Learning:\n")
for i in range(3):
    fila = ""
    for j in range(4):
        if grid[i][j] == '#':
            fila += "   ###   "
        else:
            accion = politica.get((i, j), ' ')
            fila += f"{accion:^9}"
    print(fila)
