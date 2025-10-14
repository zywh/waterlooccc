# CCC 2023 Junior J4 / Senior S1: Trianglane

def read_row(c: int) -> list[int]:
    raw = input().strip().split()
    if len(raw) == 1 and len(raw[0]) == c:
        return [int(ch) for ch in raw[0]]
    return [int(token) for token in raw]


C = int(input())
top = read_row(C)
bottom = read_row(C)

grid = [top, bottom]

perimeter = 0
rows = 2

for r in range(rows):
    for c in range(C):
        if grid[r][c] == 0:
            continue

        # Left neighbour
        if c == 0 or grid[r][c - 1] == 0:
            perimeter += 1

        # Right neighbour
        if c == C - 1 or grid[r][c + 1] == 0:
            perimeter += 1

        # Vertical neighbour depends on orientation
        upward = (r + c) % 2 == 0
        if upward:
            if r == rows - 1 or grid[r + 1][c] == 0:
                perimeter += 1
        else:
            if r == 0 or grid[r - 1][c] == 0:
                perimeter += 1

print(perimeter)
