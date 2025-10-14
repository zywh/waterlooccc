# CCC 2023 Senior S5: The Filter

import sys

sys.setrecursionlimit(1_000_000)
input = sys.stdin.readline

N = int(input())

status = {0: True}  # memoisation for remainder states


def is_good(remainder: int) -> bool:
    if remainder in status:
        return status[remainder]

    path = []
    visiting = set()
    r = remainder

    while True:
        if r in status:
            result = status[r]
            break
        value = r * 3
        digit = value // N
        next_r = value % N
        if digit == 1:
            if next_r == 0:
                result = True
                break
            result = False
            break
        if r in visiting:
            result = True
            break
        visiting.add(r)
        path.append(r)
        r = next_r

    for node in path:
        status[node] = result
    return result


def ceil_div(a: int, b: int) -> int:
    return -(-a // b)


candidates = set()


def gather(num: int, denom: int) -> None:
    # Interval [num/denom, (num+1)/denom]
    left = ceil_div(num * N, denom)
    right = ((num + 1) * N) // denom

    if right < 0 or left > N or left > right:
        return

    left = max(left, 0)
    right = min(right, N)

    if denom > N or right - left <= 32:
        for x in range(left, right + 1):
            if is_good(x % N):
                candidates.add(x)
        return

    gather(num * 3, denom * 3)
    gather(num * 3 + 2, denom * 3)


gather(0, 1)

result = sorted(candidates)
for value in result:
    print(value)
