# -*- coding: utf-8 -*-
"""
Created on Sun May  4 23:01:37 2025

@author: k
"""

############## 13: ENCADENAMIENTO HACIA ADELANTE Y ATRÁS
############ TEMA: LÓGICA DE PRIMER ORDEN
############ ENFOQUE: LÓGICA


# Hechos y reglas representados para encadenamiento

hechos = {"animal(leon)", "animal(tigre)"}
reglas = [
    {"si": {"animal(X)"}, "entonces": "mortal(X)"}
]

# Reemplazo básico para encadenamiento hacia adelante
nuevos_hechos = set()
for regla in reglas:
    for hecho in hechos:
        if hecho.startswith("animal("):
            X = hecho[7:-1]
            nuevos_hechos.add(f"mortal({X})")

print("Hechos nuevos (encadenamiento hacia adelante):")
print(nuevos_hechos)


