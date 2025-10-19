#!/usr/bin/python3
import sys

lines = [line.strip() for line in sys.stdin]  

for l in lines[1:]:
    n,c = l.split()
    o = int(n)*c
    print(o)