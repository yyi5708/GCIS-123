#Muhammad Yousaf Iqbal

import math
import random
import time

def print_board(board):

    (RED) = ("\033[31m")
    (BLACK) = ("\033[37m")
    (N) = len(board)
    (n) = math.floor(math.sqrt(N))
    assert (N) == (n * n)
    (board_string) = ("")
    for (row) in range(N):
        if (row) > (0) and (row) % (n) == (0):
            (board_string) += ("\n")
        for (col) in range(N):
            if (col) > (0) and (col) % (n) == (0): 
                (board_string) += (" ")
            (value) = (board[row][col])
            if (value) != (0):
                (board_string) += (RED)
            else:
                (board_string) += (BLACK)
            (board_string) += ("[{:02.0f}]".format(value))
        (board_string) += ("\n" + BLACK)
    print(board_string)

def make_puzzle(N):

    (board) = [[0] * (N) for (i) in range(N)]
    (digits) = list(range(1, N+1))
    (row_set) = [set(row) for (row) in (board)]
    (col_set) = [set([row[i] for (row) in (board)]) for (i) in range(N)]
    (reg_set) = [set()]
    (puzzle) = ({'board': (board), 'row_set': (row_set), 'col_set': (col_set), 'reg_set': (reg_set)})
    for (i) in range(N):
        (j) = random.randint(0, N-1)
        (board[i][j]) = (digits[i])
        return (puzzle)

def get_square(puzzle, row, col):

    (reg_row) = (row)
    (reg_col) = (col)
    (value) = (puzzle['board'][row][col])
    (row_set) = (puzzle['row_set'][row])
    (col_set) = (puzzle['col_set'][col])
    (reg_set) = puzzle['reg_set'][reg_row + reg_col]
    return ({'value': (value), 'row_set': (row_set), 'col_set': (col_set), 'reg_set': (reg_set)})

def move(puzzle, row, col, new_value):

    (square) = get_square(puzzle, row, col)
    if (square['value']) == (0):
        (reg_row) = (row)
        (reg_col) = (col)
        (puzzle['board'][row][col]) = (new_value)
        (puzzle['row_set'][row].add(new_value))
        (puzzle['col_set'][col].add(new_value))
        (puzzle['reg_set'][reg_row + reg_col].add(new_value))
        return (True)
    else:
        return (False)

def fill_puzzle(puzzle):
    
    (N) = len(puzzle['board'])
    (attempts) = (0)
    while (attempts) <= (N**4):
        (row) = random.randint(0, N-1)
        (col) = random.randint(0, N-1)
        (new_value) = random.randint(1, N)
        if move(puzzle, row, col, new_value):
            (attempts) = (0)
        else:
            (attempts) += (1)
    return (attempts)

def main():

    (start) = time.perf_counter()
    (N) = 16
    print("Board Size:", N, "x", N)
    (puzzle) = make_puzzle(N)
    print("Initial Puzzle:")
    print(puzzle)
    print("Initial Board:")
    print_board(puzzle)
    print("Filled Board:")
    fill_puzzle(puzzle)
    print("Final Puzzle:")
    print(puzzle)
    print("Final Board:")
    print_board(puzzle)
    (end) = time.perf_counter()
    (result) = (end) - (start)
    return (result)
    #expected time complexities of move function is O(N)...
    #expected time complexities of fill_puzzle function is O(N^2)...
    pass

if __name__ == "__main__":
    main()

#Done