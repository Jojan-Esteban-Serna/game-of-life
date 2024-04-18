class WorldBoard:

    def __init__(self, num_rows, num_cols):
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.world = [[False] * num_cols for _ in range(num_rows)]

    def toggle_cell(self, row, col):
        self.world[row][col] = not self.world[row][col]

    def is_cell_alive(self, row, col):
        return self.world[row][col]

    def reset(self):
        self.world = [[False] * self.num_cols for _ in range(self.num_rows)]

    def step(self):
        new_world = [[False] * self.num_cols for _ in range(self.num_rows)]

        for row in range(self.num_rows):
            for col in range(self.num_cols):
                neighbors = self.count_neighbors(row, col)
                # Caso de supervivencia(true) y muerte por soledad o sobrepoblacion(false)
                # Caso de nacimiento
                new_world[row][col] = (neighbors == 2 or neighbors == 3) if self.world[row][col] else (neighbors == 3)

        self.world = new_world

    def count_neighbors(self, row, col):
        relative_indexes = [-1, 0, 1]
        count = 0
        for row_relative_index in relative_indexes:
            for col_relative_index in relative_indexes:
                if (row_relative_index, col_relative_index) != (0, 0):
                    absolute_row_index = (row + row_relative_index + self.num_rows) % self.num_rows
                    absolute_col_index = (col + col_relative_index + self.num_cols) % self.num_cols
                    if self.world[absolute_row_index][absolute_col_index]:
                        count += 1

        return count
