# Pattern 8: Inverted Star Pyramid
# My thinking: exactly Pattern 7 upside down.
# Now the widest row comes first, and as we go down:
#   - leading spaces grow  (0, 2, 4, 6, 8)
#   - stars shrink by 2    (9, 7, 5, 3, 1)  -> formula 2*i - 1 with i going 5 -> 1

rows = 5

for i in range(rows, 0, -1):               # count backwards 5..1
    spaces = " " * ((rows - i) * 2)        # starts at 0 and grows each row
    stars = " ".join(["*"] * (2 * i - 1))  # 9, 7, 5, 3, 1
    print(spaces + stars)
