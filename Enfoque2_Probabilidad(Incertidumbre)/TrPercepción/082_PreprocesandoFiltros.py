# -*- coding: utf-8 -*-
"""
Created on Sun May  4 20:10:50 2025

@author: k
"""
############## 82: PREPROCESADO FILTROS
############ TEMA: PERCEPCIÓN
############ ENFOQUE: PROBABILIDAD (INCERTIDUMBRE)

import cv2
import numpy as np
import matplotlib.pyplot as plt

# Creamos una imagen con ruido
np.random.seed(0)
img = np.random.randint(0, 256, (200, 200), dtype=np.uint8)

# Aplicamos un filtro de desenfoque Gaussiano para suavizar la imagen
blurred = cv2.GaussianBlur(img, (5, 5), 0)

# Mostramos la imagen original y la suavizada
plt.figure(figsize=(10, 4))

plt.subplot(1, 2, 1)
plt.imshow(img, cmap='gray')
plt.title("Imagen con ruido")
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(blurred, cmap='gray')
plt.title("Filtro Gaussiano")
plt.axis('off')

plt.tight_layout()
plt.show()

