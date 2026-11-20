# Pattern 4: Increasing Number Triangle
# My thinking: same triangle shape as before, but instead of stars
# every row prints 1, 2, 3 ... up to the row number.
# The inner loop counter itself is the number I print.

rows = 5

for i in range(1, rows + 1):         # i = which row we're on
    line = []
    for num in range(1, i + 1):      # counts 1..i in this row
        line.append(str(num))        # numbers must become text before joining
    print(" ".join(line))
