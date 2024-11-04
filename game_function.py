import random

def grid_init():
    """Initializes a 4x4 game grid filled with zeros, representing empty cells."""
    return [[0] * 4 for _ in range(4)]

def grid_display(grid):
    """Displays the game grid in a readable format, replacing zeros with dots."""
    for row in grid:
        row_str_list = []
        for num in row:
            if num != 0:
                row_str_list.append(str(num))
            else:
                row_str_list.append('.')
        row_str = "\t".join(row_str_list)
        print(row_str)
        print()

def add_new_tile(grid):
    """Finding the empty cells (if available) and adding new tile (2) randomly in the grid."""
    empty_cells = [(i, j) for i in range(4) for j in range(4) if grid[i][j] == 0]
    if empty_cells != []:
        i, j = random.choice(empty_cells)
        grid[i][j] = 2
    else:
        return

def merge(line):
    """
    Merges a line (row or column) by sliding non-zero numbers to the left and combining adjacent equal values. 
    Returns the merged line and a boolean indicating if any merge occurred.
    """
    new_line = [num for num in line if num != 0]
    combined_line = []
    i = 0

    while i < len(new_line) - 1:
        if new_line[i] == new_line[i + 1]:
            combined_line.append(new_line[i] * 2)
            new_line[i], new_line[i + 1] = 0, 0
            i += 2
        else:
            combined_line.append(new_line[i])
            i += 1
    
    if i < len(new_line):
        combined_line.append(new_line[i])
    combined_line.extend([0] * (4 - len(combined_line)))

    return combined_line, combined_line != line

def move(grid, direction):
    """
    Moves tiles in the specified direction ('w', 's', 'a', or 'd') and merges tiles.
    Returns a boolean indicating if the grid changed.
    """
    moved = False
    if direction == 'w':
        for j in range(4):
            column = []
            for i in range(4):
                column.append(grid[i][j])
            new_column, combined_or_not = merge(column)
            if combined_or_not:
                moved = True
            for i in range(4):
                grid[i][j] = new_column[i]
    
    elif direction == 's':
        for j in range(4):
            column = []
            for i in range(3, -1, -1):
                column.append(grid[i][j])
            new_column, combined_or_not = merge(column)
            if combined_or_not:
                moved = True
            for i in range(4):
                grid[3 - i][j] = new_column[i]

    elif direction == 'a':
        for i in range(4):
            row = grid[i]
            new_row, combined_or_not = merge(row)
            if combined_or_not:
                moved = True
            grid[i] = new_row
    
    elif direction == 'd':
        for i in range(4):
            row = grid[i][::-1]
            new_row, combined_or_not = merge(row)
            if combined_or_not:
                moved = True
            grid[i] = new_row[::-1]
    
    return moved

def check_win(grid):
    """Checks if any cell in the grid has the winning value (2048)."""
    return any(2048 in row for row in grid)

def check_game_over(grid):
    """
    Checks if no valid moves are available. 
    Returns True if the game is over, otherwise returns False.
    """
    for i in range(4):
        for j in range(4):
            if grid[i][j] == 0:
                return False
            if j < 3 and grid[i][j] == grid[i][j + 1]:
                return False
            if i < 3 and grid[i][j] == grid[i + 1][j]:
                return False
    return True