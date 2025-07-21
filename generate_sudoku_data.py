from tqdm import tqdm
from pathlib import Path

from sudoku.generate_sudoku import generate_sudoku
from sudoku.sudoku import Sudoku

NUM_PUZZLES_TO_GENERATE = 100000

BASE_FILE_PATH = Path(".") / "data"

for i in tqdm(range(NUM_PUZZLES_TO_GENERATE)):
    s: Sudoku = generate_sudoku()

    s.save_sudoku(BASE_FILE_PATH / f"{i:07d}.npy")
