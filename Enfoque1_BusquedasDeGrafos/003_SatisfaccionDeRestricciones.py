# -*- coding: utf-8 -*-
"""
Created on Mon Apr 28 19:22:12 2025

@author: k
"""

from collections import defaultdict
import random

############################ VARIABLES DEL PROBLEMA

variables = ['A', 'B', 'C', 'D', 'E']
domains = {
    var: ['Rojo', 'Verde', 'Azul'] for var in variables
}

# Adyacencias del grafo (restricciones binarias: no puede haber mismo color)
neighbors = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D', 'E'],
    'D': ['B', 'C', 'E'],
    'E': ['C', 'D']
}

############ RESTRICCIÓN BINARIA
def constraint(var1, val1, var2, val2):
    return val1 != val2

############ VUELTA ATRÁS 
def backtracking(assignment):
    if len(assignment) == len(variables):
        return assignment

    var = select_unassigned_variable(assignment)
    for value in domains[var]:
        if is_consistent(var, value, assignment):
            assignment[var] = value
            result = backtracking(assignment)
            if result:
                return result
            del assignment[var]
    return None

############# COMPROBACIÓN HACIA ADELANTE 
def forward_checking(assignment, domains_copy):
    if len(assignment) == len(variables):
        return assignment

    var = select_unassigned_variable(assignment)
    for value in domains_copy[var]:
        if is_consistent(var, value, assignment):
            assignment[var] = value
            local_domains = deepcopy(domains_copy)
            if not forward_check(var, value, local_domains, assignment):
                del assignment[var]
                continue
            result = forward_checking(assignment, local_domains)
            if result:
                return result
            del assignment[var]
    return None

def forward_check(var, value, local_domains, assignment):
    for neighbor in neighbors[var]:
        if neighbor not in assignment:
            if value in local_domains[neighbor]:
                local_domains[neighbor].remove(value)
            if not local_domains[neighbor]:
                return False
    return True

############# PROPAGACIÓN DE RESTRICCIONES (AC-3)
def ac3(domains_input):
    queue = [(xi, xj) for xi in variables for xj in neighbors[xi]]
    while queue:
        xi, xj = queue.pop(0)
        if revise(domains_input, xi, xj):
            if not domains_input[xi]:
                return False
            for xk in neighbors[xi]:
                if xk != xj:
                    queue.append((xk, xi))
    return True

def revise(domains_input, xi, xj):
    revised = False
    for x in domains_input[xi][:]:
        if not any(x != y for y in domains_input[xj]):
            domains_input[xi].remove(x)
            revised = True
    return revised

############ SALTO ATRÁS DIRIGIDO POR CONFLICTOS 
def conflict_directed_backjumping(assignment, conflicts={}):
    if len(assignment) == len(variables):
        return assignment

    var = select_unassigned_variable(assignment)
    for value in domains[var]:
        if is_consistent(var, value, assignment):
            assignment[var] = value
            result = conflict_directed_backjumping(assignment, conflicts)
            if result:
                return result
            del assignment[var]
        else:
            conflicts[var] = conflicts.get(var, set()) | {var}
    return None

############ MÍNIMOS-CONFLICTOS (BÚSQUEDA LOCAL)
def min_conflicts(max_steps=1000):
    current = {var: random.choice(domains[var]) for var in variables}

    for _ in range(max_steps):
        conflicted = [var for var in variables if not is_consistent_all(var, current[var], current)]
        if not conflicted:
            return current
        var = random.choice(conflicted)
        value = min(domains[var], key=lambda val: count_conflicts(var, val, current))
        current[var] = value
    return None

############ ACONDICIONAMIENTO DEL CORTE (CSP REDUCIDO)
def cutset_conditioning():
    cutset = ['C']  # nodo a condicionar
    solutions = []

    for value in domains['C']:
        partial_assignment = {'C': value}
        reduced_domains = deepcopy(domains)
        reduced_domains['C'] = [value]
        ac3(reduced_domains)
        result = backtracking(partial_assignment)
        if result:
            solutions.append(result)
    return solutions

############ FUNCIONES AUXILIARES 
def is_consistent(var, value, assignment):
    return all(constraint(var, value, neighbor, assignment[neighbor])
               for neighbor in neighbors[var]
               if neighbor in assignment)

def is_consistent_all(var, value, assignment):
    for neighbor in neighbors[var]:
        if neighbor in assignment and assignment[neighbor] == value:
            return False
    return True

def count_conflicts(var, value, assignment):
    return sum(1 for neighbor in neighbors[var]
               if neighbor in assignment and assignment[neighbor] == value)

def select_unassigned_variable(assignment):
    for var in variables:
        if var not in assignment:
            return var

from copy import deepcopy

############ PRUEBAS 
print("Vuelta Atrás:", backtracking({}))  # Búsqueda de vuelta atrás

print("Comprobación hacia Adelante:", forward_checking({}, deepcopy(domains)))  # Forward Checking

dom_copy = deepcopy(domains)
print("Propagación de Restricciones (AC-3):", ac3(dom_copy), dom_copy)  # AC-3

print("Salto Atrás Dirigido por Conflictos:", conflict_directed_backjumping({}))  # CBJ

print("Mínimos Conflictos (Local):", min_conflicts())  # Búsqueda local

print("Acondicionamiento del Corte:", cutset_conditioning())  # Cutset Conditioning
