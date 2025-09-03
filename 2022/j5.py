# CCC Problem: Largest Square Pool

def can_place_square(N, trees, size):
    """Check if a square of given size can be placed without hitting trees"""
    tree_set = set(trees)  # Convert to set for O(1) lookup
    
    # Try all possible top-left corners for the square
    for top_row in range(1, N - size + 2):  # 1-indexed, ensure square fits
        for left_col in range(1, N - size + 2):
            # Check if this square position contains any trees
            has_tree = False
            for r in range(top_row, top_row + size):
                for c in range(left_col, left_col + size):
                    if (r, c) in tree_set:
                        has_tree = True
                        break
                if has_tree:
                    break
            
            if not has_tree:
                return True
    
    return False

# Read input
N = int(input())
T = int(input())

trees = []
for _ in range(T):
    r, c = map(int, input().split())
    trees.append((r, c))

# Binary search or linear search for the maximum square size
# Since we want the largest possible, we'll try from N down to 1
max_size = 0

for size in range(N, 0, -1):
    if can_place_square(N, trees, size):
        max_size = size
        break

print(max_size)
