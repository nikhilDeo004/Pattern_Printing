# Pattern 5: Repeated Row Number Triangle
# My thinking: row 1 is "1", row 2 is "2 2", row 3 is "3 3 3" ...
# So each row repeats its OWN row number, row-number times.
# Difference from Pattern 4: I print i (outer value), not the inner counter.

rows = 5

for i in range(1, rows + 1):
    line = []
    for _ in range(i):               # repeat i times
        line.append(str(i))          # always the same number: the row number
    print(" ".join(line))
