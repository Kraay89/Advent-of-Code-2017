########################
#### Initialisation ####
########################

input_ex1 = 368078

########################
####    Part one    ####
########################


def x(n):
    if n > 0:
        return x(n - 1) + 2
    else:
        return 1


n = 1
lastnum = 1
while True:

    a = x(n)**2 - 6 * n
    b = x(n)**2 - 4 * n
    c = x(n)**2 - 2 * n
    d = x(n)**2

    DA = [d] + list(range(lastnum + 1, a + 1))
    AB = list(range(a, b + 1))
    BC = list(range(b, c + 1))
    CD = list(range(c, d + 1))

    # print(DA, AB, BC, CD)

    if input_ex1 in DA:
        center = DA[int(len(DA) / 2)]
        print(center)
        if input_ex1 > center:
            print("Distance of tile {0} to the origin is {1}.".format(
                input_ex1, input_ex1 - center + n))
        else:
            print("Distance of tile {0} to the origin is {1}.".format(
                input_ex1, center - input_ex1 + n))
        break
    elif input_ex1 in AB:
        center = AB[int(len(AB) / 2)]
        print(center)
        if input_ex1 > center:
            print("Distance of tile {0} to the origin is {1}.".format(
                input_ex1, input_ex1 - center + n))
        else:
            print("Distance of tile {0} to the origin is {1}.".format(
                input_ex1, center - input_ex1 + n))
        break
    elif input_ex1 in BC:
        center = BC[int(len(BC) / 2)]
        print(center)
        if input_ex1 > center:
            print("Distance of tile {0} to the origin is {1}.".format(
                input_ex1, input_ex1 - center + n))
        else:
            print("Distance of tile {0} to the origin is {1}.".format(
                input_ex1, center - input_ex1 + n))
        break
    elif input_ex1 in CD:
        center = CD[int(len(CD) / 2)]
        print(center)
        if input_ex1 > center:
            print("Distance of tile {0} to the origin is {1}.".format(
                input_ex1, input_ex1 - center + n))
        else:
            print("Distance of tile {0} to the origin is {1}.".format(
                input_ex1, center - input_ex1 + n))
        break

    n += 1
    lastnum = d
########################
####    Part two    ####
########################
