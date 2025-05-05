# -*- coding: utf-8 -*-
"""
Created on Sun May  4 18:26:39 2025

@author: k
"""
############## 72: RETROPROPAGACIÓN DEL ERROR
############ TEMA: REDES NEURONALES
############ ENFOQUE: PROBABILIDAD (INCERTIDUMBRE)

from sklearn.neural_network import MLPClassifier

# Datos XOR
X = np.array([[0,0],[0,1],[1,0],[1,1]])
y = np.array([0,1,1,0])

# Red neuronal con una capa oculta
mlp = MLPClassifier(hidden_layer_sizes=(5,), activation='tanh', max_iter=1000)
mlp.fit(X, y)

print("Predicción XOR con red MLP:", mlp.predict([[1, 0]]))
print("Pesos de la capa oculta:", mlp.coefs_[0])
print("Pesos de la capa de salida:", mlp.coefs_[1])
