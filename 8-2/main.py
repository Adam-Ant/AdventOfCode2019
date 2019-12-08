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

outputimg = []
for i in range(0,6):
    row = []
    for j in range (0,25):
        row.append(99)
    outputimg.append(row)

for layer in layers:
    for i in range(0,6):
        for j in range(0,25):
            if outputimg[i][j] == 99:
                if layer[i][j] != 2:
                    outputimg[i][j] = layer[i][j]

for row in outputimg:
    print(row)
