# -*- coding: utf-8 -*-
"""
Created on Sun May  4 19:11:15 2025

@author: k
"""
############## 76: GRAMÁTICAS PROBABILÍSTICAS INDEPENDIENTES DEL CONTEXTO
############ TEMA: TRATAMIENTO PROBABILÍSTICO DEL LENGUAJE
############ ENFOQUE: PROBABILIDAD (INCERTIDUMBRE)

import nltk
from nltk import CFG, ChartParser

# Gramática simple con probabilidades
grammar = nltk.PCFG.fromstring("""
  S -> NP VP [1.0]
  NP -> Det N [0.8] | 'Juan' [0.2]
  VP -> V NP [1.0]
  Det -> 'el' [1.0]
  N -> 'gato' [0.5] | 'perro' [0.5]
  V -> 've' [1.0]
""")

parser = nltk.ViterbiParser(grammar)
sentence = ['Juan', 've', 'el', 'gato']
for tree in parser.parse(sentence):
    print(tree)
