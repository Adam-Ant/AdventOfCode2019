#!/usr/bin/python3
import math

def doProgram(arr, noun, verb):
    arr[1] = noun
    arr[2] = verb

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
        counter += 4
    return arr[0]
   
if __name__ == "__main__":
    inputarr = []
    
    f = open('input.txt', 'r')
    inputarr = f.readline().split(',')
    
    # Turn them all into integers
    inputarr = [ int(x) for x in inputarr ]

    
    n = 0
    v = 0
    
    for n in range(0,99):
        for v in range(0,99):
            # Copy the array, as lists act as pointers....
            if doProgram(inputarr.copy(),n,v) == 19690720:
                print("Got one! Noun: %d  Verb: %d" % (n, v))
                print("Answer required is: %d" % ((n * 100) + v))
                exit()
        verb = 0
 
 
