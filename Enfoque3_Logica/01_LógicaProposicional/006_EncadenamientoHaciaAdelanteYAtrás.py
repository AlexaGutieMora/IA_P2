# -*- coding: utf-8 -*-
"""
Created on Sun May  4 22:14:01 2025

@author: k
"""

############## 6: ENCADENAMIENTO HACIA ADELANTE Y ATRÁS
############ TEMA: LÓGICA PROPOSICIONAL
############ ENFOQUE: LÓGICA

# Base de conocimiento
hechos = {"A"}
reglas = [
    {"antecedentes": {"A"}, "consecuente": "B"},
    {"antecedentes": {"B"}, "consecuente": "C"}
]

# Hacia adelante
objetivo = "C"
derivados = set(hechos)

cambio = True
while cambio:
    cambio = False
    for regla in reglas:
        if regla["antecedentes"].issubset(derivados) and regla["consecuente"] not in derivados:
            derivados.add(regla["consecuente"])
            cambio = True

print(f"Hacia adelante - ¿Se alcanza {objetivo}? {'Sí' if objetivo in derivados else 'No'}")

# Hacia atrás
objetivo = "C"
def hacia_atras(obj):
    if obj in hechos:
        return True
    for regla in reglas:
        if regla["consecuente"] == obj:
            if all(hacia_atras(premisa) for premisa in regla["antecedentes"]):
                return True
    return False

print(f"Hacia atrás - ¿Se alcanza {objetivo}? {'Sí' if hacia_atras(objetivo) else 'No'}")
