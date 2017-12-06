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
    center = 0
    if input_ex1 in DA:
        center = DA[int(len(DA) / 2)]
    elif input_ex1 in AB:
        center = AB[int(len(AB) / 2)]
    elif input_ex1 in BC:
        center = BC[int(len(BC) / 2)]
    elif input_ex1 in CD:
        center = CD[int(len(CD) / 2)]

    if center > 0:
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


def expandGrid(grid):
    # Rethink the probem: I turn the grid 90 degrees counter clockwise
    # and add an extra row of zero's to what is now the bottom,
    # but is essentially a new part of the spiral.
    grid = zip(*grid[::-1])
    grid = [list(i) for i in list(grid)]

    return grid + [[0] * len(grid[0])]


def fillSpiral(grid):
    # Find zeros in the current and replace them with the sum of their non-zero neighbours
    while 0 in grid[-1]:
        index = grid[-1].index(0)
        try:
            grid[-1][index] += grid[-2][index]
        except:
            pass
        try:
            grid[-1][index] += grid[-2][index + 1]
        except:
            pass
        if index > 0:
            try:
                grid[-1][index] += grid[-2][index - 1]
            except:
                pass
            try:
                grid[-1][index] += grid[-1][index - 1]
            except:
                pass
    return grid


grid = [[1]]
while True:
    grid = expandGrid(grid)
    grid = fillSpiral(grid)

    if max(grid[-1]) > input_ex1:
        print("The first value in this spiral to exceed the input of exercise 1 is {}.".format(
            list(filter(lambda x: x > input_ex1, grid[-1]))[0]))
        for row in grid:
            print(row)
        break
