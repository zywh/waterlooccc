# CCC 2019 Junior J1: Winning Score

a3 = int(input())
a2 = int(input())
a1 = int(input())
b3 = int(input())
b2 = int(input())
b1 = int(input())

score_a = 3 * a3 + 2 * a2 + a1
score_b = 3 * b3 + 2 * b2 + b1

if score_a > score_b:
    print("A")
elif score_b > score_a:
    print("B")
else:
    print("T")
