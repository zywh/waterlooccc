# Problem Statement — Are we there yet?

# You are traveling on a straight road that passes through five cities. You're given the distances between each pair of consecutive cities—that is, the distance between City 1 and City 2, City 2 and City 3, City 3 and 4, and City 4 and 5 (four integers in total). All distances are positive and less than 1000.

# You need to build a distance table showing, for each pair of the five cities, the distance between them. You will output 5 lines; the 
# 𝑖
# ith line lists distances from City 
# 𝑖
# i to Cities 1, 2, … 5, in order, separated by spaces. The distance from a city to itself is 0.

# Read the four distances between consecutive cities
d = list(map(int, input().split()))  # length 4

# Build prefix sum of distances from City 1
prefix = [0] * 5
for i in range(1, 5):
    prefix[i] = prefix[i - 1] + d[i - 1]

# Generate distance table
for i in range(5):
    row = []
    for j in range(5):
        row.append(str(abs(prefix[i] - prefix[j])))
    print(" ".join(row))


#

# After computing the first line into list `dist`
dist = list(map(int, input().split()))
j = 1
while j < 5:
    current = dist[j]
    for i in range(5):
        if i < j:
            dist[i] += current
        else:
            dist[i] -= current
    print(*dist)
    j += 1
