# Pattern 2: Right-Angled Triangle
# My thinking: row 1 has 1 star, row 2 has 2 stars ... row 5 has 5 stars.
# So the number of stars in a row is simply the row number itself.

rows = 5

for i in range(1, rows + 1):     # start at 1 so row number == star count
    line = []
    for _ in range(i):           # print as many stars as the row number
        line.append("*")
    print(" ".join(line))
