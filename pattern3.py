# Pattern 3: Inverted Right-Angled Triangle
# My thinking: this is Pattern 2 flipped upside down.
# Row 1 has 5 stars and each next row loses one star.
# I just make the loop count DOWN from 5 to 1.

rows = 5

for i in range(rows, 0, -1):     # 5, 4, 3, 2, 1 (step of -1 counts backwards)
    line = []
    for _ in range(i):           # stars in this row = current value of i
        line.append("*")
    print(" ".join(line))
