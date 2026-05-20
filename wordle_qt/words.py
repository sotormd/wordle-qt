from importlib.resources import files

DATA = files("wordle_qt") / "data"

HUGE_PATH = DATA / "all.txt"
LARGE_PATH = DATA / "five-large.txt"
SMALL_PATH = DATA / "five-small.txt"

with HUGE_PATH.open() as file:
    HUGE = [word for word in file.read().split() if len(word) == 5]

with LARGE_PATH.open() as file:
    LARGE = file.read().split()

with SMALL_PATH.open() as file:
    SMALL = file.read().split()

HUGE = list(set(HUGE + LARGE + SMALL))
