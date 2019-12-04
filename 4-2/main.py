#!/usr/bin/python3

lower = 278384
upper = 824795

matches = []

for i in range(lower, upper):
    
    hasdouble = []
    doublenum = 99
    #Innocent until proven guilty!
    sequence = True
    num = [int(d) for d in str(i)]
    for j in range (1,6):
        if num[j-1] == num[j]:
            if num[j] == doublenum:
                hasdouble[-1] += 1
            else:
                hasdouble.append(1)
            doublenum = num[j]
        if num[j-1] > num[j]:
            sequence = False
    if 1 in hasdouble and sequence:
        print("Got one: " + str(i))
        matches.append(i)
    i += 1

print(len(matches))
