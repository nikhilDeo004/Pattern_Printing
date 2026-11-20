# Pattern 7: Star Pyramid
# My thinking: a pyramid is centred, so each row needs two things:
#   1) leading spaces that shrink as we go down
#   2) stars that grow by 2 each row: 1, 3, 5, 7, 9  -> formula 2*i - 1
# Because each star is drawn as "* " (2 chars wide), the padding is also
# counted in steps of 2 spaces per missing level.

rows = 5

for i in range(1, rows + 1):
    spaces = " " * ((rows - i) * 2)       # 8, 6, 4, 2, 0 spaces
    stars = " ".join(["*"] * (2 * i - 1))  # 1, 3, 5, 7, 9 stars
    print(spaces + stars)
