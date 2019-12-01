#!/usr/bin/python3

import math

arr = []

f = open('input.txt', 'r')
for l in f:
    arr.append(math.floor(int(l) / 3) - 2)

total = 0
for i in arr:
    total = total + i

print(total)
