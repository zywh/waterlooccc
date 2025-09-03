n = int(input())
"""
# Problem Description (2018 Waterloo CCC Junior Problem 4 - Tide):

# Given a list of n students' heights, arrange them in a line such that the sequence alternates between the shortest remaining and the tallest remaining student, starting with the shortest. 
# If n is odd, the last student should be the tallest remaining. 
# The final arrangement must be non-decreasing in height from left to right. 
# If it is not possible to arrange the students in this way, output "Impossible".

Args:
    None (reads input from stdin):
        n (int): The number of students.
        heights (List[int]): The heights of the students.

Returns:
    None (prints to stdout):
        Prints the arranged sequence of heights if possible, otherwise prints "Impossible".
"""
heights = list(map(int, input().split()))
heights.sort()

low = heights[:n//2]
high = heights[n//2:]

result = []
for i in range(n//2):
    result.append(low[i])
    result.append(high[i])

if n % 2 == 1:
    result.append(high[-1])

valid = True
for i in range(1, n):
    if result[i] < result[i-1]:
        valid = False
        break

if valid:
    print(' '.join(map(str, result)))
else:
    print("Impossible")