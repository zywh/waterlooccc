# CCC 2020 Senior S5: Josh's Double Bacon Deluxe

import sys

data = sys.stdin.read().strip().split()
if not data:
    sys.exit(0)

n = int(data[0])
raw_favs = data[1:]

if len(raw_favs) == 1 and len(raw_favs[0]) == n:
    favourites = [int(ch) for ch in raw_favs[0]]
else:
    favourites = list(map(int, raw_favs))

max_type = max(favourites)

counts = [0] * (max_type + 1)
for fav in favourites:
    counts[fav] += 1

remaining = counts.copy()

coach_fav = favourites[0]

prob = [0.0] * (max_type + 1)  # prob[s] = probability current shortage is type s (0 means none)
total_burgers = n

if total_burgers == 0:
    print(0.0)
    sys.exit(0)

# Coach picks first
for burger_type in range(1, max_type + 1):
    if counts[burger_type] == 0:
        continue
    p = counts[burger_type] / total_burgers
    if burger_type == coach_fav:
        prob[0] += p
    else:
        prob[burger_type] += p

# Coach is served
remaining[coach_fav] -= 1

# Process people 2..N-1
for idx in range(2, n):
    fav = favourites[idx - 1]
    total_remaining = n - (idx - 1)

    next_prob = [0.0] * (max_type + 1)
    next_prob[0] += prob[0]

    for shortage in range(1, max_type + 1):
        ps = prob[shortage]
        if ps == 0.0:
            continue
        if fav != shortage:
            next_prob[shortage] += ps
            continue

        rem_shortage = remaining[shortage]
        if rem_shortage > 1:
            next_prob[shortage] += ps
            continue

        # rem_shortage == 1 -> last fan with shortage must choose randomly
        available_total = total_remaining
        surplus_available = remaining[coach_fav] + 1
        next_prob[0] += ps * (surplus_available / available_total)

        for burger_type in range(1, max_type + 1):
            if burger_type == shortage or burger_type == coach_fav:
                continue
            rem = remaining[burger_type]
            if rem == 0:
                continue
            next_prob[burger_type] += ps * (rem / available_total)

    prob = next_prob
    remaining[fav] -= 1

# Josh (last person)
josh_fav = favourites[-1]
success = prob[0]
for shortage in range(1, max_type + 1):
    if prob[shortage] == 0.0:
        continue
    if shortage != josh_fav:
        success += prob[shortage]

print(success)
