# -*- coding: utf-8 -*-
"""
Created on Sun May  4 22:23:40 2025

@author: k
"""

############## 7: BACKTRACKING
############ TEMA: LÓGICA PROPOSICIONAL
############ ENFOQUE: LÓGICA

# Satisfacer una fórmula lógica usando backtracking (buscando una asignación verdadera)
def satisfacible(expresion, variables):
    for asignacion in product([True, False], repeat=len(variables)):
        contexto = dict(zip(variables, asignacion))
        if eval(expresion, {}, contexto):
            return contexto
    return None

# Expresión lógica como cadena
expresion = "(p or q) and not (p and q)"
variables = ['p', 'q']

resultado = satisfacible(expresion, variables)
print(f"Asignación que satisface: {resultado}")

