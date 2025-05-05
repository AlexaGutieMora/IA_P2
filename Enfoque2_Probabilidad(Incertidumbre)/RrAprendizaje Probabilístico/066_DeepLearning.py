# -*- coding: utf-8 -*-
"""
Created on Sun May  4 17:38:43 2025

@author: k
"""
############## 66: APRENDIZAJE PROFUNDO (DEEP LEARNING)
############ TEMA: APRENDIZAJE PROBABILÍSTICO 
############ ENFOQUE: PROBABILIDAD (INCERTIDUMBRE)

import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from sklearn.datasets import make_moons
from sklearn.model_selection import train_test_split

# Datos simples no lineales
X, y = make_moons(n_samples=1000, noise=0.2, random_state=0)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

# Red neuronal simple
modelo = Sequential([
    Dense(10, activation='relu', input_shape=(2,)),
    Dense(10, activation='relu'),
    Dense(1, activation='sigmoid')
])

# Compilación y entrenamiento
modelo.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
modelo.fit(X_train, y_train, epochs=20, verbose=0)

# Evaluación
loss, acc = modelo.evaluate(X_test, y_test)
print(f"Exactitud de la red neuronal: {acc:.2f}")

