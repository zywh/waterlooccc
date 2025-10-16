# https://dmoj.ca/problem/ccc05j1

# CCC '05 J1 - The Cell Sell

# Read inputs (daytime, evening, weekend) from stdin
d = int(input().strip())
e = int(input().strip())
w = int(input().strip())

# Costs in cents
# a_day =  d-100 if d>100 else 0
# b_day =  d-250 if d>250 else 0
# plan_a = a_day*25 + e*15 + w*20
# plan_b = b_day*45 + e*35 + w*25

plan_a = max(d - 100, 0) * 25 + e * 15 + w * 20
plan_b = max(d - 250, 0) * 45 + e * 35 + w * 25

print(f"Plan A costs {plan_a / 100:.2f}")
print(f"Plan B costs {plan_b / 100:.2f}")

if plan_a < plan_b:
    print("Plan A is cheapest.")
elif plan_b < plan_a:
    print("Plan B is cheapest.")
else:
    print("Plan A and B are the same price.")