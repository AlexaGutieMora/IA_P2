# -*- coding: utf-8 -*-
"""
Created on Sun May  4 21:42:49 2025

@author: k
"""

############## 2: BASE DE CONOCIMIENTO
############ TEMA: LÓGICA PROPOSICIONAL
############ ENFOQUE: PROBABILIDAD (INCERTIDUMBRE)

# Base de conocimiento: hechos y reglas
base_conocimiento = {
    'llueve': True,
    'tengo_paraguas': True,
    'me_mojo': lambda llueve, tengo_paraguas: llueve and not tengo_paraguas
}

# Evaluamos si me mojo
resultado = base_conocimiento['me_mojo'](base_conocimiento['llueve'], base_conocimiento['tengo_paraguas'])
print(f"¿Me mojo? {resultado}")
