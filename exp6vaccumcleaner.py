class VacuumCleaner:
    def __init__(self, grid):
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0])
        self.visited = set()

    def clean(self, row, col):
        if (row, col) in self.visited:
            return
        self.visited.add((row, col))
        print(f"Cleaning cell ({row}, {col})")

    def move(self, row, col):
        if row >= 0 and row < self.rows and col >= 0 and col < self.cols and self.grid[row][col] == "dirty":
            self.clean(row, col)
            self.grid[row][col] = "clean"
        else:
            return

        # Move to adjacent cells
        self.move(row + 1, col)  # Move down
        self.move(row - 1, col)  # Move up
        self.move(row, col + 1)  # Move right
        self.move(row, col - 1)  # Move left

    def clean_all(self):
        for i in range(self.rows):
            for j in range(self.cols):
                if self.grid[i][j] == "dirty":
                    self.move(i, j)

# Example grid
grid = [
    ["clean", "dirty", "clean"],
    ["clean", "clean", "dirty"],
    ["dirty", "clean", "clean"]
]

# Create a vacuum cleaner instance and clean the grid
vacuum = VacuumCleaner(grid)
vacuum.clean_all()
