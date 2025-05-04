# -*- coding: utf-8 -*-
"""
Created on Sun May  4 10:22:47 2025

@author: k
"""

############## 56. FILTROS DE KALMAN
############ TEMA: RAZONAMIENTO PROBABILÍSTICO EN EL TIEMPO 
############ ENFOQUE: PROBABILIDAD (INCERTIDUMBRE)

from pykalman import KalmanFilter
import numpy as np
import matplotlib.pyplot as plt

# Simulamos posición de un objeto con ruido
np.random.seed(0)
n = 50
estado_real = np.cumsum(np.random.normal(0, 1, n))  # posición real
observaciones = estado_real + np.random.normal(0, 1, n)  # posición observada con ruido

# Filtro de Kalman: suposición de modelo lineal + ruido gaussiano
kf = KalmanFilter(transition_matrices=[1],
                  observation_matrices=[1],
                  initial_state_mean=0,
                  observation_covariance=1,
                  transition_covariance=0.1)

estado_filtrado, _ = kf.filter(observaciones)

# Mostrar resultados
plt.plot(observaciones, label='Observado')
plt.plot(estado_real, label='Real')
plt.plot(estado_filtrado, label='Kalman Filtrado')
plt.legend()
plt.title("Filtro de Kalman: seguimiento de posición")
plt.show()

