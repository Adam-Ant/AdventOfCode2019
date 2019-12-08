#!/usr/bin/python3
inputarr = []

f = open('input.txt', 'r')
inputarr = list(f.readline())

# Remove the newline
inputarr.pop()

# Turn them all into integers
inputarr = [ int(x) for x in inputarr ]

layers = []

while inputarr:
    layer = []
    for i in range(0,6):
        row = []
        for j in range(0,25):
            try:
                row.append(inputarr.pop(0))
            except IndexError:
                break
        layer.append(row)
    layers.append(layer)

zeroes = []
for layer in layers:
    count = 0
    for row in layer:
        count += row.count(0)
    zeroes.append(count)

ones = 0
for row in layers[zeroes.index(min(zeroes))]:
    ones += row.count(1)

twos = 0
for row in layers[zeroes.index(min(zeroes))]:
    twos += row.count(2)

print(ones * twos)
