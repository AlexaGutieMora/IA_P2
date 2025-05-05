# -*- coding: utf-8 -*-
"""
Created on Sun May  4 20:18:15 2025

@author: k
"""

############## 83: DETECCIÓN DE ARISTAS Y SEGMENTACIÓN
############ TEMA: PERCEPCIÓN
############ ENFOQUE: PROBABILIDAD (INCERTIDUMBRE)

import cv2
import matplotlib.pyplot as plt

# Imagen en escala de grises con forma definida
img = np.zeros((200, 200), dtype=np.uint8)
cv2.circle(img, (100, 100), 50, 255, -1)  # Círculo blanco sobre fondo negro

# Detección de aristas con Canny
edges = cv2.Canny(img, 50, 150)

# Segmentación mediante umbral adaptativo
segment = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C,
                                 cv2.THRESH_BINARY, 11, 2)

# Visualización
plt.figure(figsize=(12, 4))
plt.subplot(1, 3, 1), plt.imshow(img, cmap='gray'), plt.title('Original'), plt.axis('off')
plt.subplot(1, 3, 2), plt.imshow(edges, cmap='gray'), plt.title('Canny Edges'), plt.axis('off')
plt.subplot(1, 3, 3), plt.imshow(segment, cmap='gray'), plt.title('Segmentación'), plt.axis('off')
plt.tight_layout()
plt.show()
