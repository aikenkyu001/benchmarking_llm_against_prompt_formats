import random

def solve_puzzle(board):
    if len(board) == 0:
        return True

    for i in range(len(board)):
        row = board[i]
        if not is_valid_move(row, board):
            return False

    return True

def is_valid_move(row, board):
    if row < len(board) and board[row][0] == 1:
        return False
    elif row > 0 and board[row - 1][0] == 2:
        return False
    elif row + 1 < len(board) and board[row + 1][0] == 3:
        return False
    else:
        return True