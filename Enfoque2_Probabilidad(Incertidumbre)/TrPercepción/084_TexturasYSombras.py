# -*- coding: utf-8 -*-
"""
Created on Sun May  4 20:29:21 2025

@author: k
"""

############## 84: TEXTURAS Y SOMBRAS
############ TEMA: PERCEPCIÓN
############ ENFOQUE: PROBABILIDAD (INCERTIDUMBRE)


# Creamos una imagen con gradientes simulando sombras
img = np.tile(np.linspace(0, 255, 200, dtype=np.uint8), (200, 1))

# Filtro Sobel para detectar gradientes (cambios de textura)
sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)
sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)
gradient = np.sqrt(sobelx**2 + sobely**2)

# Visualización
plt.figure(figsize=(10, 4))
plt.subplot(1, 2, 1), plt.imshow(img, cmap='gray'), plt.title('Simulación de sombra'), plt.axis('off')
plt.subplot(1, 2, 2), plt.imshow(gradient, cmap='hot'), plt.title('Mapa de textura (gradiente)'), plt.axis('off')
plt.tight_layout()
plt.show()
