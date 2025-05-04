# -*- coding: utf-8 -*-
"""
Created on Sun May  4 01:02:14 2025

@author: k
"""
############## 51. PROCESOS ESTACIONARIOS
############ TEMA: RAZONAMIENTO PROBABILÍSTICO EN EL TIEMPO 
############ ENFOQUE: PROBABILIDAD (INCERTIDUMBRE)

import numpy as np
import matplotlib.pyplot as plt

# Generamos un proceso estacionario: ruido blanco (media y varianza constantes)
np.random.seed(0)
ruido_blanco = np.random.normal(loc=0, scale=1, size=100)

plt.plot(ruido_blanco)
plt.title("Proceso Estacionario: Ruido Blanco")
plt.xlabel("Tiempo")
plt.ylabel("Valor")
plt.grid(True)
plt.show()
