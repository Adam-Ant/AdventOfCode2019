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

w = Walker()

walked = w.walk(a['YOU'].parent, a['SAN'].parent)

print(len(walked[0]) + len(walked[2]))

## Find the last common ancestor
#
#you = (a['YOU'].ancestors)
#san = (a['SAN'].ancestors)
#
#lca = a['COM']
#for node in list(set(you) & set(san)):
#    if len(node.ancestors) > len(lca.ancestors):
#        lca = node
#
#print(lca)


