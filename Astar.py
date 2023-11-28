import heapq

class Node:
    def __init__(self, position, parent=None):
        self.position = position
        self.parent = parent
        self.g = 0  # Cost from start node to current node
        self.h = 0  # Heuristic (estimated cost from current node to goal)
        self.f = 0  # Total cost (g + h)

    def __lt__(self, other):
        return self.f < other.f

def astar(grid, start, goal):
    rows, cols = len(grid), len(grid[0])
    open_set = []  # Priority queue to store open nodes
    closed_set = set()  # Set to store closed nodes

    start_node = Node(start)
    goal_node = Node(goal)

    heapq.heappush(open_set, start_node)

    while open_set:
        current_node = heapq.heappop(open_set)
        closed_set.add(current_node.position)

        if current_node.position == goal_node.position:
            path = []
            while current_node:
                path.append(current_node.position)
                current_node = current_node.parent
            return path[::-1]

        neighbors = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # Possible movement directions (up, down, right, left)
        for neighbor in neighbors:
            new_position = (current_node.position[0] + neighbor[0], current_node.position[1] + neighbor[1])

            if (
                0 <= new_position[0] < rows
                and 0 <= new_position[1] < cols
                and grid[new_position[0]][new_position[1]] == 0
                and new_position not in closed_set
            ):
                neighbor_node = Node(new_position, current_node)
                neighbor_node.g = current_node.g + 1
                neighbor_node.h = abs(new_position[0] - goal_node.position[0]) + abs(new_position[1] - goal_node.position[1])
                neighbor_node.f = neighbor_node.g + neighbor_node.h

                if neighbor_node not in open_set:
                    heapq.heappush(open_set, neighbor_node)

    return None  # No path found

# Example Usage
if __name__ == "__main__":
    # Example grid (0 represents a walkable path, 1 represents an obstacle)
    example_grid = [
        [0, 0, 0, 0, 0],
        [0, 1, 1, 0, 0],
        [0, 0, 0, 1, 0],
        [0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0],
    ]

    start_position = (0, 0)
    goal_position = (4, 4)

    path = astar(example_grid, start_position, goal_position)

    if path:
        print(f"A* Path from {start_position} to {goal_position}: {path}")
    else:
        print("No path found.")
