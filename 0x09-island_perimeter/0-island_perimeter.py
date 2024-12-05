#!/usr/bin/python3

def island_perimeter(grid):
    """
    Calculate the perimeter of the island described in the grid.

    Args:
        grid (list of list of int): A rectangular grid where 0 represents water and 1 represents land.

    Returns:
        int: The perimeter of the island.
    """
    rows = len(grid)
    cols = len(grid[0])
    perimeter = 0

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 1:  # Land cell
                # Start with 4 sides
                perimeter += 4

                # Check for adjacent land cells and subtract shared edges
                if row > 0 and grid[row - 1][col] == 1:  # Top
                    perimeter -= 1
                if row < rows - 1 and grid[row + 1][col] == 1:  # Bottom
                    perimeter -= 1
                if col > 0 and grid[row][col - 1] == 1:  # Left
                    perimeter -= 1
                if col < cols - 1 and grid[row][col + 1] == 1:  # Right
                    perimeter -= 1

    return perimeter
