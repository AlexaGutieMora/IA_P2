# -*- coding: utf-8 -*-
"""
Created on Sun May  4 10:08:10 2025

@author: k
"""
############## 54. ALGORITMO HACIA DELANTE - ATRÁS
############ TEMA: RAZONAMIENTO PROBABILÍSTICO EN EL TIEMPO 
############ ENFOQUE: PROBABILIDAD (INCERTIDUMBRE)

# Usamos pomegranate para mostrar probabilidad de cada estado oculto en cada tiempo
from pomegranate import HiddenMarkovModel

modelo = HiddenMarkovModel.from_samples(DiscreteDistribution, n_components=2,
                                        X=[['frio', 'calor', 'frio', 'frio']], random_state=1)

# Hacia adelante-atrás: probabilidad marginal de los estados en cada paso
probs = modelo.forward_backward(['frio', 'calor', 'frio', 'frio'])
print("Probabilidades marginales de cada estado en cada instante:")
print(probs)

