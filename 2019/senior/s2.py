# CCC 2019 Senior S2: Pretty Average Primes

import sys


def sieve(limit: int) -> list[bool]:
    prime = [True] * (limit + 1)
    prime[0] = prime[1] = False
    for num in range(2, int(limit ** 0.5) + 1):
        if prime[num]:
            step = num
            prime[num * num : limit + 1 : step] = [False] * (((limit - num * num) // step) + 1)
    return prime


def main() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    t = int(data[0])
    nums = list(map(int, data[1 : 1 + t]))

    max_n = max(nums)
    limit = max_n * 2
    prime = sieve(limit)

    primes_list = [i for i, is_prime in enumerate(prime) if is_prime]

    out_lines = []
    for n in nums:
        target = 2 * n
        for p in primes_list:
            if p > n:
                break
            q = target - p
            if q >= 2 and prime[q]:
                out_lines.append(f"{p} {q}")
                break
    sys.stdout.write("\n".join(out_lines))


if __name__ == "__main__":
    main()
