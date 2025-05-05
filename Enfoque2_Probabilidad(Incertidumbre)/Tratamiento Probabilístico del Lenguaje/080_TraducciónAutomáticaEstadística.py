# -*- coding: utf-8 -*-
"""
Created on Sun May  4 19:47:42 2025

@author: k
"""

############## 80: TRADUCCIÓN AUTOMÁTICA ESTADÍSTICA
############ TEMA: TRATAMIENTO PROBABILÍSTICO DEL LENGUAJE
############ ENFOQUE: PROBABILIDAD (INCERTIDUMBRE)

from collections import defaultdict

# Diccionario de traducción con probabilidades (simplificado)
translation_prob = {
    ('el', 'the'): 0.9,
    ('gato', 'cat'): 0.8,
    ('duerme', 'sleeps'): 0.95
}

source_sentence = ['el', 'gato', 'duerme']

# Traducción palabra por palabra maximizando probabilidad
target_sentence = []
for word in source_sentence:
    best_translation = max(
        [(eng, prob) for (src, eng), prob in translation_prob.items() if src == word],
        key=lambda x: x[1]
    )[0]
    target_sentence.append(best_translation)

print("Traducción generada:", " ".join(target_sentence))
