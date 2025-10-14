# CCC 2023 Senior S2 / Junior J5: Symmetric Mountains

import sys

input = sys.stdin.readline

n = int(input())
line = input().strip()
if " " in line:
    heights = list(map(int, line.split()))
else:
    heights = list(map(int, line))

dp_even = None
dp_odd = None

answers = []

for length in range(1, n + 1):
    size = n - length + 1
    if length == 1:
        current = [0] * size
    elif length == 2:
        current = [abs(heights[i] - heights[i + 1]) for i in range(size)]
    else:
        previous = dp_even if length % 2 == 0 else dp_odd
        current = [
            abs(heights[i] - heights[i + length - 1]) + previous[i + 1]
            for i in range(size)
        ]

    if length % 2 == 0:
        dp_even = current
    else:
        dp_odd = current

    answers.append(min(current))

print(" ".join(map(str, answers)))
