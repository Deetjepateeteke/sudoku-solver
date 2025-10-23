# Sudoku Solver

A simple and efficient command-line Sudoku solver written in Python.
It uses depth-first search with backtracking and some heuristics to solve any Sudoku puzzle.

## Example

After running the solver, this is what the output looks like:

```text
+---------+---------+---------+
| 5  3  4 | 6  7  8 | 1  9  2 |
| 6  7  2 | 1  9  5 | 3  4  8 |
| 1  9  8 | 3  4  2 | 5  6  7 |
+---------+---------+---------+
| 8  5  9 | 7  6  1 | 4  2  3 |
| 4  2  6 | 8  5  3 | 7  1  9 |
| 7  1  3 | 9  2  4 | 8  5  6 |
+---------+---------+---------+
| 9  6  1 | 5  3  7 | 2  8  4 |
| 2  8  7 | 4  1  9 | 6  3  5 |
| 3  4  5 | 2  8  6 | 9  7  1 |
+---------+---------+---------+
Found solution: (43 states visited)
Time taken: 0.023 seconds
```

## License

This project is licensed under the [MIT License](LICENSE).
