# -*- coding: utf-8 -*-
"""
Created on Tue Apr  8 22:53:47 2025

@author: k
"""

##################################### BÚSQUEDA NO INFORMADA

import heapq
import random
import math

################## Grafo de ejemplo y heurísticas 
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

############# Costos reales
costs = {
    ('A', 'B'): 1, ('A', 'C'): 4,
    ('B', 'D'): 2, ('B', 'E'): 5,
    ('C', 'F'): 1,
    ('E', 'F'): 1
}

##### Heurísticas (estimación del costo desde un nodo hasta el objetivo)
############## HEURÍSTICAS
heuristic = {
    'A': 6,
    'B': 4,
    'C': 4,
    'D': 2,
    'E': 1,
    'F': 0
}

############## BÚSQUEDA VORAZ PRIMERO EL MEJOR
def greedy_best_first(start, goal):
    frontier = [(heuristic[start], [start])]
    visited = set()

    while frontier:
        _, path = heapq.heappop(frontier)
        node = path[-1]

        if node == goal:
            return path

        if node not in visited:
            visited.add(node)
            for neighbor in graph.get(node, []):
                new_path = list(path)
                new_path.append(neighbor)
                heapq.heappush(frontier, (heuristic[neighbor], new_path))

############## BÚSQUEDA A*
def a_star(start, goal):
    frontier = [(heuristic[start], 0, [start])]
    visited = set()

    while frontier:
        est_total, cost_so_far, path = heapq.heappop(frontier)
        node = path[-1]

        if node == goal:
            return path, cost_so_far

        if node not in visited:
            visited.add(node)
            for neighbor in graph.get(node, []):
                new_cost = cost_so_far + costs.get((node, neighbor), 1)
                est = new_cost + heuristic[neighbor]
                new_path = list(path)
                new_path.append(neighbor)
                heapq.heappush(frontier, (est, new_cost, new_path))

############## BÚSQUEDA AO* (simplificada)
# Nota: AO* es para grafos AND-OR y requiere estructuras más complejas.
# Aquí se da una simulación básica orientada a mostrar el flujo.
def ao_star(start, goal):
    print(f"AO* (simulado): camino desde {start} hasta {goal}")
    return a_star(start, goal)  # Usamos A* como base para la estructura

############### BÚSQUEDA DE ASCENSIÓN DE COLINAS
def hill_climbing(start, goal):
    current = start
    path = [current]

    while current != goal:
        neighbors = graph.get(current, [])
        if not neighbors:
            return None
        current = min(neighbors, key=lambda x: heuristic[x])
        path.append(current)
        if heuristic[current] >= heuristic[path[-2]]:
            return None  # Estancado
    return path

############## BÚSQUEDA TABÚ 
def tabu_search(start, goal, max_iter=10, tabu_size=3):
    current = start
    tabu_list = [current]
    path = [current]

    for _ in range(max_iter):
        neighbors = graph.get(current, [])
        candidates = [n for n in neighbors if n not in tabu_list]
        if not candidates:
            return None
        next_node = min(candidates, key=lambda x: heuristic[x])
        tabu_list.append(next_node)
        if len(tabu_list) > tabu_size:
            tabu_list.pop(0)
        path.append(next_node)
        current = next_node
        if current == goal:
            return path
    return None

############## BÚSQUEDA DE TEMPLE SIMULADO
def simulated_annealing(start, goal, temp=1000, cooling=0.95):
    current = start
    path = [current]

    while temp > 1:
        neighbors = graph.get(current, [])
        if not neighbors:
            return None
        next_node = random.choice(neighbors)
        delta = heuristic[current] - heuristic[next_node]

        if delta > 0 or random.random() < math.exp(delta / temp):
            current = next_node
            path.append(current)
            if current == goal:
                return path

        temp *= cooling
    return None

############## BÚSQUEDA DE HAZ LOCAL
def local_beam_search(start, goal, beam_width=2):
    states = [[start]]
    while states:
        new_states = []
        for path in states:
            current = path[-1]
            if current == goal:
                return path
            for neighbor in graph.get(current, []):
                new_path = list(path)
                new_path.append(neighbor)
                new_states.append(new_path)
        states = sorted(new_states, key=lambda p: heuristic[p[-1]])[:beam_width]
    return None

############## ALGORITMOS GENÉTICOS
def genetic_search(start, goal, population_size=6, generations=10):
    def fitness(path):
        if path[-1] != goal:
            return float('inf')
        return sum(heuristic[n] for n in path)

    def mutate(path):
        if len(path) < 2:
            return path
        idx = random.randint(0, len(path)-2)
        next_steps = graph.get(path[idx], [])
        if next_steps:
            return path[:idx+1] + [random.choice(next_steps)]
        return path

    population = [[start] for _ in range(population_size)]

    for _ in range(generations):
        for i in range(len(population)):
            while population[i][-1] != goal:
                next_nodes = graph.get(population[i][-1], [])
                if not next_nodes:
                    break
                population[i].append(random.choice(next_nodes))
        population.sort(key=fitness)
        if population[0][-1] == goal:
            return population[0]
        population = population[:population_size//2]
        population += [mutate(p) for p in population]
    return None

############## BÚSQUEDA ONLINE (reacción sin conocimiento previo)
def online_search(start, goal):
    current = start
    path = [current]
    visited = set([current])

    while current != goal:
        neighbors = [n for n in graph.get(current, []) if n not in visited]
        if not neighbors:
            return None
        next_node = min(neighbors, key=lambda x: heuristic[x])
        visited.add(next_node)
        path.append(next_node)
        current = next_node
    return path


print("Greedy:", greedy_best_first('A', 'F'))  # Búsqueda voraz (primero el mejor)
print("A*:", a_star('A', 'F'))  # Búsqueda A*
print("AO*:", ao_star('A', 'F'))  # Búsqueda AO* (simulada)
print("Hill Climbing:", hill_climbing('A', 'F'))  # Ascensión de colinas
print("Tabu Search:", tabu_search('A', 'F'))  # Búsqueda tabú
print("Simulated Annealing:", simulated_annealing('A', 'F'))  # Temple simulado
print("Local Beam:", local_beam_search('A', 'F'))  # Búsqueda de haz local
print("Genetic Algorithm:", genetic_search('A', 'F'))  # Algoritmo genético
print("Online Search:", online_search('A', 'F'))  # Búsqueda online
