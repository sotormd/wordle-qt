import os

HUGE_PATH = os.path.join("data", "all.txt")
LARGE_PATH = os.path.join("data", "five-large.txt")
SMALL_PATH = os.path.join("data", "five-small.txt")

with open(HUGE_PATH) as file:
    HUGE = [word for word in file.read().split() if len(word) == 5]

with open(LARGE_PATH) as file:
    LARGE = file.read().split()

with open(SMALL_PATH) as file:
    SMALL = file.read().split()

HUGE = list(set(HUGE + LARGE + SMALL))
