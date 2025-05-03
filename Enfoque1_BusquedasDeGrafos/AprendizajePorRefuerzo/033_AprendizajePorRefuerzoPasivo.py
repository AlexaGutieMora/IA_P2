# -*- coding: utf-8 -*-
"""
Created on Sat May  3 11:43:25 2025

@author: k
"""
############## 37. APRENDIZAJE POR REFUERZO PASIVO
############ TEMA: APRENDIZAJE POR REFUERZO
############ ENFOQUE: BÚSQUEDA DE GRAFOS
import random
import numpy as np


# Grid de 3x4 con obstáculos y recompensas
# Leyenda: 
# . = libre, # = muro, G = objetivo (+1), P = pozo (-1)

grid = [
    ['.', '.', '.', 'G'],
    ['.', '#', '.', 'P'],
    ['.', '.', '.', '.']
]

# Estados válidos
estados = [(i, j) for i in range(3) for j in range(4) if grid[i][j] != '#']

# Recompensas por estado
recompensas = {
    'G': 1.0,
    'P': -1.0,
    '.': -0.04  # pequeño castigo por cada movimiento
}

# Política fija: siempre ir hacia la derecha si es posible, si no, hacia abajo
def politica_fija(estado):
    i, j = estado
    if (i, j + 1) in estados:
        return (i, j + 1)  # Derecha
    elif (i + 1, j) in estados:
        return (i + 1, j)  # Abajo
    return estado  # Si no se puede mover

# Verifica si el estado es terminal
def es_terminal(estado):
    i, j = estado
    return grid[i][j] in ['G', 'P']

################## APRENDIZAJE PASIVO
# Inicializa valores en 0
V = {s: 0.0 for s in estados}

# Contadores para promediar las recompensas (evaluación directa)
conteo = {s: 0 for s in estados}
total_recompensas = {s: 0.0 for s in estados}

# Ejecutamos muchos episodios siguiendo la política fija
episodios = 1000
for _ in range(episodios):
    estado = (2, 0)  # Estado inicial
    trayectoria = []

    while not es_terminal(estado):
        recompensa = recompensas[grid[estado[0]][estado[1]]]
        trayectoria.append((estado, recompensa))
        estado = politica_fija(estado)

    # Incluir recompensa del estado terminal
    recompensa_final = recompensas[grid[estado[0]][estado[1]]]
    trayectoria.append((estado, recompensa_final))

    # Sumar retorno total de este episodio
    retorno = sum([r for _, r in trayectoria])

    # Evaluación directa: actualizar valores promediados
    for (s, _) in trayectoria:
        conteo[s] += 1
        total_recompensas[s] += retorno
        V[s] = total_recompensas[s] / conteo[s]

print("Valores aprendidos por evaluación directa (aprendizaje por refuerzo pasivo):\n")
for i in range(3):
    fila = ""
    for j in range(4):
        if grid[i][j] == '#':
            fila += "  ######  "
        else:
            valor = V.get((i, j), 0)
            fila += f"{valor:9.3f} "
    print(fila)


