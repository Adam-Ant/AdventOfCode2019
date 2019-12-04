#!/usr/bin/python3

#lower = 278384
lower = 278384
upper = 824795

matches = []

for i in range(lower, upper):
    
    hasdouble = False
    #Innocent until proven guilty!
    sequence = True
    num = [int(d) for d in str(i)]
    for j in range (1,6):
        if num[j-1] == num[j]:
            hasdouble = True
        if num[j-1] > num[j]:
            sequence = False
    if hasdouble and sequence:
        print("Got one: " + str(i))
        matches.append(i)
    i += 1

print(len(matches))
