#!/usr/bin/python3
from anytree import *

# Create a dict to store the nodes
a = {}

# Create a Root Node
a['COM'] = Node('COM')

inpt = []

f = open('input.txt', 'r')
line = f.readline()
while line:
    line = line.rstrip('\n')
    inpt.append(line.split(')'))
    line = f.readline()
f.close()

for x in inpt:
    a[x[1]] = Node(x[1])


for x in inpt:
    a[x[1]].parent = a[x[0]]

count = 0
for key in a:
    count += len(a[key].ancestors)

print(count)
