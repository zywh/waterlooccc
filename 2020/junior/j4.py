# CCC 2020 Junior J4: Cyclic Shifts

s = input().strip()
t = input().strip()

extended = t
for _ in range(len(t)):
    if extended in s:
        print("yes")
        break
    extended = extended[1:] + extended[0]
else:
    print("no")
