# -*- coding: utf-8 -*-
"""
Created on Sat May  3 12:48:20 2025

@author: k
"""
############## 34. APRENDIZAJE POR REFUERZO ACTIVO
############ TEMA: APRENDIZAJE POR REFUERZO
############ ENFOQUE: BÚSQUEDA DE GRAFOS

import random
import numpy as np
from collections import defaultdict

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

# Inicialización de política aleatoria
politica = {s: random.choice(acciones) for s in estados if not es_terminal(s)}
valores = {s: 0.0 for s in estados}  # Estimación de V(s)

# Inicializar modelo aprendido (transiciones y recompensas)
modelo_transiciones = defaultdict(lambda: defaultdict(int))
modelo_recompensas = {}

gamma = 0.9
alpha = 0.1
epsilon = 0.2
episodios = 1000

for ep in range(episodios):
    estado = (2, 0)

    while not es_terminal(estado):
        # Selección de acción con ε-greedy
        if random.random() < epsilon:
            accion = random.choice(acciones)
        else:
            accion = politica.get(estado, random.choice(acciones))

        siguiente_estado = mover(estado, accion)
        recompensa = recompensas[grid[siguiente_estado[0]][siguiente_estado[1]]]

        # Aprender el modelo (conteo de transiciones)
        modelo_transiciones[(estado, accion)][siguiente_estado] += 1
        modelo_recompensas[(estado, accion)] = recompensa

        # Actualizar estimación de valor (tipo iteración de valores con modelo aprendido)
        if not es_terminal(siguiente_estado):
            valores[siguiente_estado] = valores[siguiente_estado] + alpha * (
                recompensa + gamma * valores.get(siguiente_estado, 0) - valores[siguiente_estado]
            )

        # Actualizar política para estado actual usando el modelo aprendido
        mejores_valores = {}
        for a in acciones:
            transiciones = modelo_transiciones[(estado, a)]
            total = sum(transiciones.values())
            if total == 0:
                continue
            valor_estimado = 0.0
            for s_prime, freq in transiciones.items():
                prob = freq / total
                r = modelo_recompensas.get((estado, a), 0)
                valor_estimado += prob * (r + gamma * valores[s_prime])
            mejores_valores[a] = valor_estimado

        if mejores_valores:
            politica[estado] = max(mejores_valores, key=mejores_valores.get)

        estado = siguiente_estado

print("Política aprendida (Aprendizaje por refuerzo activo general):\n")
for i in range(3):
    fila = ""
    for j in range(4):
        if grid[i][j] == '#':
            fila += "   ###   "
        else:
            accion = politica.get((i, j), 'T' if es_terminal((i, j)) else ' ')
            fila += f"{accion:^9}"
    print(fila)

