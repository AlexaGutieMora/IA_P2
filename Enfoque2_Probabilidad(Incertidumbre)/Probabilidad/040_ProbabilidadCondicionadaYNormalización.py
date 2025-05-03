# -*- coding: utf-8 -*-
"""
Created on Sat May  3 16:43:56 2025

@author: k
"""
############## 40. PROBABILIDAD CONDICIONADA Y NORMALIZACIÓN
############ TEMA: PROBABILIDAD
############ ENFOQUE: PROBABILIDAD (INCERTIDUMBRE)

# Supongamos: P(lluvia) = 0.3, P(sensor detecta lluvia | lluvia) = 0.9, P(sensor detecta lluvia | no lluvia) = 0.2

P_lluvia = 0.3
P_no_lluvia = 0.7

P_sensor_lluvia_dado_lluvia = 0.9
P_sensor_lluvia_dado_no_lluvia = 0.2

# Aplicamos normalización para encontrar P(lluvia | sensor detecta lluvia)
# P(evidencia) = P(sensor|lluvia)*P(lluvia) + P(sensor|no_lluvia)*P(no_lluvia)
P_evidencia = (P_sensor_lluvia_dado_lluvia * P_lluvia) + (P_sensor_lluvia_dado_no_lluvia * P_no_lluvia)

# Probabilidad condicionada
P_lluvia_dado_sensor = (P_sensor_lluvia_dado_lluvia * P_lluvia) / P_evidencia

print(f"Probabilidad de que esté lloviendo dado que el sensor lo detectó: {P_lluvia_dado_sensor:.2f}")
