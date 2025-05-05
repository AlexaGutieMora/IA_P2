# -*- coding: utf-8 -*-
"""
Created on Sun May  4 20:42:08 2025

@author: k
"""

############## 86_ ETIQUETADOS DE LÍNEAS
############ TEMA: PERCEPCIÓN
############ ENFOQUE: PROBABILIDAD (INCERTIDUMBRE)

# Creamos imagen con líneas horizontales y verticales
img = np.zeros((100, 100), dtype=np.uint8)
cv2.line(img, (10, 10), (90, 10), 255, 2)
cv2.line(img, (10, 10), (10, 90), 255, 2)

# Detección de bordes
edges = cv2.Canny(img, 50, 150)

# Detección de líneas con Hough
lines = cv2.HoughLines(edges, 1, np.pi / 180, 50)
img_color = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)

if lines is not None:
    for rho, theta in lines[:, 0]:
        a, b = np.cos(theta), np.sin(theta)
        x0, y0 = a * rho, b * rho
        pt1 = (int(x0 + 1000 * (-b)), int(y0 + 1000 * (a)))
        pt2 = (int(x0 - 1000 * (-b)), int(y0 - 1000 * (a)))
        cv2.line(img_color, pt1, pt2, (0, 0, 255), 1)

plt.imshow(img_color)
plt.title("Detección y Etiquetado de Líneas")
plt.axis('off')
plt.show()
