########################
#### Initialisation ####
########################

input_ex1 = []
with open("inputs/day5_1.txt") as inputfile:
    for line in inputfile.readlines():
        input_ex1.append(int(line.strip()))


########################
####    Part one    ####
########################

sample_input = [0,
                3,
                0,
                1,
                -3]

input_data = input_ex1[::]
newIndex = 0
steps = 0
while True:

    try:
        instruction = input_data[newIndex]
        input_data[newIndex] += 1
        newIndex += instruction
        steps += 1
    except IndexError:
        print("It takes {} steps to escape this list of instructions".format(steps))
        break


########################
####    Part two    ####
########################

input_data = input_ex1[::]
newIndex = 0
steps = 0
while True:
    try:
        instruction = input_data[newIndex]
    except IndexError:
        print("It takes {} steps to escape this list of instructions".format(steps))
        break
    if instruction >= 3:
        input_data[newIndex] -= 1
    else:
        input_data[newIndex] += 1
    newIndex += instruction
    steps += 1
