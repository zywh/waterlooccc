# CCC 2019 Senior S4: Tourism

import heapq
import sys
from collections import deque
from typing import Deque, Dict, List, Optional


class Group:
    def __init__(self, max_val: int, group_id: int) -> None:
        self.max_val = max_val
        self.id = group_id
        self.bases: Deque[int] = deque()
        self.max_deque: Deque[int] = deque()
        self.value = float("-inf")
        self.active = True

    def push_back(self, base: int) -> None:
        self.bases.append(base)
        while self.max_deque and self.max_deque[-1] < base:
            self.max_deque.pop()
        self.max_deque.append(base)

    def pop_front(self) -> None:
        val = self.bases.popleft()
        if self.max_deque and self.max_deque[0] == val:
            self.max_deque.popleft()

    def extend_from(self, other: "Group") -> None:
        for base in other.bases:
            self.push_back(base)

    def recompute(self) -> None:
        if self.max_deque:
            self.value = self.max_val + self.max_deque[0]
        else:
            self.value = float("-inf")
            self.active = False


def push_group_value(heap: List[tuple[float, int]], group: Group) -> None:
    if not group.active:
        return
    group.recompute()
    heapq.heappush(heap, (-group.value, group.id))


def get_best(heap: List[tuple[float, int]], groups_map: Dict[int, Group]) -> int:
    while heap:
        neg_val, gid = heap[0]
        group = groups_map.get(gid)
        if group is None or not group.active or group.value != -neg_val:
            heapq.heappop(heap)
            continue
        return int(group.value)
    return 0


def solve_day(
    day: int, n: int, k: int, values: List[int], best: List[int], group_counter: int
) -> int:
    current_start = (day - 1) * k + 1
    current_end = min(day * k, n)
    start_lower = current_start - k + 1

    max_suffix: Dict[int, int] = {}
    running_max = float("-inf")
    for pos in range(current_start, start_lower - 1, -1):
        running_max = max(running_max, values[pos])
        max_suffix[pos] = int(running_max)

    groups: Deque[Group] = deque()
    groups_map: Dict[int, Group] = {}
    heap: List[tuple[float, int]] = []

    for start in range(start_lower, current_start + 1):
        max_val = max_suffix[start]
        base = best[start - 1]
        if not groups or groups[-1].max_val != max_val:
            group = Group(max_val, group_counter)
            group_counter += 1
            groups.append(group)
            groups_map[group.id] = group
        else:
            group = groups[-1]
        group.push_back(base)

    for group in groups:
        push_group_value(heap, group)

    for day_end in range(current_start, current_end + 1):
        best[day_end] = get_best(heap, groups_map)
        if day_end == current_end:
            break

        # Remove the earliest start from the window.
        while groups and (not groups[0].active or not groups[0].bases):
            front = groups.popleft()
            front.active = False
        if groups:
            front_group = groups[0]
            front_group.pop_front()
            if not front_group.bases:
                front_group.active = False
                groups.popleft()
            else:
                push_group_value(heap, front_group)

        # Incorporate the next attraction.
        next_value = values[day_end + 1]
        collected: List[Group] = []
        while groups and groups[-1].max_val < next_value:
            grp = groups.pop()
            grp.active = False
            collected.append(grp)

        if groups and groups[-1].max_val == next_value:
            target = groups[-1]
        else:
            target = Group(next_value, group_counter)
            group_counter += 1
            groups.append(target)
            groups_map[target.id] = target

        for grp in reversed(collected):
            target.extend_from(grp)
        target.max_val = next_value
        target.active = True
        push_group_value(heap, target)

    return group_counter


def solve(n: int, k: int, values: List[int]) -> int:
    if k == 1:
        return sum(values[1:])

    best = [0] * (n + 1)

    current_max = values[1]
    for i in range(1, min(k, n) + 1):
        current_max = max(current_max, values[i])
        best[i] = current_max

    total_days = (n + k - 1) // k
    group_counter = 0
    for day in range(2, total_days + 1):
        group_counter = solve_day(day, n, k, values, best, group_counter)

    return best[n]


def main() -> None:
    data = list(map(int, sys.stdin.read().strip().split()))
    if not data:
        return
    n, k = data[:2]
    arr = data[2:]
    values = [0] + arr  # 1-based indexing

    print(solve(n, k, values))


if __name__ == "__main__":
    main()
