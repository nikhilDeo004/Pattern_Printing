# Pattern 10: Hollow Square (5 x 5)
# My thinking: only the border has stars; everything inside is empty.
# A cell gets a star when it is on:
#   - the first row or the last row, OR
#   - the first column or the last column
# Otherwise I put a blank so the spacing stays aligned.

size = 5

for row in range(size):
    line = []
    for col in range(size):
        on_border = (row == 0 or row == size - 1 or col == 0 or col == size - 1)
        if on_border:
            line.append("*")
        else:
            line.append(" ")          # keeps the hollow part the right width
    print(" ".join(line))
