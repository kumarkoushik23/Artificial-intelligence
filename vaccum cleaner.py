import random

class VacuumCleaner:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.grid = [[0] * cols for _ in range(rows)]  # Initialize a grid with all cells set to 0 (no dirt)
        self.position = (random.randint(0, rows-1), random.randint(0, cols-1))  # Random initial position
        self.directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # Possible movement directions

    def place_dirt(self, num_dirt):
        for _ in range(num_dirt):
            row, col = random.randint(0, self.rows-1), random.randint(0, self.cols-1)
            self.grid[row][col] = 1  # Place dirt in a random cell

    def print_grid(self):
        for row in self.grid:
            print(row)
        print()

    def clean(self):
        steps = 0
        while any(1 in row for row in self.grid):  # Continue cleaning until there is no more dirt
            self.print_grid()
            self.clean_current_cell()
            self.move()
            steps += 1
        print(f"Cleaning completed in {steps} steps.")

    def clean_current_cell(self):
        row, col = self.position
        if self.grid[row][col] == 1:
            print(f"Cleaning dirt at ({row}, {col})")
            self.grid[row][col] = 0  # Clean the dirt

    def move(self):
        row, col = self.position
        direction = random.choice(self.directions)
        new_row, new_col = row + direction[0], col + direction[1]
        if 0 <= new_row < self.rows and 0 <= new_col < self.cols:
            print(f"Moving from ({row}, {col}) to ({new_row}, {new_col})")
            self.position = (new_row, new_col)
        else:
            print("Cannot move in that direction, staying in the same position.")

# Example Usage
rows = 5
cols = 5
num_dirt = 5

vacuum = VacuumCleaner(rows, cols)
vacuum.place_dirt(num_dirt)
vacuum.clean()
