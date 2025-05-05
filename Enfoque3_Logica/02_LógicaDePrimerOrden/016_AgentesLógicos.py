# -*- coding: utf-8 -*-
"""
Created on Sun May  4 23:14:02 2025

@author: k
"""
############## 16: AGENTES LÓGICOS
############ TEMA: LÓGICA DE PRIMER ORDEN
############ ENFOQUE: LÓGICA

# Un agente lógico que decide si debe moverse o no
percepciones = {"obstaculo_adelante": False}
acciones = []

# Regla: si no hay obstáculo adelante, entonces avanza
if not percepciones["obstaculo_adelante"]:
    acciones.append("avanzar")

print("Acciones del agente:", acciones)
