########################
#### Initialisation ####
########################

import itertools

input_ex1 = []
with open("inputs/day4_1.txt") as inputfile:
    for line in inputfile.readlines():
        input_ex1.append(line.strip().split(" "))

# print(input_ex1)
########################
####    Part one    ####
########################


def checkpass(passphrase):
    return len(passphrase) == len(set(passphrase))


testphrases = [
    "aa bb cc dd ee",
    "aa bb cc dd aa",
    "aa bb cc dd aaa"]

testphrases = [i.split(" ") for i in testphrases]

valid = 0
for i in input_ex1:
    if checkpass(i):
        valid += 1

print("{} passphrases are valid.".format(valid))

########################
####    Part two    ####
########################

testphrases = [
    "abcde fghij",
    "abcde xyz ecdab",
    "a ab abc abd abf abj",
    "iiii oiii ooii oooi oooo",
    "oiii ioii iioi iiio",
    "cirkjq nmjuu xtgejv gtexvj vjcmtqq unjmu"
]

testphrases = [i.split(" ") for i in testphrases]
# print(testphrases)


def isAnagram(s1, s2):
    return sorted(s1) == sorted(s2)


valid = 0
for phrase in input_ex1:
    stillOK = True
    for ind, word in enumerate(phrase[0:-1]):
        for otherWord in phrase[ind + 1::]:
            # print("testing on: {} and {}".format(word, otherWord))
            if isAnagram(word, otherWord):
                # print("failed on: {} and {}".format(word, otherWord))
                stillOK = False
                break
    if stillOK:
        # print(phrase)
        valid += 1


print("{} passphrases are valid.".format(valid))
