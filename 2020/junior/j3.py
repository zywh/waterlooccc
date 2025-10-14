# CCC 2020 Junior J3: Art

n = int(input())

min_x = float("inf")
max_x = float("-inf")
min_y = float("inf")
max_y = float("-inf")

for _ in range(n):
    x_str, y_str = input().split()
    x = int(x_str)
    y = int(y_str)
    min_x = min(min_x, x)
    max_x = max(max_x, x)
    min_y = min(min_y, y)
    max_y = max(max_y, y)

width = (max_x - min_x) + 2
height = (max_y - min_y) + 2

print(width, height)
