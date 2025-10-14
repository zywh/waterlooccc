# CCC 2020 Senior S4: Swapping Seats

from array import array
from itertools import permutations

s = input().strip()
n = len(s)

counts = {
    "A": s.count("A"),
    "B": s.count("B"),
    "C": s.count("C"),
}

if n <= 1 or list(counts.values()).count(0) >= 2:
    print(0)
    raise SystemExit

s2 = s + s
size = len(s2)

pref_a = array("I", [0] * (size + 1))
pref_b = array("I", [0] * (size + 1))
pref_c = array("I", [0] * (size + 1))

for i, ch in enumerate(s2, 1):
    pref_a[i] = pref_a[i - 1]
    pref_b[i] = pref_b[i - 1]
    pref_c[i] = pref_c[i - 1]
    if ch == "A":
        pref_a[i] += 1
    elif ch == "B":
        pref_b[i] += 1
    else:
        pref_c[i] += 1

def segment_counts(l: int, r: int) -> tuple[int, int, int]:
    return (
        pref_a[r] - pref_a[l],
        pref_b[r] - pref_b[l],
        pref_c[r] - pref_c[l],
    )


def swaps_for_order(order: tuple[str, str, str]) -> int:
    length = [counts[ch] for ch in order]
    best = float("inf")

    l1, l2, l3 = length
    # handle degenerate cases quickly
    if l1 == n:
        return 0

    for start in range(n):
        p1 = start
        p2 = p1 + l1
        p3 = p2 + l2
        p4 = p3 + l3

        block_map = {
            order[0]: segment_counts(p1, p2),
            order[1]: segment_counts(p2, p3),
            order[2]: segment_counts(p3, p4),
        }

        counts_a = block_map["A"]
        counts_b = block_map["B"]
        counts_c = block_map["C"]

        AB = counts_a[1]
        AC = counts_a[2]
        BA = counts_b[0]
        BC = counts_b[2]
        CA = counts_c[0]
        CB = counts_c[1]

        direct_ab = min(AB, BA)
        direct_ac = min(AC, CA)
        direct_bc = min(BC, CB)

        mis = (AB + AC + BA + BC + CA + CB) - 2 * (direct_ab + direct_ac + direct_bc)
        swaps = direct_ab + direct_ac + direct_bc + (mis // 3) * 2
        if swaps < best:
            best = swaps

    return int(best)


orders = set(permutations("ABC"))
answer = min(swaps_for_order(order) for order in orders)
print(answer)
