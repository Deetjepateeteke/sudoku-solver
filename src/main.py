from utils import (
    convert_board_to_tuple,
    get_possible_moves,
    is_solved,
    play_move,
    pretty_print
)
import time


class SudokuSolver:

    def __init__(self, board: list[list[int]]):
        self.stack = [board]
        self.visited = set()

    def solve(self) -> list[list[int]] | None:
        """ Solve the Sudoku using DFS and backtacking. """

        if len(self.stack):
            current_board = self.stack.pop()
            self.visited.add(convert_board_to_tuple(current_board))

            moves = get_possible_moves(current_board)
            for move in moves:
                new_board = play_move(current_board, *move)

                if is_solved(new_board):
                    pretty_print(new_board)
                    print(f"Found solution: ({len(self.visited)} states visited)")
                    print(f"Time taken: {round(time.time() - start_time, 3)} seconds")
                    return True

                if convert_board_to_tuple(new_board) not in self.visited:
                    self.stack.append(new_board)

                if self.solve():
                    return True
                else:
                    return False
            else:
                print(f"Couldn't find a solution. ({len(self.visited)} states visited)")
                return False


if __name__ == "__main__":
    start_time = time.time()

    board = [
        [0, 0, 4, 6, 7, 8, 0, 0, 0],
        [0, 7, 0, 1, 9, 5, 0, 0, 0],
        [1, 0, 8, 0, 4, 2, 0, 0, 0],
        [8, 5, 0, 7, 6, 1, 0, 2, 3],
        [4, 2, 6, 8, 0, 0, 0, 0, 0],
        [7, 1, 3, 0, 0, 0, 0, 0, 6],
        [0, 0, 0, 0, 3, 7, 2, 8, 4],
        [2, 8, 0, 0, 0, 9, 0, 3, 5],
        [3, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

    solver = SudokuSolver(board)
    solver.solve()
