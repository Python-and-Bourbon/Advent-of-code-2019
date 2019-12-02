import sys
from copy import deepcopy as dc

target, solved = 19690720, False

def iterate(opcode, n, v):
    i, opcode[1], opcode[2] = 0, n, v
    while opcode[i] != 99:
        command, inp1, inp2, output_position = opcode[i], opcode[opcode[i+1]], opcode[opcode[i+2]], opcode[i+3]
        if command == 1: output = inp1 + inp2
        elif command == 2: output = inp1 * inp2
        opcode[output_position] = output
        i += 4
    return opcode[0]

with open (sys.path[0]+'\\input.txt', 'r') as inp:
    original = [int(i) for i in inp.read().split(',')]

for n in range(100):
    if not solved:
        for v in range(100):
            if iterate(dc(original), n, v) == target: 
                print(n, v)
                solved = True
                break

print("Submit without spaces. If either integer is less than 10, then input integer with a leading 0")