grid = [ ["-", "-", "-", "#", "#"],
         ["-", "#", "-", "-", "-"],
         ["-", "-", "#", "-", "-"],
         ["-", "#", "#", "-", "-"],
         ["-", "-", "-", "-", "-"] ]

def new_value_grid(grid):
    rows = len(grid)
    cols = len(grid[0])
    new_grid = [[" " for _ in range(cols)] for _ in range(rows)]

    directions = [
        (-1, -1), (-1, 0), (-1, 1), 
        ( 0, -1), ( 0, 1),
        ( 1, -1), ( 1, 0), ( 1, 1) 
                ]

    for row, row_list in enumerate(grid):
        for col, cell in enumerate(row_list):
            if cell == "#":
                new_grid[row][col] = "#"