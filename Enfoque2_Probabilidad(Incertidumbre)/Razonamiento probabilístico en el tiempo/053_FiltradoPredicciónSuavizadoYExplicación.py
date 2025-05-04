# -*- coding: utf-8 -*-
"""
Created on Sun May  4 9:38:45 2025

@author: k
"""
############## 53. FILTRADO, PREDICCIÓN, SUAVIZADO Y EXPLICACIÓN
############ TEMA: RAZONAMIENTO PROBABILÍSTICO EN EL TIEMPO 
############ ENFOQUE: PROBABILIDAD (INCERTIDUMBRE)


# Usamos Hidden Markov Model para ilustrar filtrado y predicción
from pomegranate import HiddenMarkovModel, State, DiscreteDistribution

# Modelo simple: 2 estados ocultos con observaciones binarias
estado_soleado = State(DiscreteDistribution({'calor': 0.9, 'frio': 0.1}), name="Soleado")
estado_lluvioso = State(DiscreteDistribution({'calor': 0.2, 'frio': 0.8}), name="Lluvioso")

modelo = HiddenMarkovModel()
modelo.add_states(estado_soleado, estado_lluvioso)
modelo.add_transition(modelo.start, estado_soleado, 0.6)
modelo.add_transition(modelo.start, estado_lluvioso, 0.4)
modelo.add_transition(estado_soleado, estado_soleado, 0.7)
modelo.add_transition(estado_soleado, estado_lluvioso, 0.3)
modelo.add_transition(estado_lluvioso, estado_lluvioso, 0.6)
modelo.add_transition(estado_lluvioso, estado_soleado, 0.4)
modelo.bake()

# Observación: ['calor', 'frio']
observaciones = ['calor', 'frio']

# Filtrado: estimar estado actual dado observaciones pasadas
logp, estados_filtrados = modelo.viterbi(observaciones)
print("Filtrado / Suavizado:")
print(estados_filtrados)
