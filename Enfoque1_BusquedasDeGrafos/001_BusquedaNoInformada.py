# -*- coding: utf-8 -*-
"""
Created on Tue Apr  1 22:27:29 2025

@author: k
"""

################PLANIFICACIÓN
#### BÚSQUEDA NO INFORMADA
from collections import deque
import heapq

# Estructura de grafo para pruebas
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# Costos para búsqueda de costo uniforme
costs = {
    ('A', 'B'): 1, ('A', 'C'): 4,
    ('B', 'D'): 5, ('B', 'E'): 2,
    ('C', 'F'): 1,
    ('E', 'F'): 3
}

################  BÚSQUEDA EN ANCHURA (BFS) 
def bfs(start, goal):
    queue = deque([[start]])
    visited = set()
    
    while queue:
        path = queue.popleft()
        node = path[-1]

        if node == goal:
            return path
        
        if node not in visited:
            visited.add(node)
            for neighbor in graph.get(node, []):
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)

################  BÚSQUEDA DE COSTO UNIFORME
def uniform_cost_search(start, goal):
    queue = [(0, [start])]
    visited = set()

    while queue:
        cost, path = heapq.heappop(queue)
        node = path[-1]

        if node == goal:
            return path, cost
        
        if node not in visited:
            visited.add(node)
            for neighbor in graph.get(node, []):
                total_cost = cost + costs.get((node, neighbor), 1)
                new_path = list(path)
                new_path.append(neighbor)
                heapq.heappush(queue, (total_cost, new_path))

################  BÚSQUEDA EN PROFUNDIDAD (DFS)
def dfs(start, goal, visited=None, path=None):
    if visited is None:
        visited = set()
    if path is None:
        path = []

    visited.add(start)
    path = path + [start]

    if start == goal:
        return path

    for neighbor in graph.get(start, []):
        if neighbor not in visited:
            result = dfs(neighbor, goal, visited, path)
            if result:
                return result

################  BÚSQUEDA EN PROFUNDIDAD LIMITADA 
def dls(start, goal, limit):
    def recursive_dls(node, goal, limit, path, visited):
        if node == goal:
            return path
        if limit <= 0:
            return None
        visited.add(node)
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                result = recursive_dls(neighbor, goal, limit - 1, path + [neighbor], visited)
                if result:
                    return result
        return None

    return recursive_dls(start, goal, limit, [start], set())

################  BÚSQUEDA EN PROFUNDIDAD ITERATIVA
def ids(start, goal, max_depth):
    for depth in range(max_depth + 1):
        result = dls(start, goal, depth)
        if result:
            return result

################  BÚSQUEDA BIDIRECCIONAL
def bidirectional_search(start, goal):
    if start == goal:
        return [start]

    front = {start: [start]}
    back = {goal: [goal]}
    frontier_front = deque([start])
    frontier_back = deque([goal])

    while frontier_front and frontier_back:
        node_front = frontier_front.popleft()
        for neighbor in graph.get(node_front, []):
            if neighbor not in front:
                front[neighbor] = front[node_front] + [neighbor]
                frontier_front.append(neighbor)
                if neighbor in back:
                    return front[neighbor] + back[neighbor][::-1][1:]

        node_back = frontier_back.popleft()
        for neighbor in graph.get(node_back, []):
            if neighbor not in back:
                back[neighbor] = back[node_back] + [neighbor]
                frontier_back.append(neighbor)
                if neighbor in front:
                    return front[neighbor] + back[neighbor][::-1][1:]
    return None

############### BÚSQUEDA EN GRAFOS 
def graph_search(start, goal):
    frontier = deque([[start]])
    explored = set()

    while frontier:
        path = frontier.popleft()
        node = path[-1]
        if node == goal:
            return path
        if node not in explored:
            explored.add(node)
            for neighbor in graph.get(node, []):
                new_path = list(path)
                new_path.append(neighbor)
                frontier.append(new_path)

############### PRUEBAS
print("Anchura:", bfs('A', 'F'))  # Búsqueda en Anchura
print("Costo Uniforme:", uniform_cost_search('A', 'F'))  # Búsqueda en Anchura de Costo Uniforme
print("Profundidad:", dfs('A', 'F'))  # Búsqueda en Profundidad
print("Profundidad Limitada (lim=2):", dls('A', 'F', 2))  # Búsqueda en Profundidad Limitada
print("Profundidad Iterativa (max=5):", ids('A', 'F', 5))  # Búsqueda en Profundidad Iterativa
print("Bidireccional:", bidirectional_search('A', 'F'))  # Búsqueda Bidireccional
print("Búsqueda en Grafos:", graph_search('A', 'F'))  # Búsqueda en Grafos
