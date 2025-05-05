# -*- coding: utf-8 -*-
"""
Created on Sun May  4 22:47:52 2025

@author: k
"""

############## 10: REGLAS DE DIAGNÓSTICO Y CAUSALES
############ TEMA: LÓGICA DE PRIMER ORDEN
############ ENFOQUE: LÓGICA

# Reglas diagnósticas: si hay fiebre y tos, entonces hay gripe.
# Reglas causales: si hay gripe, entonces puede haber fiebre.
hechos = {
    "fiebre": True,
    "tos": True,
    "gripe": False
}

# Diagnóstico
if hechos["fiebre"] and hechos["tos"]:
    hechos["gripe"] = True
    print("Diagnóstico: Tiene gripe.")

# Causal
if hechos["gripe"]:
    print("Causa posible: fiebre (por gripe)")

