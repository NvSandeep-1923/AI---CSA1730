# Travelling Salesman Problem using Brute Force

import itertools

def calculate_distance(city1, city2):
    return ((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2) ** 0.5

def total_distance(route, cities):
    distance = 0
    for i in range(len(route) - 1):
        distance += calculate_distance(cities[route[i]], cities[route[i + 1]])
    distance += calculate_distance(cities[route[-1]], cities[route[0]])  # Return to starting city
    return distance

def travelling_salesman(cities):
    n = len(cities)
    min_route = None
    min_distance = float('inf')
    
    for perm in itertools.permutations(range(n)):
        current_distance = total_distance(perm, cities)
        if current_distance < min_distance:
            min_distance = current_distance
            min_route = perm
            
    return min_route, min_distance

# Example usage
cities = [(0, 0), (1, 2), (2, 4), (3, 1)]
route, distance = travelling_salesman(cities)
print("Optimal route:", route)
print("Minimum distance:", distance)
