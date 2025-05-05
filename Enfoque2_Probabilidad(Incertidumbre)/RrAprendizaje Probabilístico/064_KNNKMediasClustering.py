# -*- coding: utf-8 -*-
"""
Created on Sun May  4 16:47:12 2025

@author: k
"""

############## 64: K-NN, K-MEDIAS Y CLUSTERING
############ TEMA: APRENDIZAJE PROBABILÍSTICO 
############ ENFOQUE: PROBABILIDAD (INCERTIDUMBRE)

from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt

# Creamos datos artificiales
X, y = make_blobs(n_samples=300, centers=3, cluster_std=0.5, random_state=0)

# Clustering con KMeans
kmeans = KMeans(n_clusters=3, random_state=0).fit(X)

# Clasificación con k-NN
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X, kmeans.labels_)  # usamos los clusters como etiquetas

# Clasificamos un nuevo punto
nuevo = [[2, 2]]
print("Etiqueta estimada por k-NN:", knn.predict(nuevo))

# Visualización
plt.scatter(X[:, 0], X[:, 1], c=kmeans.labels_, cmap='viridis')
plt.scatter(nuevo[0][0], nuevo[0][1], c='red', marker='X', s=200)
plt.title("k-Means + k-NN")
plt.show()
