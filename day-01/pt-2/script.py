import sys

def fuel_req(mass): return (mass // 3) - 2

total = 0

with open(sys.path[0]+'\\'+'input.txt', 'r') as masses:
    for mass in masses.readlines():
        iter = fuel_req(int(mass.rstrip('\n')))
        while iter > 0:
            total += iter
            iter = fuel_req(iter)

print(total)