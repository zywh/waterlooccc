# CCC 2019 Senior S3: Arithmetic Square

from typing import List, Optional


def fill_line(values: List[Optional[int]]) -> List[Optional[int]]:
    if values.count(None) != 1:
        return values

    idx = values.index(None)
    a, b, c = values
    if idx == 0:
        values[0] = 2 * b - c
    elif idx == 1:
        values[1] = (a + c) // 2
    else:
        values[2] = 2 * b - a
    return values


def solve(grid: List[List[Optional[int]]]) -> List[List[int]]:
    while any(cell is None for row in grid for cell in row):
        changed = False

        for i in range(3):
            before = grid[i][:]
            grid[i] = fill_line(grid[i][:])
            if grid[i] != before:
                changed = True

        for j in range(3):
            col = [grid[i][j] for i in range(3)]
            before = col[:]
            col = fill_line(col)
            if col != before:
                changed = True
                for i in range(3):
                    grid[i][j] = col[i]

        if changed:
            continue

        # No direct deduction possible. Apply heuristic fill.
        # If everything is unknown, fill with zeros.
        if all(cell is None for row in grid for cell in row):
            for i in range(3):
                for j in range(3):
                    grid[i][j] = 0
            continue

        # Try to find a row with at least one known value and fill remaining
        filled = False
        for i in range(3):
            row = grid[i]
            known = [val for val in row if val is not None]
            if known and any(val is None for val in row):
                fill_value = known[0]
                grid[i] = [fill_value if val is None else val for val in row]
                filled = True
                break

        if filled:
            continue

        # Otherwise, fill a column similarly.
        for j in range(3):
            col = [grid[i][j] for i in range(3)]
            known = [val for val in col if val is not None]
            if known and any(val is None for val in col):
                fill_value = known[0]
                for i in range(3):
                    if grid[i][j] is None:
                        grid[i][j] = fill_value
                filled = True
                break

        if filled:
            continue

        # As a last resort, fill any remaining None with zero.
        for i in range(3):
            for j in range(3):
                if grid[i][j] is None:
                    grid[i][j] = 0

    return [[cell for cell in row] for row in grid]


def main() -> None:
    grid: List[List[Optional[int]]] = []
    for _ in range(3):
        row = input().split()
        parsed_row: List[Optional[int]] = []
        for val in row:
            if val == "X":
                parsed_row.append(None)
            else:
                parsed_row.append(int(val))
        grid.append(parsed_row)

    solved = solve(grid)
    for row in solved:
        print(" ".join(str(x) for x in row))


if __name__ == "__main__":
    main()
