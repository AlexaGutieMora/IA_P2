# -*- coding: utf-8 -*-
"""
Created on Sun May  4 10:16:45 2025

@author: k
"""

############## 55. MODELOS OCULTOS DE MARKOV
############ TEMA: RAZONAMIENTO PROBABILÍSTICO EN EL TIEMPO 
############ ENFOQUE: PROBABILIDAD (INCERTIDUMBRE)

from hmmlearn import hmm
import numpy as np

# HMM con 2 estados, 2 observaciones: 0=frio, 1=calor
modelo = hmm.MultinomialHMM(n_components=2, n_iter=10, random_state=42)

# Emisión y transición arbitrarias
modelo.startprob_ = np.array([0.6, 0.4])
modelo.transmat_ = np.array([[0.7, 0.3],
                              [0.4, 0.6]])
modelo.emissionprob_ = np.array([[0.9, 0.1],  # estado 0 emite [frio, calor]
                                 [0.2, 0.8]])  # estado 1 emite [frio, calor]

secuencia_obs = np.array([[0], [1], [0], [0]])  # observaciones: frio, calor, frio, frio
logprob, secuencia_estados = modelo.decode(secuencia_obs, algorithm="viterbi")

print("Secuencia más probable de estados ocultos (Viterbi):")
print(secuencia_estados)
