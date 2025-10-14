# CCC 2020 Senior S1: Surmising a Sprinter's Speed

n = int(input())
observations = []
for _ in range(n):
    t, x = map(int, input().split())
    observations.append((t, x))

observations.sort()

best = 0.0
for i in range(1, n):
    t1, x1 = observations[i - 1]
    t2, x2 = observations[i]
    speed = abs(x2 - x1) / (t2 - t1)
    if speed > best:
        best = speed

print(best)
