Module 11 - Advanced 2D Grids and Algorithm Design
Weeks Covered: Weeks 13-14

Session 1 (1.5 hrs)
- Model complex grid challenges such as path counting and obstacle navigation.
- Analyze sample CCC Junior and Senior grid problems to identify patterns.
- Practice converting problem descriptions into state diagrams or flowcharts.

Session 2 (1.5 hrs)
- Contrast brute-force and greedy approaches on small datasets.
- Facilitate group design sessions to brainstorm CCC-style problem solutions.
- Emphasize documenting assumptions, invariants, and edge cases.

Homework and Practice
- Solve a past CCC problem involving grid traversal (e.g., 2016 J4) and summarize the strategy.
- Draft a new CCC-style question as a team exercise, including constraints and expected output.
- Reflect on algorithm choices: why does a particular approach work efficiently?

Sample Question
- Prompt: Given a 4 by 4 grid with `.` representing open cells and `#` representing walls, count the number of open cells that have at least two open neighbors.
- Solution:
```python
grid = [
    list("..#."),
    list(".##."),
    list("...."),
    list("#..#"),
]
rows = len(grid)
cols = len(grid[0])
count = 0
directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
for r in range(rows):
    for c in range(cols):
        if grid[r][c] != ".":
            continue
        open_neighbors = 0
        for dr, dc in directions:
            nr = r + dr
            nc = c + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == ".":
                open_neighbors += 1
        if open_neighbors >= 2:
            count += 1
print(count)
```

Practice Challenge
- Prompt: Design a plan (pseudocode or code) for finding the shortest path from the top-left to bottom-right of a grid where movement is allowed only on `.` cells. Provide a Python implementation using Breadth-First Search for the sample grid above (treat `#` as blocked).
- Solution:
```python
from collections import deque

def shortest_path_bfs(grid):
    rows = len(grid)
    cols = len(grid[0])
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    visited = [[False] * cols for _ in range(rows)]
    queue = deque()
    if grid[0][0] == "#":
        return -1
    queue.append((0, 0, 0))
    visited[0][0] = True
    while queue:
        r, c, dist = queue.popleft()
        if r == rows - 1 and c == cols - 1:
            return dist
        for dr, dc in directions:
            nr = r + dr
            nc = c + dc
            if 0 <= nr < rows and 0 <= nc < cols and not visited[nr][nc] and grid[nr][nc] == ".":
                visited[nr][nc] = True
                queue.append((nr, nc, dist + 1))
    return -1

grid = [
    list("..#."),
    list(".##."),
    list("...."),
    list("#..#"),
]
print(shortest_path_bfs(grid))
```
