# -*- coding: utf-8 -*-
"""
Created on Sat May  3 13:59:35 2025

@author: k
"""

############## 36. EXPLORACIÓN VS EXPLOTACIÓN
############ TEMA: APRENDIZAJE POR REFUERZO
############ ENFOQUE: BÚSQUEDA DE GRAFOS

import random

# Entorno simple de 1x5 casillas: el objetivo es llegar al final
estado_final = 4
estados = list(range(5))
acciones = ['izquierda', 'derecha']

# Recompensas: solo se gana al llegar al estado 4
def obtener_recompensa(estado):
    return 1.0 if estado == estado_final else 0.0

# Moverse en el entorno
def mover(estado, accion):
    if accion == 'derecha':
        return min(estado + 1, estado_final)
    elif accion == 'izquierda':
        return max(estado - 1, 0)
    return estado

# Inicializamos una política Q arbitraria (valores = 0)
Q = {(s, a): 0.0 for s in estados for a in acciones}

# Parámetros
epsilon = 0.3  # Probabilidad de exploración
alpha = 0.1    # Tasa de aprendizaje
gamma = 0.9    # Descuento
episodios = 200

# Entrenamiento
for ep in range(episodios):
    estado = 0  # Comienza en el extremo izquierdo

    while estado != estado_final:
        # DILEMA EXPLORACIÓN vs EXPLOTACIÓN:
        if random.random() < epsilon:
            accion = random.choice(acciones)  # Exploración
        else:
            # Explotación: elegir la mejor acción conocida
            accion = max(acciones, key=lambda a: Q[(estado, a)])

        siguiente_estado = mover(estado, accion)
        recompensa = obtener_recompensa(siguiente_estado)

        # Actualización de Q
        Q[(estado, accion)] += alpha * (
            recompensa + gamma * max(Q[(siguiente_estado, a)] for a in acciones) - Q[(estado, accion)]
        )

        estado = siguiente_estado

# Mostrar valores aprendidos
print("Valores Q aprendidos (muestran cómo se equilibró exploración y explotación):\n")
for s in estados:
    for a in acciones:
        print(f"Q({s},{a}) = {Q[(s,a)]:.2f}")

# Mostrar política aprendida
print("\nPolítica aprendida (mejor acción por estado):")
for s in estados:
    if s == estado_final:
        print(f"Estado {s}: 🏁")
    else:
        mejor = max(acciones, key=lambda a: Q[(s, a)])
        print(f"Estado {s}: {mejor}")
