import heapq

class PuzzleNode:
    def __init__(self, state, parent=None, action=None, cost=0):
        self.state = state
        self.parent = parent
        self.action = action
        self.cost = cost
        self.heuristic = self.calculate_heuristic()

    def __lt__(self, other):
        return (self.cost + self.heuristic) < (other.cost + other.heuristic)

    def calculate_heuristic(self):
        # Manhatten distance heuristic
        total_distance = 0
        for i in range(3):
            for j in range(3):
                if self.state[i][j] != 0:
                    goal_row, goal_col = divmod(self.state[i][j] - 1, 3)
                    total_distance += abs(i - goal_row) + abs(j - goal_col)
        return total_distance

    def get_neighbors(self):
        neighbors = []
        zero_row, zero_col = self.find_zero_position()

        for move in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            new_row, new_col = zero_row + move[0], zero_col + move[1]

            if 0 <= new_row < 3 and 0 <= new_col < 3:
                new_state = [row[:] for row in self.state]
                new_state[zero_row][zero_col], new_state[new_row][new_col] = new_state[new_row][new_col], new_state[zero_row][zero_col]
                neighbors.append(PuzzleNode(new_state, self, move, self.cost + 1))

        return neighbors

    def find_zero_position(self):
        for i in range(3):
            for j in range(3):
                if self.state[i][j] == 0:
                    return i, j

def print_solution(node):
    actions = []
    while node.parent is not None:
        actions.append(node.action)
        node = node.parent
    actions.reverse()

    for action in actions:
        print(action)

def solve_puzzle(initial_state):
    initial_node = PuzzleNode(initial_state)
    heap = [initial_node]
    visited = set()

    while heap:
        current_node = heapq.heappop(heap)

        if current_node.state == [[1, 2, 3], [4, 5, 6], [7, 8, 0]]:
            print("Solution found!")
            print_solution(current_node)
            return

        visited.add(tuple(map(tuple, current_node.state)))

        for neighbor in current_node.get_neighbors():
            if tuple(map(tuple, neighbor.state)) not in visited:
                heapq.heappush(heap, neighbor)
                visited.add(tuple(map(tuple, neighbor.state)))

    print("No solution found.")

# Example usage:
initial_state = [[1, 2, 3], [4, 0, 5], [7, 8, 6]]
solve_puzzle(initial_state)
