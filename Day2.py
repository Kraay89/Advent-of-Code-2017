########################
#### Initialisation ####
########################

input_ex1 = []
with open("inputs/day2_1.txt") as inputfile:
    for line in inputfile.readlines():
        input_ex1.append([int(num) for num in line.split()])

########################
####    Part one    ####
########################

spreadsheet = input_ex1
checksum = 0

for row in spreadsheet:
    min_n = min(row)
    max_n = max(row)
    diff = max_n - min_n
    checksum += diff

print("The checksum of this spreadsheet is: {}".format(checksum))

########################
####    Part two    ####
########################

input_ex2 = [sorted(row, reverse=True) for row in input_ex1]


def find_division_result(row):
    while len(row) > 0:
        test = row.pop()
        for num in row:
            if num % test == 0:
                return num / test


checksum = 0
for row in input_ex2:
    checksum += find_division_result(row)

print("The checksum of this spreadsheet is: {}".format(int(checksum)))
