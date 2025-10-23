def is_valid_move(board, row: int, column: int, n: int) -> bool:
    """ Check if placing n in board[row][column] is a valid move. """

    # Check for row
    if n in board[row]:
        return False

    # Check column
    if n in [r[column] for r in board]:
        return False

    # Check square
    r_n = (row // 3) * 3
    c_n = (column // 3) * 3
    square = [[c for c in r[c_n:c_n + 3]] for r in board[r_n:r_n + 3]]
    if n in square[0] + square[1] + square[2]:
        return False
    return True


def get_empty_positions(board) -> list[tuple[int]]:
    """ Returns a list of empty positions on the board. """
    empty = []
    for row in range(9):
        for column in range(9):
            if not board[row][column]:
                empty.append((row, column))

    return empty


def get_possible_moves(board) -> list[tuple[int]]:
    """ Return a list with a tuple like (row, column , n) as possible moves. """
    positions = get_empty_positions(board)

    possible_moves = []
    for pos in positions:
        for n in range(1, 10):
            if is_valid_move(board, *pos, n):
                possible_moves.append((*pos, n))

    # Sort moves by least possible options
    possible_moves.sort(key=lambda move: sum(1 for n in range(1, 10) if is_valid_move(board, move[0], move[1], n)))

    return possible_moves


def play_move(board, row: int, column: int, n: int) -> list[list[int]]:
    """ Place the number at the given position at board[row][column]. """
    updated = [r.copy() for r in board]
    updated[row][column] = n
    return updated


def is_solved(board) -> bool:
    """ Checks if the board is solved. """
    for row in board:
        if 0 in row:
            return False
    return True


def convert_board_to_tuple(board) -> tuple[tuple[int]]:
    """ Convert the board to a tuple of tuples for immutability. """
    return tuple(tuple(row) for row in board)


def pretty_print(board):
    print("+---------+---------+---------+")
    for row in range(0, 9):
        for col in range(0, 9):
            if not col % 3:
                print("|", end="")
            print(" " + str(board[row][col]) + " ", end="")
        print("|")
        if not (row+1) % 3:
            print("+---------+---------+---------+")
