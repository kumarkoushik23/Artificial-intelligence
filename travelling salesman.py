from itertools import permutations

def calculate_total_distance(tour, distances):
    total_distance = 0
    for i in range(len(tour) - 1):
        total_distance += distances[tour[i]][tour[i + 1]]
    total_distance += distances[tour[-1]][tour[0]]  # Return to the starting city
    return total_distance

def traveling_salesman_bruteforce(distances):
    num_cities = len(distances)
    cities = list(range(num_cities))
    min_distance = float('inf')
    best_tour = None

    for tour in permutations(cities):
        distance = calculate_total_distance(tour, distances)
        if distance < min_distance:
            min_distance = distance
            best_tour = tour

    return best_tour, min_distance

# Example Usage
if __name__ == "__main__":
    # Example distances between cities (replace with your own data)
    distances = [
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0]
    ]

    best_tour, min_distance = traveling_salesman_bruteforce(distances)
    print("Best tour:", best_tour)
    print("Minimum distance:", min_distance)
