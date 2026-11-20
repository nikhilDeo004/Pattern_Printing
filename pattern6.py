# Pattern 6: Right-Aligned Triangle
# My thinking: it's the normal triangle, but pushed to the right with spaces.
# Each star takes 2 characters on screen ("* "), so every missing star
# on the left has to be replaced by 2 blank characters.
# Row i has i stars, so it needs (rows - i) "missing" stars -> (rows - i) * 2 spaces.

rows = 5

for i in range(1, rows + 1):
    spaces = " " * ((rows - i) * 2)       # leading padding that pushes stars right
    stars = " ".join(["*"] * i)           # the stars of this row
    print(spaces + stars)
