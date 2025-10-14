# CCC 2023 Junior J3: Special Event

n = int(input())
availability = [input().strip() for _ in range(n)]

best = 0
days = []
for day in range(5):
    count = sum(1 for person in availability if person[day] == "Y")
    if count > best:
        best = count
        days = [str(day + 1)]
    elif count == best:
        days.append(str(day + 1))

print(",".join(days))
