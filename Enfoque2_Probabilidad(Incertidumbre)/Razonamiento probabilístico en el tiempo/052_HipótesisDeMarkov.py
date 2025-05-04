# -*- coding: utf-8 -*-
"""
Created on Sun May  4 9:25:09 2025

@author: k
"""

############## 52. HIPÓTESIS DE MARKOV
############ TEMA: RAZONAMIENTO PROBABILÍSTICO EN EL TIEMPO 
############ ENFOQUE: PROBABILIDAD (INCERTIDUMBRE)

import random
# Cadena de Markov: solo depende del estado anterior
estados = ["soleado", "nublado", "lluvioso"]
transicion = {
    "soleado": {"soleado": 0.8, "nublado": 0.15, "lluvioso": 0.05},
    "nublado": {"soleado": 0.2, "nublado": 0.6, "lluvioso": 0.2},
    "lluvioso": {"soleado": 0.1, "nublado": 0.3, "lluvioso": 0.6}
}

estado = "soleado"
secuencia = [estado]

# Simulamos 10 pasos
for _ in range(10):
    probs = list(transicion[estado].values())
    estado = random.choices(estados, weights=probs)[0]
    sequencia.append(estado)

print("Secuencia de estados según proceso de Markov:")
print(sequencia)
