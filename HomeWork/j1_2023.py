d = int(input())
c = int(input())

# b = 500 if d>c else 0

b = 500 * (d > c)

p = d*50 - c*10 + b
print(p)