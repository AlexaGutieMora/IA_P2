# -*- coding: utf-8 -*-
"""
Created on Sun May  4 20:32:46 2025

@author: k
"""
############## 85: RECONOCIMIENTO DE ESCRITURA
############ TEMA: PERCEPCIÓN
############ ENFOQUE: PROBABILIDAD (INCERTIDUMBRE)

import pytesseract
from PIL import Image, ImageDraw, ImageFont

# Creamos una imagen con texto
img = Image.new('RGB', (200, 100), color=(255, 255, 255))
draw = ImageDraw.Draw(img)
draw.text((10, 40), "Hola", fill=(0, 0, 0))

# Convertimos para OCR
text_detected = pytesseract.image_to_string(img, lang='spa')

plt.imshow(img)
plt.title(f"Texto detectado: {text_detected.strip()}")
plt.axis('off')
plt.show()
