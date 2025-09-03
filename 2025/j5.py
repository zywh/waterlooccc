# CCC 2025 Junior J5: Connecting Territories

def get_cost(row, col, C, M):
    """Get the cost of tile at (row, col) given the pattern with max cost M"""
    # Calculate the position in the repeating pattern (reading left to right, row by row)
    position = row * C + col  # 0-indexed position in the flattened grid
    return (position % M) + 1

# Read input
R = int(input())  # Number of rows
C = int(input())  # Number of columns  
M = int(input())  # Maximum cost of a tile

# Create the grid with costs
grid = []
for r in range(R):
    row = []
    for c in range(C):
        cost = get_cost(r, c, C, M)
        row.append(cost)
    grid.append(row)

# Dynamic programming approach
# dp[r][c] = minimum cost to reach tile (r, c)
dp = [[float('inf')] * C for _ in range(R)]

# Initialize first row
for c in range(C):
    dp[0][c] = grid[0][c]

# Fill the DP table
for r in range(1, R):
    for c in range(C):
        # Check all possible previous positions (adjacent tiles)
        for prev_c in range(max(0, c-1), min(C, c+2)):  # c-1, c, c+1
            if dp[r-1][prev_c] != float('inf'):
                dp[r][c] = min(dp[r][c], dp[r-1][prev_c] + grid[r][c])

# Find the minimum cost in the last row
min_cost = min(dp[R-1])
print(min_cost)
