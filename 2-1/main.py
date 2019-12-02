#!/usr/bin/python3

import math

arr = []

f = open('input.txt', 'r')
arr = f.readline().split(',')

# Turn them all into integers
arr = [ int(x) for x in arr ]

arr[1] = 12
arr[2] = 2

# Init the counter
counter = 0 

while True:
    if arr[counter] == 1:
        # Add the numbers together
        num1 = arr[arr[counter+1]]
        num2 = arr[arr[counter+2]]
        arr[arr[counter+3]] = num1 + num2
    elif arr[counter] == 2:
        # Multiply the numbers
        num1 = arr[arr[counter+1]]
        num2 = arr[arr[counter+2]]
        arr[arr[counter+3]] = num1 * num2
    elif arr[counter] == 99:
        break
    else:
        print("Ruh Roh Raggy, got a weird counter value at pos:")
        print(counter)
        print(arr)
        exit()
    counter += 4

print(arr)
