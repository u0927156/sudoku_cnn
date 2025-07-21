# %%
import random as r

import numpy as np
from tqdm import tqdm

from sudoku.sudoku import Sudoku, load_sudoku
from sudoku.generate_sudoku import make_sudoku

# %%

_SOLVED_SET = set(range(1, 10))


example_sudoku = Sudoku(
    np.array(
        [
            [0, 0, 0, 9, 0, 3, 1, 0, 0],
            [6, 0, 7, 0, 0, 0, 0, 8, 0],
            [2, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 5, 0, 0, 0, 0, 4, 0, 0],
            [0, 0, 0, 0, 6, 0, 0, 2, 0],
            [0, 1, 0, 0, 0, 0, 0, 0, 0],
            [8, 0, 0, 0, 7, 0, 0, 0, 0],
            [0, 0, 0, 3, 0, 0, 5, 0, 0],
            [0, 0, 0, 4, 0, 0, 0, 0, 9],
        ]
    )
)

solved_example = Sudoku(
    np.array(
        [
            [2, 4, 5, 9, 8, 3, 1, 6, 7],
            [6, 3, 7, 1, 4, 2, 9, 8, 5],
            [1, 8, 9, 6, 5, 7, 2, 3, 4],
            [3, 5, 6, 7, 2, 1, 4, 9, 8],
            [4, 7, 8, 5, 6, 9, 3, 2, 1],
            [9, 1, 2, 8, 3, 4, 7, 5, 6],
            [8, 9, 1, 2, 7, 5, 6, 4, 3],
            [7, 6, 4, 3, 9, 8, 5, 1, 2],
            [5, 2, 3, 4, 1, 6, 8, 7, 9],
        ]
    )
)

incorrectly_solved_example = Sudoku(
    np.array(
        [
            [2, 4, 5, 9, 8, 3, 1, 6, 7],
            [6, 3, 7, 1, 4, 2, 9, 8, 5],
            [1, 8, 9, 6, 5, 7, 2, 3, 4],
            [2, 5, 6, 7, 2, 1, 4, 9, 8],
            [4, 7, 8, 5, 6, 9, 3, 2, 1],
            [9, 1, 3, 8, 3, 4, 7, 5, 6],
            [8, 9, 1, 2, 7, 5, 6, 4, 3],
            [7, 6, 4, 3, 9, 8, 5, 1, 2],
            [5, 2, 3, 4, 1, 6, 8, 7, 9],
        ]
    )
)

# %%
# Check sudoku puzzle

print(solved_example.check_sudoku())
print(example_sudoku.check_sudoku())
print(incorrectly_solved_example.check_sudoku())

# %%


generated_sudoku = make_sudoku()

print(generated_sudoku.check_sudoku())
generated_sudoku.sudoku

# %%

for i in tqdm(range(10000)):
    s = make_sudoku()
