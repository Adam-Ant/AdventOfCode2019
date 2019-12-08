#!/usr/bin/python3

# This is borked and not finished, I need to come back to it later.

from itertools import permutations

def getValue(arr, param, mode):
    if mode:
        return param
    else:
        return arr[param]

def doProgram(inpt):

    arr = inpt[0]
    inVal = inpt[1]


    # Init the counter
    counter = 0
    while True:
        # First, breakdown the opcode
        instruction = str(arr[counter]).zfill(5)

        opcode = int(instruction[3:])
        mode1 = int(instruction[2])
        mode2 = int(instruction[1])
        mode3 = int(instruction[0])

        # DEBUG: Uncomment below
        #print("Counter: %d Instruction: %s Opcode: %d   Mode1: %d Mode2: %d Mode3: %d   Param1: %d Param2: %d Param3: %d" % (counter, instruction, opcode, mode1, mode2, mode3, arr[counter + 1], arr[counter + 2], arr[counter + 3]))

        if opcode == 1:
            # Add the numbers together
            num1 = getValue(arr, arr[counter + 1], mode1)
            num2 = getValue(arr, arr[counter + 2], mode2)
            arr[arr[counter+3]] = num1 + num2
            counter += 4

        elif opcode == 2:
            # Multiply the numbers
            num1 = getValue(arr, arr[counter + 1], mode1)
            num2 = getValue(arr, arr[counter + 2], mode2)
            arr[arr[counter+3]] = num1 * num2
            counter += 4

        elif opcode == 3:
            # Input to the program
            arr[arr[ counter + 1 ]] = inVal.pop(0)
            counter += 2

        elif opcode == 4:
            # Output to the tty
            # DEBUG:
            #print("Output at %d: %d" % (counter, getValue(arr, arr[counter + 1], mode1)))
            return getValue(arr, arr[counter + 1], mode1)
            break

        elif opcode == 5:
            # Jump-If-True
            if getValue(arr, arr[counter + 1], mode1) != 0:
                counter = getValue(arr, arr[counter + 2], mode2)
            else:
                counter += 3

        elif opcode == 6:
            # Jump-If-False
            if getValue(arr, arr[counter + 1], mode1) == 0:
                counter = getValue(arr, arr[counter + 2], mode2)
            else:
                counter += 3

        elif opcode == 7:
            # If param1 < param2
            if getValue(arr, arr[counter + 1], mode1) < getValue(arr, arr[counter + 2], mode2):
                arr[ arr[counter + 3] ] = 1
            else:
                arr[ arr[counter + 3] ] = 0
            counter += 4

        elif opcode == 8:
            # If param1 == param2
            if getValue(arr, arr[counter + 1], mode1) == getValue(arr, arr[counter + 2], mode2):
                arr[ arr[counter + 3] ] = 1
            else:
                arr[ arr[counter + 3] ] = 0
            counter += 4

        elif opcode == 99:
            #Magic numbers are fun!
            return -255

    return arr[0]

inputarr = []

f = open('input.txt', 'r')
inputarr = f.readline().split(',')

# Turn them all into integers
inputarr = [ int(x) for x in inputarr ]

phases = [5, 6, 7, 8, 9]
biggestoutput = 0

for phase in permutations(phases):

    ampA = [inputarr.copy(), [phase[0], 0]]
    ampB = [inputarr.copy(), [phase[1]]]
    ampC = [inputarr.copy(), [phase[2]]]
    ampD = [inputarr.copy(), [phase[3]]]
    ampE = [inputarr.copy(), [phase[4]]]

    output = 0

    while True:
        ampB[1].append(doProgram(ampA))
        ampC[1].append(doProgram(ampB))
        ampD[1].append(doProgram(ampC))
        ampE[1].append(doProgram(ampD))
        loopout = doProgram(ampE)
        if loopout != -255:
            ampA[1].append(loopout)
            output = loopout
        else:
            break

    if output > biggestoutput:
        biggestoutput = output

print(biggestoutput)
