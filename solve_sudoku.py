def solve_sudoku(board):
    empty_cell = find_empty_cell(board)
    if not empty_cell:
        return board