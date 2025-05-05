# -*- coding: utf-8 -*-
"""
Created on Sun May  4 20:31:11 2025

@author: k
"""

############## 85: RECONOCIMIENTO DE OBJETOS
############ TEMA: PERCEPCIÓN
############ ENFOQUE: PROBABILIDAD (INCERTIDUMBRE)

# Imagen con formas
img = np.zeros((300, 300), dtype=np.uint8)
cv2.rectangle(img, (50, 50), (150, 150), 255, -1)
cv2.circle(img, (220, 220), 40, 255, -1)

# Detección de contornos (objetos)
contours, _ = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Dibujamos los contornos sobre una copia
img_rgb = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
cv2.drawContours(img_rgb, contours, -1, (0, 255, 0), 2)

plt.imshow(img_rgb)
plt.title("Reconocimiento de Objetos")
plt.axis('off')
plt.show()
