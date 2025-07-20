# %%
import random as r

import numpy as np
from tqdm import tqdm

from sudoku.sudoku import Sudoku


# %%

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


def make_sudoku():
    grid = np.zeros((9, 9))

    random_starting_point = tuple(np.random.randint(0, 9, (2,)))

    # Set a random starting point to a random number
    grid[tuple(random_starting_point)] = np.random.randint(1, 10)
    # grid[7, 8] = np.random.randint(1, 10)

    _NUMBER_POSSIBILITIES = set(range(1, 10))

    while 0 in grid:

        possibilities = {}
        for row in range(9):
            for col in range(9):
                if grid[row, col] == 0:
                    excluded_by_row = set(grid[row, :])
                    excluded_by_col = set(grid[:, col])

                    square_row_index = int(row / 3) * 3
                    square_col_index = int(col / 3) * 3

                    excluded_by_square = set(
                        grid[
                            square_row_index : square_row_index + 3,
                            square_col_index : square_col_index + 3,
                        ].flatten()
                    )

                    excluded_numbers = excluded_by_col.union(excluded_by_row).union(
                        excluded_by_square
                    )
                    possibilities[(row, col)] = _NUMBER_POSSIBILITIES - excluded_numbers

        # Choose next point
        min_num_possibilities = 9
        coordinates_to_choose_from = []

        for coordinate, coordinate_possibilities in possibilities.items():
            if len(coordinate_possibilities) > min_num_possibilities:
                continue
            elif len(coordinate_possibilities) < min_num_possibilities:
                min_num_possibilities = len(coordinate_possibilities)
                coordinates_to_choose_from = []

            coordinates_to_choose_from.append(coordinate)

        # Start generation from scratch if we write ourselves into a corner
        if len(coordinates_to_choose_from) == 0:
            return make_sudoku()
        if min_num_possibilities == 0:
            return make_sudoku()

        next_coordinate = r.choice(coordinates_to_choose_from)
        next_entry = r.choice(list(possibilities[next_coordinate]))

        grid[next_coordinate] = next_entry

    return Sudoku(grid)


generated_sudoku = make_sudoku()

print(generated_sudoku.check_sudoku())
generated_sudoku.sudoku

# %%
# Check if we get any errors
for i in tqdm(range(10000)):
    make_sudoku()
