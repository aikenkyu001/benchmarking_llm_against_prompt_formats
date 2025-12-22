def solve_puzzle(grid, start_row, start_col, end_row, end_col):
    if grid[start_row][start_col] != 0:
        return

    if grid[end_row][end_col] == 1 and grid[start_row][start_col] == 2:
        solve_puzzle(grid, start_row, start_col, end_row, end_col)
    elif grid[end_row][end_col] == 0:
        if grid[start_row][start_col] != 1 and grid[end_row][end_col] == 2:
            solve_puzzle(grid, start_row, start_col, end_row, end_col)
    else:
        solve_puzzle(grid, start_row, start_col, end_row, end_col)

def solve_puzzle(grid, row, col, end_row, end_col):
    if grid[end_row][end_col] == 0:
        return

    if grid[end_row][end_col] == 1 and grid[row][col] == 2:
        solve_puzzle(grid, row, col, end_row, end_col)
    elif grid[end_row][end_col] == 0:
        if grid[row][col] != 1 and grid[end_row][col] == 2:
            solve_puzzle(grid, row, col, end_row, end_col)

def main():
    grid = [[0, 0, 0, 0],
         [0, 0, 0, 0],
         [0, 1, 0, 0],
         [0, 0, 0, 0]]

    start_row = 0
    start_col = 0
    end_row = 3
    end_col = 2
    solve_puzzle(grid, start_row, start_col, end_row, end_col)

if __name__ == '__main__':
    main()