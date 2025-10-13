# CCC 2019 Junior J4: Flipper

ops = input().strip()

grid = [[1, 2], [3, 4]]

for op in ops:
    if op == "H":
        grid[0], grid[1] = grid[1], grid[0]
    elif op == "V":
        grid[0][0], grid[0][1] = grid[0][1], grid[0][0]
        grid[1][0], grid[1][1] = grid[1][1], grid[1][0]

print(f"{grid[0][0]} {grid[0][1]}")
print(f"{grid[1][0]} {grid[1][1]}")
