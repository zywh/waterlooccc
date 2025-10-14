# CCC 2020 Junior J2: Epidemiology

p = int(input())
n = int(input())
r = int(input())

total = n
current = n
day = 0

while total <= p:
    day += 1
    current *= r
    total += current

print(day)
