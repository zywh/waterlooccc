# CCC 2018 Junior Problem 5: Tandem Bicycle
# CCC 2018 Junior Problem 5: Tandem Bicycle
# 
# Problem Statement:
# Given two groups of cyclists, each with n members, and their respective speeds,
# pair up one cyclist from each group to form n tandem bicycles.
# For each tandem, the speed is the maximum of the two cyclists' speeds.
# There are two scenarios:
#   1. Minimize the total speed of all tandems.
#   2. Maximize the total speed of all tandems.
# Input:
#   n - number of cyclists in each group
#   d - 1 for minimizing, 2 for maximizing total speed
#   a - list of speeds for the first group
#   b - list of speeds for the second group
# Output:
#   The minimum or maximum total speed, depending on d.

n = int(input())
d = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort(reverse=(d == 2))

total = 0
for i in range(n):
    total += max(a[i], b[i])

print(total)