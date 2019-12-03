#!/usr/bin/python3

def generatePath(arr):
    targetarray = [[0,0,0]]
    for a in arr:
        command = a[:1]
        value = int(a[1:])
        # We need to keep the lengths in sync. In effect, we are building a 2d array of the coordinates.
        if command == 'U':
            # positive, vertical array
            for i in range(0, value):
                targetarray.append([targetarray[-1][0], (targetarray[-1][1] + 1), (targetarray[-1][2] + 1)])
                i =+1
        elif command == 'D':
            # negative, vertical array
            for i in range(0, value):
                targetarray.append([targetarray[-1][0], (targetarray[-1][1] - 1), (targetarray[-1][2] + 1)])
                i =+1
        elif command == 'R':
            # positive, horizontal array
            for i in range(0, value):
                targetarray.append([(targetarray[-1][0] + 1), targetarray[-1][1], (targetarray[-1][2] + 1)])
                i =+1
        elif command == 'L':
            # negative, horizontal array
            for i in range(0, value):
                targetarray.append([(targetarray[-1][0] - 1), targetarray[-1][1], (targetarray[-1][2] + 1)])
                i =+1
    return targetarray

f = open('input.txt', 'r')

wire1 = f.readline().split(',')
wire1path = generatePath(wire1).copy()

wire2 = f.readline().split(',')
wire2path = generatePath(wire2).copy()

# Compare wire1 with wire2
matches = []
for i in wire1path:
    for j in wire2path:
        if i[0] == j[0]:
            if i == [0, 0, 0]:
                break
            if i[1] == j[1]:
                if i == [0, 0, 0]:
                    break
                print("Got a match!" + str(i))
                matches.append(i[2] + j[2])
                matches.sort()
                print("Smallest match :" + str(matches[0]))
