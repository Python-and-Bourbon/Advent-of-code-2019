import sys

with open (sys.path[0]+'\\input.txt', 'r') as inp:
    opcode = [int(i) for i in inp.read().split(',')]

opcode[1] = 12
opcode[2] = 2

i = 0

while opcode[i] != 99:
    command, inp1, inp2, output_position = opcode[i], opcode[opcode[i+1]], opcode[opcode[i+2]], opcode[i+3]
    if command == 1:
        output = inp1 + inp2
    if command == 2:
        output = inp1 * inp2
    opcode[output_position] = output
    i += 4

print(opcode[0])