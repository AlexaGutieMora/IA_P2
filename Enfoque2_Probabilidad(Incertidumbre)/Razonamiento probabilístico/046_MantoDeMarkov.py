# -*- coding: utf-8 -*-
"""
Created on Sat May  3 23:57:14 2025

@author: k
"""

############## 46. MANTO DE MARKOV
############ TEMA: RAZONAMIENTO PROBABILÍSTICO
############ ENFOQUE: PROBABILIDAD (INCERTIDUMBRE)

# Manto de Markov: los nodos son condicionalmente independientes de los demás dado sus vecinos en la red.
from pgmpy.models import BayesianNetwork

# Red: A → B → C. B es el manto de Markov de C.
modelo = BayesianNetwork([("A", "B"), ("B", "C")])

# Manto de Markov de C es solo B, no A
print("Manto de Markov de 'C':", modelo.get_markov_blanket("C"))
