# CCC 2019 Junior J5 / S3: Escape Room

from collections import defaultdict, deque

rows = int(input())
cols = int(input())

grid = [list(map(int, input().split())) for _ in range(rows)]

# Map every possible product to the set of coordinates (1-indexed) that produce it.
product_to_cells = defaultdict(list)
for r in range(1, rows + 1):
    for c in range(1, cols + 1):
        product_to_cells[r * c].append((r, c))

target = (rows, cols)
queue = deque([(1, 1)])
visited = set(queue)

while queue:
    r, c = queue.popleft()
    if (r, c) == target:
        print("yes")
        break

    next_cells = product_to_cells.pop(grid[r - 1][c - 1], [])
    for nr, nc in next_cells:
        if (nr, nc) not in visited:
            visited.add((nr, nc))
            queue.append((nr, nc))
else:
    print("no")
