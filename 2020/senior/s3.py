# CCC 2020 Senior S3: Searching for Strings

from typing import List, Tuple


def compute_hashes(s: str, base: int, mod: int) -> Tuple[List[int], List[int]]:
    n = len(s)
    prefix = [0] * (n + 1)
    power = [1] * (n + 1)
    for i, ch in enumerate(s, 1):
        val = ord(ch) - 96  # 'a' -> 1
        prefix[i] = (prefix[i - 1] * base + val) % mod
        power[i] = (power[i - 1] * base) % mod
    return prefix, power


def substring_hash(prefix: List[int], power: List[int], left: int, right: int, base: int, mod: int) -> int:
    result = (prefix[right] - (prefix[left] * power[right - left]) % mod) % mod
    if result < 0:
        result += mod
    return result


needle = input().strip()
haystack = input().strip()

n = len(needle)
m = len(haystack)

if n > m:
    print(0)
    raise SystemExit

needle_count = [0] * 26
for ch in needle:
    needle_count[ord(ch) - 97] += 1

window_count = [0] * 26
for ch in haystack[:n]:
    window_count[ord(ch) - 97] += 1

base1, mod1 = 911382323, 1_000_000_007
base2, mod2 = 972663749, 1_000_000_009

prefix1, power1 = compute_hashes(haystack, base1, mod1)
prefix2, power2 = compute_hashes(haystack, base2, mod2)

seen = set()

def add_hash(idx: int) -> None:
    h1 = substring_hash(prefix1, power1, idx, idx + n, base1, mod1)
    h2 = substring_hash(prefix2, power2, idx, idx + n, base2, mod2)
    seen.add((h1, h2))

if window_count == needle_count:
    add_hash(0)

for i in range(n, m):
    window_count[ord(haystack[i - n]) - 97] -= 1
    window_count[ord(haystack[i]) - 97] += 1
    if window_count == needle_count:
        add_hash(i - n + 1)

print(len(seen))
