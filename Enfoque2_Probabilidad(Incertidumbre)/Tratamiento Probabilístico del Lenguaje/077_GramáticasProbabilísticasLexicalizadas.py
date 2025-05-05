# -*- coding: utf-8 -*-
"""
Created on Sun May  4 19:21:49 2025

@author: k
"""
############## 77: GRAMÁTICAS PROBABILÍSTICAS LEXICALIZADAS
############ TEMA: TRATAMIENTO PROBABILÍSTICO DEL LENGUAJE
############ ENFOQUE: PROBABILIDAD (INCERTIDUMBRE)

# Definimos estructuras con palabras asociadas
rules = {
    ("NP", "perro"): 0.6,
    ("NP", "gato"): 0.4,
    ("VP", "ladra"): 0.7,
    ("VP", "duerme"): 0.3
}

# Evaluamos una estructura simple: NP seguido de VP
sentence = ("NP", "perro"), ("VP", "ladra")
prob = 1.0
for rule in sentence:
    prob *= rules.get(rule, 0)

print("Probabilidad lexicalizada de la oración:", prob)


