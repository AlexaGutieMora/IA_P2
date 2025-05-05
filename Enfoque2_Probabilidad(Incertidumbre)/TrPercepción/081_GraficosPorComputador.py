# -*- coding: utf-8 -*-
"""
Created on Sun May  4 20:02:42 2025

@author: k
"""
############## 81: GRAFICOS POR COMPUTADOR
############ TEMA: PERCEPCIÓN
############ ENFOQUE: PROBABILIDAD (INCERTIDUMBRE)

import cv2
import numpy as np
import matplotlib.pyplot as plt

# Creamos una imagen en blanco (negro en escala de grises)
img = np.zeros((400, 400, 3), dtype=np.uint8)

# Dibujamos un círculo azul (simulación de objeto)
cv2.circle(img, (200, 200), 100, (255, 0, 0), -1)

# Dibujamos un rectángulo verde
cv2.rectangle(img, (50, 50), (100, 150), (0, 255, 0), -1)

# Dibujamos una línea roja
cv2.line(img, (300, 300), (350, 350), (0, 0, 255), 5)

# Mostramos la imagen
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title("Gráficos por Computador")
plt.axis('off')
plt.show()

