#!/usr/bin/python3

def generatePath(arr):
    targetarray = [[0,0]]
    for a in arr:
        command = a[:1]
        value = int(a[1:])
        # We need to keep the lengths in sync. In effect, we are building a 2d array of the coordinates.
        if command == 'U':
            # positive, vertical array
            for i in range(0, value):
                targetarray.append([targetarray[-1][0], (targetarray[-1][1] + 1)])
                i =+1
        elif command == 'D':
            # negative, vertical array
            for i in range(0, value):
                targetarray.append([targetarray[-1][0], (targetarray[-1][1] - 1)])
                i =+1
        elif command == 'R':
            # positive, horizontal array
            for i in range(0, value):
                targetarray.append([(targetarray[-1][0] + 1), targetarray[-1][1]])
                i =+1
        elif command == 'L':
            # negative, vertical array
            for i in range(0, value):
                targetarray.append([(targetarray[-1][0] - 1), targetarray[-1][1]])
                i =+1
    return targetarray
      




f = open('input.txt', 'r')

wire1 = f.readline().split(',')
wire1path = generatePath(wire1).copy()

wire2 = f.readline().split(',')
wire2path = generatePath(wire2).copy()

#from turtle import *
#turt = Turtle()
#turt.pd()
#
#turt.speed(0)
#
#for i in wire1path:
#    turt.setpos(i[0],i[1])
#turt.color('blue')
#for i in wire2path:
#    turt.setpos(i[0],i[1])
#
#

# Compare wire1-h with wire2-v
matches = []
for i in wire1path:
    for j in wire2path:
        if i == j:
            if i == [0, 0]:
                break
            print("Got a match!" + str(i))
            matches.append(abs(i[0]) + abs(i[1]))
            matches.sort()
            print("Smallest match :" + str(matches[0]))




