# CCC 2020 Junior J5 / Senior S2: Escape Room

from collections import defaultdict, deque

m = int(input())
n = int(input())
grid = [list(map(int, input().split())) for _ in range(m)]

value_to_cells = defaultdict(list)
for r in range(1, m + 1):
    for c in range(1, n + 1):
        value_to_cells[r * c].append((r, c))

target = (m, n)
queue = deque([(1, 1)])
visited = set(queue)

while queue:
    r, c = queue.popleft()
    if (r, c) == target:
        print("yes")
        break

    next_cells = value_to_cells.pop(grid[r - 1][c - 1], [])
    for nr, nc in next_cells:
        if (nr, nc) not in visited:
            visited.add((nr, nc))
            queue.append((nr, nc))
else:
    print("no")
