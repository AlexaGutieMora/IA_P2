# -*- coding: utf-8 -*-
"""
Created on Sat May  3 23:30:50 2025

@author: k
"""

############## 44. RED BAYESIANA
############ TEMA: RAZONAMIENTO PROBABILÍSTICO
############ ENFOQUE: PROBABILIDAD (INCERTIDUMBRE)

# Usamos la librería `pgmpy` para crear una red bayesiana simple
from pgmpy.models import BayesianNetwork
from pgmpy.factors.discrete import TabularCPD

# Definimos una red: Lluvia → Césped mojado
modelo = BayesianNetwork([("Lluvia", "CespedMojado")])

# Definimos la probabilidad de lluvia
cpd_lluvia = TabularCPD(variable="Lluvia", variable_card=2, values=[[0.7], [0.3]])

# Definimos la probabilidad de césped mojado dado lluvia
cpd_cesped = TabularCPD(variable="CespedMojado", variable_card=2,
                        values=[[0.9, 0.2],  # P(césped seco)
                                [0.1, 0.8]], # P(césped mojado)
                        evidence=["Lluvia"], evidence_card=[2])

modelo.add_cpds(cpd_lluvia, cpd_cesped)
print("Red Bayesiana construida correctamente:", modelo.check_model())
