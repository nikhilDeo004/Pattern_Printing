# Pattern 1: Solid Square (4 x 4)
# My thinking: a square is just "rows" lines, each holding "cols" stars.
# So I need one loop for the rows and one small loop (inside) for the stars.

size = 4

for row in range(size):          # outer loop -> walks down the rows
    line = []                    # I collect the stars of this row here
    for col in range(size):      # inner loop -> walks across the columns
        line.append("*")
    print(" ".join(line))        # join with a space so it looks like "* * * *"
                                 # (join also avoids a messy trailing space)
