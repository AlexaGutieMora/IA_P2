# -*- coding: utf-8 -*-
"""
Created on Sun May  4 13:34:08 2025

@author: k
"""
############## 59.APRENDIZAJE BAYESIANO
############ TEMA: APRENDIZAJE PROBABILÍSTICO 
############ ENFOQUE: PROBABILIDAD (INCERTIDUMBRE)

import numpy as np
import matplotlib.pyplot as plt

# Datos observados: número de éxitos en 10 ensayos
exitos = 7
ensayos = 10

# Priori beta (parámetros iniciales): asume una creencia previa
a_prior, b_prior = 2, 2

# Posterior beta (actualización bayesiana con datos)
a_post = a_prior + exitos
b_post = b_prior + (ensayos - exitos)

# Visualización de la distribución posterior
from scipy.stats import beta
x = np.linspace(0, 1, 100)
plt.plot(x, beta.pdf(x, a_post, b_post), label="Posterior")
plt.plot(x, beta.pdf(x, a_prior, b_prior), '--', label="Priori")
plt.title("Aprendizaje Bayesiano: Priori vs Posterior")
plt.legend()
plt.show()
