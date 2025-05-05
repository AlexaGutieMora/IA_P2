# -*- coding: utf-8 -*-
"""
Created on Sun May  4 18:59:58 2025

@author: k
"""
############## 75: CORPUS
############ TEMA: TRATAMIENTO PROBABILÍSTICO DEL LENGUAJE
############ ENFOQUE: PROBABILIDAD (INCERTIDUMBRE)

from collections import Counter
import math

# Corpus de ejemplo
corpus = "el gato come pescado el gato duerme el perro ladra"

# Tokenizamos las palabras
tokens = corpus.split()

# Contamos las frecuencias de cada palabra
word_counts = Counter(tokens)
total_words = sum(word_counts.values())

# Probabilidad de una palabra
def word_probability(word):
    return word_counts[word] / total_words

print("Probabilidad de 'gato':", word_probability("gato"))

