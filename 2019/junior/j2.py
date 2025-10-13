# CCC 2019 Junior J2: Time to Decompress

lines = int(input())

for _ in range(lines):
    count, char = input().split()
    print(char * int(count))
