import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    if len(data) < 3:
        return

    rows = int(data[0])
    cols = int(data[1])
    max_cost = int(data[2])

    if rows <= 0 or cols <= 0:
        print(0)
        return

    pattern = list(range(1, max_cost + 1))
    prev = [0] * cols
    new = [0] * cols

    # Fill first row directly.
    idx = 0
    if max_cost == 1:
        # Fast path when all tiles cost 1.
        prev[:] = [1] * cols
    else:
        pat = pattern
        m_local = max_cost
        for c in range(cols):
            prev[c] = pat[idx]
            idx += 1
            if idx == m_local:
                idx = 0

    row_offset = 0
    last_index = cols - 1

    for _ in range(1, rows):
        row_offset = (row_offset + cols) % max_cost
        idx = row_offset

        pat = pattern
        prev_local = prev
        new_local = new
        m_local = max_cost

        i = 0
        while i < cols:
            cost = pat[idx]
            idx += 1
            if idx == m_local:
                idx = 0

            best = prev_local[i]
            if i:
                left = prev_local[i - 1]
                if left < best:
                    best = left
            if i != last_index:
                right = prev_local[i + 1]
                if right < best:
                    best = right

            new_local[i] = best + cost
            i += 1

        prev, new = new, prev

    print(min(prev))


if __name__ == "__main__":
    main()
