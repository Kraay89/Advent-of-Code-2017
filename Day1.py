########################
#### Initialisation ####
########################
import re

input_ex1 = ""
with open("inputs/day1_1.txt") as inputfile:
    input_ex1 = inputfile.readline().strip()

########################
####    Part one    ####
########################
regex = re .compile(r"(\d)(?=\1+)")
matches = [match.group(1) for match in regex.finditer(input_ex1)]


# Note that this misses the edgecase of the supposed circularity of the list
# lets add it to the matches list.
matches.append('6')

# flatten the list into single integers
numbers = [num for match in matches for num in match]

# Print the Sum
print("The solution to my captcha is: {0}".format(
    sum((int(i)for i in matches))))

########################
####    Part two    ####
########################

length_of_list = len(input_ex1)
total = 0
for index, number in enumerate(input_ex1):
    if number == input_ex1[int(index + (length_of_list / 2)) % length_of_list]:
        total += int(number)

print("The solution to my captcha is: {0}".format(total))
