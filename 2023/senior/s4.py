# CCC 2023 Senior S4: Minimum Cost Roads

import heapq
import sys

input = sys.stdin.readline

N, M = map(int, input().split())

graph = [[] for _ in range(N)]
cost = [0] * M

for idx in range(M):
    u, v, length, c = map(int, input().split())
    u -= 1
    v -= 1
    graph[u].append((v, length, c, idx))
    graph[v].append((u, length, c, idx))
    cost[idx] = c

chosen = [False] * M
INF = 10**18

for source in range(N):
    dist = [INF] * N
    dist[source] = 0
    heap = [(0, source)]

    while heap:
        d, node = heapq.heappop(heap)
        if d > dist[node]:
            continue
        for neighbour, length, _, _ in graph[node]:
            nd = d + length
            if nd < dist[neighbour]:
                dist[neighbour] = nd
                heapq.heappush(heap, (nd, neighbour))

    order = sorted(range(N), key=lambda x: dist[x])

    for v in order:
        if v == source or dist[v] == INF:
            continue
        best_idx = None
        best_cost = None
        for neighbour, length, edge_cost, edge_idx in graph[v]:
            if dist[neighbour] + length == dist[v]:
                if best_idx is None or edge_cost < best_cost:
                    best_idx = edge_idx
                    best_cost = edge_cost
        if best_idx is not None:
            chosen[best_idx] = True

answer = sum(cost[i] for i, flag in enumerate(chosen) if flag)
print(answer)
