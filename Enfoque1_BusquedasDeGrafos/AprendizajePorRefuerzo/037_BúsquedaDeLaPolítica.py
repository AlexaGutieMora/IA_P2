# -*- coding: utf-8 -*-
"""
Created on Sat May  3 14:18:19 2025

@author: k
"""
############## 37. BÚSQUEDA DE LA POLÍTICA
############ TEMA: APRENDIZAJE POR REFUERZO
############ ENFOQUE: BÚSQUEDA DE GRAFOS

import numpy as np
import random

estados = list(range(5))
estado_final = 4
acciones = ['izquierda', 'derecha']
recompensas = [0, 0, 0, 0, 1]  # solo estado 4 da recompensa

def mover(estado, accion):
    if accion == 'derecha':
        return min(estado + 1, estado_final)
    elif accion == 'izquierda':
        return max(estado - 1, 0)
    return estado

# Inicializar con probabilidad 0.5 para ambas acciones
policy = {s: {'izquierda': 0.5, 'derecha': 0.5} for s in estados if s != estado_final}


episodios = 2000
tasa_aprendizaje = 0.01
gamma = 0.9

for ep in range(episodios):
    estado = 0
    trayectoria = []

    # Generar episodio siguiendo la política actual
    while estado != estado_final:
        probs = list(policy[estado].values())
        acciones_posibles = list(policy[estado].keys())
        accion = np.random.choice(acciones_posibles, p=probs)
        siguiente_estado = mover(estado, accion)
        recompensa = recompensas[siguiente_estado]

        trayectoria.append((estado, accion, recompensa))
        estado = siguiente_state = siguiente_estado

    # Evaluar retorno total (recompensa acumulada)
    G = 0
    for t in reversed(range(len(trayectoria))):
        estado, accion, recompensa = trayectoria[t]
        G = recompensa + gamma * G

        # Reforzar acción tomada si retorno fue bueno
        for a in acciones:
            if a == accion:
                policy[estado][a] += tasa_aprendizaje * G * (1 - policy[estado][a])
            else:
                policy[estado][a] -= tasa_aprendizaje * G * policy[estado][a]

        # Normalizar para que siga siendo una distribución de probabilidad
        total = sum(policy[estado].values())
        for a in acciones:
            policy[estado][a] /= total

print("Política aprendida (probabilidad de elegir cada acción):\n")
for s in estados:
    if s == estado_final:
        print(f"Estado {s}: 🏁")
    else:
        izq = policy[s]['izquierda']
        der = policy[s]['derecha']
        print(f"Estado {s}: izquierda = {izq:.2f}, derecha = {der:.2f}")
