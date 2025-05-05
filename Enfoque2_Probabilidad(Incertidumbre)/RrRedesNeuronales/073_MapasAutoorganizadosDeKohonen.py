# -*- coding: utf-8 -*-
"""
Created on Sun May  4 18:28:09 2025

@author: k
"""
############## 73: MAPAS AUTOORGANIZADOS DE KOHONEN
############ TEMA: REDES NEURONALES
############ ENFOQUE: PROBABILIDAD (INCERTIDUMBRE)

# Requiere biblioteca: pip install minisom
from minisom import MiniSom
from sklearn.datasets import load_iris
from sklearn.preprocessing import MinMaxScaler

data = load_iris()
X = MinMaxScaler().fit_transform(data.data)

som = MiniSom(x=7, y=7, input_len=4, sigma=0.5, learning_rate=0.5)
som.random_weights_init(X)
som.train_random(X, 100)

# Mapeo de los datos
print("Neurona ganadora para la primera muestra:", som.winner(X[0]))
