# -*- coding: utf-8 -*-
"""
Created on Sun May  4 15:44:04 2025

@author: k
"""

############## 62: AGRUPAMIENTO NO SUPERVISADO
############ TEMA: APRENDIZAJE PROBABILÍSTICO 
############ ENFOQUE: PROBABILIDAD (INCERTIDUMBRE)

from sklearn.cluster import DBSCAN
from sklearn.datasets import make_moons
import matplotlib.pyplot as plt

# Generamos datos no lineales
X, _ = make_moons(n_samples=300, noise=0.05, random_state=0)

# Clustering con DBSCAN
modelo = DBSCAN(eps=0.2, min_samples=5)
labels = modelo.fit_predict(X)

# Visualización
plt.scatter(X[:, 0], X[:, 1], c=labels, cmap='viridis')
plt.title("Agrupamiento No Supervisado con DBSCAN")
plt.show()
