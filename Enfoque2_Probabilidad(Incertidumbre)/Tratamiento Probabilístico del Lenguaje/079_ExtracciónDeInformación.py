# -*- coding: utf-8 -*-
"""
Created on Sun May  4 19:29:13 2025

@author: k
"""

############## 79: EXTRACCIÓN DE INFORMACIÓN
############ TEMA: TRATAMIENTO PROBABILÍSTICO DEL LENGUAJE
############ ENFOQUE: PROBABILIDAD (INCERTIDUMBRE)

import spacy
# Cargamos el modelo de lenguaje (requiere: python -m spacy download es_core_news_sm)
nlp = spacy.load("es_core_news_sm")

texto = "Juan trabaja en Google y vive en México."

# Procesamos el texto
doc = nlp(texto)

# Extraemos entidades nombradas
for ent in doc.ents:
    print(ent.text, "-", ent.label_)

