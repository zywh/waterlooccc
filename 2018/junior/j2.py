# You supervise a small parking lot with 
# 𝑁
# N parking spaces.

# Input:

# First line: integer 
# 𝑁
# N — the number of parking spaces (
# 1
# ≤
# 𝑁
# ≤
# 100
# 1≤N≤100).

# Second line: a string of 
# 𝑁
# N characters, each being either C (occupied) or . (empty), representing the status yesterday.

# Third line: another string of 
# 𝑁
# N characters in the same format, representing the status today.

# Objective: Determine the number of parking spaces that were occupied both yesterday and today (i.e., positions where both lines have C).

# Output: A single integer — the count of spaces that were occupied on both days.


# Read input
N = int(input().strip())
yesterday = input().strip()
today = input().strip()

# Count spaces that were occupied both days
count = 0
for i in range(N):
    if yesterday[i] == 'C' and today[i] == 'C':
        count += 1

print(count
# Solution using list comprehension for conciseness
N = int(input().strip())
yesterday = input().strip()
today = input().strip()

# Sum up matches of 'C' in both strings
result = sum(1 for y, t in zip(yesterday, today) if y == t == 'C')
print(result)


# Solution by converting C to 1 and . to 0 and run logic and summing
N = int(input().strip())
yesterday = input().strip()
today = input().strip()

# Convert C to 1 and . to 0
yesterday_numeric = [1 if c == 'C' else 0 for c in yesterday]
today_numeric = [1 if c == 'C' else 0 for c in today]

# Count occupied spaces on both days
count = sum(y & t for y, t in zip(yesterday_numeric, today_numeric))
print(count))