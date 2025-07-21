import random as r

import numpy as np

from sudoku.sudoku import Sudoku


def generate_sudoku():
    grid = np.zeros((9, 9))

    random_starting_point = tuple(np.random.randint(0, 9, (2,)))

    # Set a random starting point to a random number
    grid[tuple(random_starting_point)] = np.random.randint(1, 10)
    # grid[7, 8] = np.random.randint(1, 10)

    _NUMBER_POSSIBILITIES = set(range(1, 10))

    while 0 in grid:

        # possibilities = {}
        # for row in range(9):
        #     for col in range(9):
        #         if grid[row, col] == 0:
        #             excluded_by_row = set(grid[row, :])
        #             excluded_by_col = set(grid[:, col])

        #             square_row_index = int(row / 3) * 3
        #             square_col_index = int(col / 3) * 3

        #             excluded_by_square = set(
        #                 grid[
        #                     square_row_index : square_row_index + 3,
        #                     square_col_index : square_col_index + 3,
        #                 ].flatten()
        #             )

        #             excluded_numbers = excluded_by_col.union(excluded_by_row).union(
        #                 excluded_by_square
        #             )
        #             possibilities[(row, col)] = _NUMBER_POSSIBILITIES - excluded_numbers

        # Turned for loop logic above into this dictionary comprehension.
        possibilities = {
            (row, col): _NUMBER_POSSIBILITIES
            - set(grid[row, :])
            .union(set(grid[:, col]))
            .union(
                set(
                    grid[
                        int(row / 3) * 3 : int(row / 3) * 3 + 3,
                        int(col / 3) * 3 : int(col / 3) * 3 + 3,
                    ].flatten()
                )
            )
            for row in range(9)
            for col in range(9)
            if grid[row, col] == 0
        }

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
            return generate_sudoku()
        if min_num_possibilities == 0:
            return generate_sudoku()

        next_coordinate = r.choice(coordinates_to_choose_from)
        next_entry = r.choice(list(possibilities[next_coordinate]))

        grid[next_coordinate] = next_entry

    return Sudoku(grid)
