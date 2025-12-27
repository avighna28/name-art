import os
from datetime import datetime, timedelta

NAME = "AVIGHNA"

# Simple 5x5 font for letters
LETTERS = {
    "A": [
        "  #  ",
        " # # ",
        "#####",
        "#   #",
        "#   #",
    ],
    "V": [
        "#   #",
        "#   #",
        "#   #",
        " # # ",
        "  #  ",
    ],
    "I": [
        "#####",
        "  #  ",
        "  #  ",
        "  #  ",
        "#####",
    ],
    "G": [
        " ### ",
        "#    ",
        "# ###",
        "#   #",
        " ### ",
    ],
    "H": [
        "#   #",
        "#   #",
        "#####",
        "#   #",
        "#   #",
    ],
    "N": [
        "#   #",
        "##  #",
        "# # #",
        "#  ##",
        "#   #",
    ],
}

start_date = datetime.now() - timedelta(weeks=40)

def make_commit(date):
    with open("data.txt", "a") as f:
        f.write(str(date) + "\n")
    os.system("git add data.txt")
    os.system(f'git commit --date="{date.isoformat()}" -m "commit"')

x_offset = 0

for ch in NAME:
    pattern = LETTERS[ch]
    for row in range(5):
        for col in range(5):
            if pattern[row][col] == "#":
                commit_date = start_date + timedelta(days=row * 7 + col + x_offset)
                make_commit(commit_date)
    x_offset += 6
