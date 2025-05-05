# -*- coding: utf-8 -*-
"""
Created on Sun May  4 17:07:19 2025

@author: k
"""
############## 65: MÁQUINAS DE VECTORES DE SOPORTE
############ TEMA: APRENDIZAJE PROBABILÍSTICO 
############ ENFOQUE: PROBABILIDAD (INCERTIDUMBRE)

from sklearn.svm import SVC
from sklearn.datasets import make_circles
import matplotlib.pyplot as plt

# Datos no linealmente separables
X, y = make_circles(n_samples=200, factor=0.5, noise=0.05)

# Clasificador SVM con kernel RBF
modelo = SVC(kernel='rbf', C=1)
modelo.fit(X, y)

# Visualización
plt.scatter(X[:, 0], X[:, 1], c=modelo.predict(X), cmap='coolwarm', alpha=0.6)
plt.title("Máquina de Vectores Soporte con Kernel RBF")
plt.show()



