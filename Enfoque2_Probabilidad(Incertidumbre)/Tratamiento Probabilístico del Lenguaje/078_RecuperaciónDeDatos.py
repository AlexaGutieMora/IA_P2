# -*- coding: utf-8 -*-
"""
Created on Sun May  4 19:25:26 2025

@author: k
"""
############## 78: RECUPERACIÓN DE DATOS
############ TEMA: TRATAMIENTO PROBABILÍSTICO DEL LENGUAJE
############ ENFOQUE: PROBABILIDAD (INCERTIDUMBRE)

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Documentos de ejemplo
docs = ["el gato duerme", "el perro ladra", "el gato come pescado"]

# Consulta
query = ["gato duerme"]

# Vectorizamos los textos
vectorizer = CountVectorizer()
doc_matrix = vectorizer.fit_transform(docs + query)

# Calculamos similitud del coseno (aproximación a prob. de relevancia)
similarities = cosine_similarity(doc_matrix[-1], doc_matrix[:-1])

print("Similaridad con documentos:", similarities)
