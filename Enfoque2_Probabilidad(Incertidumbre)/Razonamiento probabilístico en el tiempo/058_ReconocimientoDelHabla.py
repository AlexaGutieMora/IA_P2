# -*- coding: utf-8 -*-
"""
Created on Sun May  4 13:18:59 2025

@author: k
"""
############## 58. RECONOCIMIENTO DEL HABLA
############ TEMA: RAZONAMIENTO PROBABILÍSTICO EN EL TIEMPO 
############ ENFOQUE: PROBABILIDAD (INCERTIDUMBRE)

from hmmlearn import hmm
import numpy as np

# Supongamos que cada vocal tiene un vector de características (simplificado)
# 'a', 'e', 'i' → observaciones 0, 1, 2
vocales = ['a', 'e', 'i']
observaciones = np.array([[0], [1], [2], [0], [2]])

# Creamos HMM con 3 estados (uno por vocal)
modelo = hmm.MultinomialHMM(n_components=3, n_iter=100, random_state=42)
modelo.fit(observaciones)

# Decodificamos la secuencia de estados (representando las vocales)
logprob, estados = modelo.decode(observaciones, algorithm="viterbi")

print("Estados ocultos estimados para la secuencia de vocales:")
print(estados)
