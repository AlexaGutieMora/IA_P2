# -*- coding: utf-8 -*-
"""
Created on Sun May  4 18:07:28 2025

@author: k
"""
############## : PERCEPTRÓN, ADALINE Y MADELINE
############ TEMA: REDES NEURONALES
############ ENFOQUE: PROBABILIDAD (INCERTIDUMBRE)

from sklearn.linear_model import Perceptron
import numpy as np

# Entradas AND
X = np.array([[0,0],[0,1],[1,0],[1,1]])
y = np.array([0,0,0,1])

# Entrenamiento
modelo = Perceptron(max_iter=10)
modelo.fit(X, y)

print("Predicción del perceptrón:", modelo.predict([[1, 1]]))


