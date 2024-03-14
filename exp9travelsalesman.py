import itertools
import math

def tsp(cities, distances):
    n = len(cities)
    all_cities = set(range(n))

        .....# Initialize memoization table
    memo = {}

    # Base case: starting from city 0 to any other city
    for j in range(1, n):
        memo[(frozenset([0, j]), j)] = (distances[0][j], 0)

    # Dynamic programming to compute shortest paths
    for size in range(2, n):
        for subset in itertools.combinations(all_cities - {0}, size):
            subset = frozenset(subset) | {0}
            for j in subset - {0}:
                memo[(subset, j)] = min(
                    (memo[(subset - {j}, k)][0] + distances[k][j], k)
                    for k in subset if k != j
                )

    # Find the shortest path from the last city back to city 0
    min_dist, last_city = min(
        (memo[(all_cities, k)][0] + distances[k][0], k)
        for k in range(1, n)
    )

    # Reconstruct the path
    path = [0]
    current_set = all_cities - {0}
    while len(path) < n:
        path.append(last_city)
        current_set -= {last_city}
        _, last_city = memo[(current_set, last_city)]

    path.append(0)  # Return to starting city
    return path

# Example cities and distances
cities = ["A", "B", "C", "D"]
distances = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

# Solve TSP
shortest_path = tsp(cities, distances)
print("Shortest path:", shortest_path)
