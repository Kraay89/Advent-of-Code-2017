########################
#### Initialisation ####
########################

input_ex1 = []
with open("inputs/day6_1.txt") as inputfile:
    input_ex1 = [int(i) for i in inputfile.readline().strip().split()]


########################
####    Part one    ####
########################

def redistribute(memblock):
    memsize = len(memblock)
    tracker = memblock.index(max(memblock))
    stack = memblock[tracker]
    memblock[tracker] = 0
    tracker += 1
    while stack > 0:
        memblock[tracker % memsize] += 1
        stack -= 1
        tracker += 1
    return memblock


# input_ex1 = [0, 2, 7, 0]

found_distributions = []
found_distributions.append(input_ex1[::])

new_input = redistribute(input_ex1[::])
steps = 1
while not new_input in found_distributions:
    found_distributions.append(new_input)
    new_input = redistribute(new_input[::])
    steps += 1
print("It takes {} cycles to enter an infinite loop.".format(steps))


########################
####    Part two    ####
########################

length_of_loop = len(found_distributions) - \
    found_distributions.index(new_input)
print("The infinite loop contains {} steps".format(length_of_loop))
