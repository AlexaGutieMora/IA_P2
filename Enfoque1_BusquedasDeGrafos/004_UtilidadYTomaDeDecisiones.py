# -*- coding: utf-8 -*-
"""
Created on Wed Apr 30 12:22:48 2025

@author: k
"""

import numpy as np
import random

############################################### TEORÍA DE LA UTILIDAD 
# Definimos una función de utilidad simple
def utilidad(estado):
    utilidad_estados = {
        'A': 0,
        'B': 5,
        'C': 10,
        'D': -10
    }
    return utilidad_estados.get(estado, 0)

################ RED DE DECISIÓN
# Representamos una red de decisión: estados, acciones y recompensas
estados = ['A', 'B', 'C', 'D']
acciones = {
    'A': ['ir_B', 'ir_C'],
    'B': ['ir_C', 'ir_D'],
    'C': ['ir_A'],
    'D': []
}

transiciones = {
    ('A', 'ir_B'): 'B',
    ('A', 'ir_C'): 'C',
    ('B', 'ir_C'): 'C',
    ('B', 'ir_D'): 'D',
    ('C', 'ir_A'): 'A'
}

################ MDP: PROCESO DE DECISIÓN DE MARKOV
class MDP:
    def __init__(self, estados, acciones, transiciones, recompensas, gamma=0.9):
        self.estados = estados
        self.acciones = acciones
        self.transiciones = transiciones
        self.recompensas = recompensas
        self.gamma = gamma

    # ----------------- ITERACIÓN DE VALORES -----------------
    def iteracion_valores(self, threshold=0.01):
        V = {s: 0 for s in self.estados}
        while True:
            delta = 0
            for s in self.estados:
                max_valor = float('-inf')
                for a in self.acciones.get(s, []):
                    s_prime = self.transiciones.get((s, a), s)
                    recompensa = self.recompensas.get(s_prime, 0)
                    val = recompensa + self.gamma * V[s_prime]
                    max_valor = max(max_valor, val)
                if max_valor != float('-inf'):
                    delta = max(delta, abs(max_valor - V[s]))
                    V[s] = max_valor
            if delta < threshold:
                break
        return V

    # ----------------- ITERACIÓN DE POLÍTICAS -----------------
    def iteracion_politicas(self):
        V = {s: 0 for s in self.estados}
        pi = {s: random.choice(self.acciones[s]) if self.acciones.get(s) else None for s in self.estados}

        is_stable = False
        while not is_stable:
            # Evaluación de política
            while True:
                delta = 0
                for s in self.estados:
                    a = pi[s]
                    if a is None:
                        continue
                    s_prime = self.transiciones.get((s, a), s)
                    recompensa = self.recompensas.get(s_prime, 0)
                    val = recompensa + self.gamma * V[s_prime]
                    delta = max(delta, abs(val - V[s]))
                    V[s] = val
                if delta < 0.01:
                    break

            # Mejora de política
            is_stable = True
            for s in self.estados:
                old_action = pi[s]
                max_val = float('-inf')
                best_action = None
                for a in self.acciones.get(s, []):
                    s_prime = self.transiciones.get((s, a), s)
                    recompensa = self.recompensas.get(s_prime, 0)
                    val = recompensa + self.gamma * V[s_prime]
                    if val > max_val:
                        max_val = val
                        best_action = a
                if best_action and old_action != best_action:
                    pi[s] = best_action
                    is_stable = False
        return pi, V

################ VALOR DE LA INFORMACIÓN 
def valor_informacion(estado, accion, transiciones, recompensas):
    # Valor esperado con y sin información perfecta
    sin_info = recompensas.get(transiciones.get((estado, accion), estado), 0)
    con_info = max(recompensas.values())
    return con_info - sin_info

################ MDP PARCIALMENTE OBSERVABLE (Simplificado)
# Manejamos una creencia (probabilidad) sobre el estado real
def belief_update(belief, observacion):
    new_belief = {}
    for estado in belief:
        # actualización bayesiana simplificada
        prob_obs = 0.9 if estado == observacion else 0.1
        new_belief[estado] = belief[estado] * prob_obs
    total = sum(new_belief.values())
    for estado in new_belief:
        new_belief[estado] /= total
    return new_belief

################ RED BAYESIANA DINÁMICA 
# Modelo simple: transición probabilística entre estados
def red_bayesiana_dinamica():
    estados = ['Sano', 'Enfermo']
    trans_prob = {
        'Sano': {'Sano': 0.8, 'Enfermo': 0.2},
        'Enfermo': {'Sano': 0.1, 'Enfermo': 0.9}
    }
    estado_actual = 'Sano'
    trayecto = [estado_actual]
    for _ in range(10):
        estado_actual = random.choices(estados, weights=[trans_prob[estado_actual]['Sano'], trans_prob[estado_actual]['Enfermo']])[0]
        trayecto.append(estado_actual)
    return trayecto

################ TEORÍA DE JUEGOS
def teoria_juegos():
    # Juego del Dilema del Prisionero
    pagos = {
        ('Coop', 'Coop'): (3, 3),
        ('Coop', 'Traiciona'): (0, 5),
        ('Traiciona', 'Coop'): (5, 0),
        ('Traiciona', 'Traiciona'): (1, 1)
    }
    acciones = ['Coop', 'Traiciona']
    mejor_respuesta_A = {}
    for a2 in acciones:
        mejor = max(acciones, key=lambda a1: pagos[(a1, a2)][0])
        mejor_respuesta_A[a2] = mejor
    return mejor_respuesta_A

################ PRUEBAS 

# Utilidad básica
print("Utilidad del estado C:", utilidad('C'))

# Red de decisión simple
print("Resultado de acción A->ir_C:", transiciones[('A', 'ir_C')])

# MDP con iteración de valores y políticas
recompensas = {s: utilidad(s) for s in estados}
mdp = MDP(estados, acciones, transiciones, recompensas)
print("Iteración de valores:", mdp.iteracion_valores())
print("Iteración de políticas:", mdp.iteracion_politicas())

# Valor de la información
print("Valor de la información:", valor_informacion('A', 'ir_B', transiciones, recompensas))

# POMDP - actualizando creencias
creencia = {'A': 0.5, 'B': 0.5}
print("Actualización de creencia POMDP:", belief_update(creencia, 'A'))

# Red bayesiana dinámica
print("Trayectoria red bayesiana dinámica:", red_bayesiana_dinamica())

# Teoría de juegos: mejor respuesta
print("Teoría de Juegos (mejor respuesta A):", teoria_juegos())
