#!/usr/bin/python3

import math

arr = []

def doFuel(fuel):
    return math.floor((fuel / 3) - 2)

f = open('input.txt', 'r')
for l in f:
    mass = int(l)
    while mass > 0:
        newmass = doFuel(mass)
        if newmass < 0:
            newmass = 0
        arr.append(newmass)
        mass = newmass

total = 0

for i in arr:
    total = total + i

print(total)
