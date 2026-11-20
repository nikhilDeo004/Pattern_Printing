# Pattern 11: Hollow Right-Angled Triangle
# My thinking: it's the normal triangle, but only the outline is drawn.
# In row i (counting from 1) there are i cells, and a star is needed at:
#   - the first cell of the row (the left edge)
#   - the last cell of the row  (the slanted edge)
#   - every cell of the last row (the base)
# All other cells are blank.

rows = 5

for i in range(1, rows + 1):
    line = []
    for col in range(1, i + 1):
        if col == 1 or col == i or i == rows:
            line.append("*")
        else:
            line.append(" ")          # hollow interior
    print(" ".join(line))
