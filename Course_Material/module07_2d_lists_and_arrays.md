Module 07 - 2D Lists and Grid Thinking
Weeks Covered: Week 7

Session 1 (1.5 hrs)
- Build 2D lists manually and with list comprehension patterns.
- Index elements using `[row][col]` and visualize grids on paper.
- Traverse rows and columns to compute sums, minima, and maxima.

Session 2 (1.5 hrs)
- Apply 2D lists to simulations such as seating charts and simple games.
- Practice neighbor checks (up, down, left, right) for CCC-style grid problems.
- Solve a past CCC Junior grid simulation together.

Homework and Practice
- Create a tic-tac-toe board representation and print it in a readable format.
- Implement a program that counts how many cells in a grid contain a specific value.
- Attempt a CCC Junior grid processing problem (e.g., 2015 J4) with focus on systematic traversal.

Sample Question
- Prompt: Given the grid `[[1, 2], [3, 4]]`, compute the sum of all entries.
- Solution:
```python
grid = [[1, 2], [3, 4]]
total = 0
for row in grid:
    for value in row:
        total += value
print(total)  # 10
```

Practice Challenge
- Prompt: Read a 3 by 3 grid of integers from the user and print the values in reverse row order.
- Solution:
```python
grid = []
for _ in range(3):
    row = list(map(int, input("Enter 3 numbers separated by spaces: ").split()))
    grid.append(row)
for row_index in range(2, -1, -1):
    print(" ".join(str(value) for value in grid[row_index]))
```
