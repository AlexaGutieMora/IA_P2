# -*- coding: utf-8 -*-
"""
Created on Sun May  4 22:51:08 2025

@author: k
"""
############## 11: INGENIERÍA DEL CONOCIMIENTO
############ TEMA: LÓGICA DE PRIMER ORDEN
############ ENFOQUE: LÓGICA

# Base de conocimiento representada como una estructura lógica
base_conocimiento = [
    {"nombre": "Socrates", "tipo": "humano"},
    {"nombre": "humano", "propiedad": "mortal"}
]

# Inferencia simple: si X es humano → X es mortal
for hecho in base_conocimiento:
    if hecho.get("tipo") == "humano":
        print(f"{hecho['nombre']} es mortal.")
