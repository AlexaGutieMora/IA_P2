# -*- coding: utf-8 -*-
"""
Created on Sun May  4 16:13:20 2025

@author: k
"""
############## 63: MODELOS DE MARKOV OCULTOS
############ TEMA: APRENDIZAJE PROBABILÍSTICO 
############ ENFOQUE: PROBABILIDAD (INCERTIDUMBRE)

from hmmlearn import hmm
import numpy as np

# Creamos modelo HMM multinomial con 2 estados ocultos
modelo = hmm.MultinomialHMM(n_components=2, n_iter=10)

# Observaciones: codificamos texto como números
observaciones = np.array([[0], [1], [0], [1], [1]])

# Configuramos parámetros
modelo.startprob_ = np.array([0.6, 0.4])
modelo.transmat_ = np.array([[0.7, 0.3],
                             [0.4, 0.6]])
modelo.emissionprob_ = np.array([[0.9, 0.1], [0.2, 0.8]])

# Decodificamos los estados ocultos
logprob, estados = modelo.decode(observaciones, algorithm="viterbi")
print("Estados ocultos estimados:", estados)
