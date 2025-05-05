# -*- coding: utf-8 -*-
"""
Created on Sun May  4 14:00:16 2025

@author: k
"""

############## 60: NAIVE BAYES
############ TEMA: APRENDIZAJE PROBABILÍSTICO 
############ ENFOQUE: PROBABILIDAD (INCERTIDUMBRE)

from sklearn.naive_bayes import GaussianNB
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

# Cargamos el dataset de iris
X, y = load_iris(return_X_y=True)

# División entrenamiento/prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Clasificador Naïve Bayes Gaussiano
modelo = GaussianNB()
modelo.fit(X_train, y_train)

# Predicción
pred = modelo.predict(X_test)
print("Exactitud:", modelo.score(X_test, y_test))
