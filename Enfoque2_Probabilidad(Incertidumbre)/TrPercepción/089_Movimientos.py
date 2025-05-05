# -*- coding: utf-8 -*-
"""
Created on Sun May  4 20:50:58 2025

@author: k
"""
############## 86: MOVIMIENTOS
############ TEMA: PERCEPCIÓN
############ ENFOQUE: PROBABILIDAD (INCERTIDUMBRE)
# Creamos dos imágenes: una figura cambia de posición
img1 = np.zeros((100, 100), dtype=np.uint8)
cv2.circle(img1, (30, 50), 10, 255, -1)

img2 = np.zeros((100, 100), dtype=np.uint8)
cv2.circle(img2, (50, 50), 10, 255, -1)

# Restamos imágenes para detectar movimiento
motion = cv2.absdiff(img1, img2)

# Visualización
plt.figure(figsize=(10, 3))
plt.subplot(1, 3, 1), plt.imshow(img1, cmap='gray'), plt.title('Cuadro 1'), plt.axis('off')
plt.subplot(1, 3, 2), plt.imshow(img2, cmap='gray'), plt.title('Cuadro 2'), plt.axis('off')
plt.subplot(1, 3, 3), plt.imshow(motion, cmap='hot'), plt.title('Detección de movimiento'), plt.axis('off')
plt.tight_layout()
plt.show()
