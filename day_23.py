N = (-1, 0)
S = (1, 0)
E = (0, 1)
W = (0, -1)
NE = (-1, 1)
NW = (-1, -1)
SE = (1, 1)
SW = (1, -1)

NORTH = [N, NW, NE]
SOUTH = [S, SW, SE]
WEST = [W, NW, SW]
EAST = [E, NE, SE]

def check_direction(direction, postion, elves):
    return all((postion[0] + x, postion[1] + y) not in elves for (x, y) in direction)

def first_star():
    elves = []
    proposals = []
    check_order = [NORTH, SOUTH, WEST, EAST]
    with open('day_23_input') as f:
        matrix = [list(l.strip('\n')) for l in f.readlines()]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == "#": 
                    elves.append((i, j))
                    proposals.append((i, j))
    
    for ronde in range(10):
        for i in range(len(elves)):
            checked_directions = [check_direction(d, elves[i], elves) for d in check_order]
            if all(check for check in checked_directions): proposals[i] = elves[i]
            elif True in checked_directions:
                direction = check_order[checked_directions.index(True)][0]
                proposals[i] = (elves[i][0] + direction[0], elves[i][1] + direction[1])
            else:
                proposals[i] = elves[i]
        for i in range(len(elves)):
            if proposals.count(proposals[i]) == 1:
                elves[i] = proposals[i]
        check_order.append(check_order.pop(0))

    min_point = None
    max_point = None
    for elf in elves:
        if min_point == None: min_point = elf
        if max_point == None: max_point = elf
        min_point = (min(min_point[0], elf[0]), min(min_point[1], elf[1]))
        max_point = (max(max_point[0], elf[0]), max(max_point[1], elf[1]))

    print((max_point[0] - min_point[0] + 1) * (max_point[1] - min_point[1] + 1) - len(elves))

def second_star():
    elves = []
    proposals = []
    check_order = [NORTH, SOUTH, WEST, EAST]
    with open('day_23_input') as f:
        matrix = [list(l.strip('\n')) for l in f.readlines()]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == "#": 
                    elves.append((i, j))
                    proposals.append((i, j))
    
    ronde = 0
    n_moved = len(elves)
    while n_moved != 0:
        n_moved = 0
        ronde += 1
        
        for i in range(len(elves)):
            checked_directions = [check_direction(d, elves[i], elves) for d in check_order]
            if all(check for check in checked_directions): proposals[i] = elves[i]
            elif True in checked_directions:
                direction = check_order[checked_directions.index(True)][0]
                proposals[i] = (elves[i][0] + direction[0], elves[i][1] + direction[1])
            else:
                proposals[i] = elves[i]
        for i in range(len(elves)):
            if proposals.count(proposals[i]) == 1:
                if elves[i] != proposals[i]: n_moved += 1
                elves[i] = proposals[i]
        check_order.append(check_order.pop(0))

        if ronde % 10 == 0: print(str(ronde) + ' rondes: ' + str(1 - n_moved/len(elves)))

    print(ronde)

first_star()
second_star()