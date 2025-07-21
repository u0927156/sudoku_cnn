import numpy as np
from os import PathLike


class Sudoku:

    def __init__(self, sudoku: np.ndarray):
        if not isinstance(sudoku, np.ndarray):
            raise ValueError("Sudoku must be a numpy array")
        if sudoku.shape != (9, 9):
            raise ValueError("Sudoku must be 9x9")

        self.sudoku = sudoku

    def check_sudoku(self):
        _SOLVED_SET = set(range(1, 10))

        for col in range(9):
            if set(self.sudoku[:, col]) != _SOLVED_SET:
                return False
        for row in range(9):
            if set(self.sudoku[row, :]) != _SOLVED_SET:
                return False

        for horizontal_square in range(3):
            for vertical_square in range(3):
                idx_h = horizontal_square * 3
                idx_v = vertical_square * 3
                if (
                    set(self.sudoku[idx_h : idx_h + 3, idx_v : idx_v + 3].flatten())
                    != _SOLVED_SET
                ):
                    return False

        return True

    def __str__(self):
        return str(self.sudoku)

    def __repr__(self):
        return str(self.sudoku)

    def save_sudoku(self, file_path: PathLike):
        np.save(file_path, self.sudoku)


def load_sudoku(file_path: PathLike):
    return Sudoku(np.load(file_path))
