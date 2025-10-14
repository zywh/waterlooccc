# CCC 2023 Senior S3: Palindromic Poster

from collections import defaultdict
import sys

input = sys.stdin.readline


class DSU:
    def __init__(self, size: int) -> None:
        self.parent = list(range(size))
        self.rank = [0] * size

    def find(self, x: int) -> int:
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, a: int, b: int) -> None:
        ra = self.find(a)
        rb = self.find(b)
        if ra == rb:
            return
        if self.rank[ra] < self.rank[rb]:
            ra, rb = rb, ra
        self.parent[rb] = ra
        if self.rank[ra] == self.rank[rb]:
            self.rank[ra] += 1


N, M, R, C = map(int, input().split())

if R > N or C > M:
    print("IMPOSSIBLE")
    sys.exit(0)

if M == 1 and R != N:
    print("IMPOSSIBLE")
    sys.exit(0)

if N == 1 and C != M:
    print("IMPOSSIBLE")
    sys.exit(0)

row_pal = [False] * N
for i in range(R):
    row_pal[i] = True

col_pal = [False] * M
for j in range(C):
    col_pal[j] = True

dsu = DSU(N * M)

# Apply row palindrome constraints
for r in range(N):
    if not row_pal[r]:
        continue
    for c in range(M // 2):
        left = r * M + c
        right = r * M + (M - 1 - c)
        dsu.union(left, right)

# Apply column palindrome constraints
for c in range(M):
    if not col_pal[c]:
        continue
    for r in range(N // 2):
        top = r * M + c
        bottom = (N - 1 - r) * M + c
        dsu.union(top, bottom)

row_requirements = {}
if M > 1:
    for r in range(N):
        if row_pal[r]:
            continue
        found = False
        for c in range(M // 2):
            a = dsu.find(r * M + c)
            b = dsu.find(r * M + (M - 1 - c))
            if a != b:
                row_requirements[r] = (a, b)
                found = True
                break
        if not found:
            print("IMPOSSIBLE")
            sys.exit(0)
else:
    if any(not flag for flag in row_pal):
        print("IMPOSSIBLE")
        sys.exit(0)

col_requirements = {}
if N > 1:
    for c in range(M):
        if col_pal[c]:
            continue
        found = False
        for r in range(N // 2):
            a = dsu.find(r * M + c)
            b = dsu.find((N - 1 - r) * M + c)
            if a != b:
                col_requirements[c] = (a, b)
                found = True
                break
        if not found:
            print("IMPOSSIBLE")
            sys.exit(0)
else:
    if any(not flag for flag in col_pal):
        print("IMPOSSIBLE")
        sys.exit(0)

adj = defaultdict(set)

for a, b in row_requirements.values():
    adj[a].add(b)
    adj[b].add(a)

for a, b in col_requirements.values():
    adj[a].add(b)
    adj[b].add(a)

nodes = set(adj.keys())
for neighbours in adj.values():
    nodes.update(neighbours)

letters = [chr(ord("a") + i) for i in range(26)]
char_map = {}

for node in nodes:
    if node in char_map:
        continue
    used = {char_map[nbr] for nbr in adj[node] if nbr in char_map}
    for ch in letters:
        if ch not in used:
            char_map[node] = ch
            break
    else:
        print("IMPOSSIBLE")
        sys.exit(0)

    stack = [node]
    while stack:
        current = stack.pop()
        for neighbour in adj[current]:
            if neighbour in char_map:
                continue
            used_neighbours = {char_map[n] for n in adj[neighbour] if n in char_map}
            for ch in letters:
                if ch not in used_neighbours:
                    char_map[neighbour] = ch
                    stack.append(neighbour)
                    break
            else:
                print("IMPOSSIBLE")
                sys.exit(0)

result = []
for r in range(N):
    row_chars = []
    for c in range(M):
        root = dsu.find(r * M + c)
        row_chars.append(char_map.get(root, "a"))
    result.append("".join(row_chars))

# Optional verification to ensure counts (for safety)
row_count = sum(s == s[::-1] for s in result)
col_count = 0
for c in range(M):
    col_string = "".join(result[r][c] for r in range(N))
    if col_string == col_string[::-1]:
        col_count += 1

if row_count != R or col_count != C:
    print("IMPOSSIBLE")
else:
    print("\n".join(result))
