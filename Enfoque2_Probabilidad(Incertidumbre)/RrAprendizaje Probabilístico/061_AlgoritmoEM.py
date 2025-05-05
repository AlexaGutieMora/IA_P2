# -*- coding: utf-8 -*-
"""
Created on Sun May  4 14:28:32 2025

@author: k
"""
############## 61: ALGORITMO EM
############ TEMA: APRENDIZAJE PROBABILÍSTICO 
############ ENFOQUE: PROBABILIDAD (INCERTIDUMBRE)

from sklearn.mixture import GaussianMixture
import numpy as np

# Creamos datos artificiales con dos distribuciones gaussianas
np.random.seed(42)
X = np.concatenate([
    np.random.normal(loc=0, scale=1, size=(100, 1)),
    np.random.normal(loc=5, scale=1, size=(100, 1))
])

# Aplicamos el algoritmo EM mediante GMM
gmm = GaussianMixture(n_components=2)
gmm.fit(X)

# Clasificamos cada muestra
labels = gmm.predict(X)
print("Medias encontradas por EM:", gmm.means_.ravel())
