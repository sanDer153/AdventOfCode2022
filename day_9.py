

def first_star():
    with open("day_9_input") as f:
        instructions = list(map(lambda n: [n.strip("\n").split()[0], int(n.strip("\n").split()[1])], f))
        # instructions = [["R", 4],["U", 4],["L", 3],["D", 1],["R", 4],["D", 1],["L", 5],["R", 2]]
        head = [0, 0]
        tail = [0, 0]
        tail_visited = {(0, 0)}
        for inst in instructions:
            if inst[0] == "U":
                head[1] += inst[1]
            elif inst[0] == "D":
                head[1] -= inst[1]
            elif inst[0] == "L":
                head[0] -= inst[1]
            elif inst[0] == "R":
                head[0] += inst[1]

            diff = [head[0]-tail[0], head[1]-tail[1]]
            while not(abs(diff[0]) <= 1 and abs(diff[1]) <= 1):
                if diff[0] != 0 and diff[1] != 0:
                    tail = [tail[0]+int(diff[0]/abs(diff[0])), tail[1]+int(diff[1]/abs(diff[1]))]
                elif diff[0] == 0:
                    tail = [tail[0], tail[1]+int(diff[1]/abs(diff[1]))]
                else:
                    tail = [tail[0]+int(diff[0]/abs(diff[0])), tail[1]]
                tail_visited.add(tuple(tail))
                diff = [head[0]-tail[0], head[1]-tail[1]]

        print(len(tail_visited))

def second_star():
    with open("day_9_input") as f:
        instructions = list(map(lambda n: [n.strip("\n").split()[0], int(n.strip("\n").split()[1])], f))
        # instructions = [["R", 4],["U", 4],["L", 3],["D", 1],["R", 4],["D", 1],["L", 5],["R", 2]]
        # instructions = [["R", 5],["U", 8],["L", 8],["D", 3],["R", 17],["D", 10],["L", 25],["U", 20]]
        rope = [(0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)]
        tail_visited = {(0, 0)}
        for inst in instructions:
            if inst[0] == "U":
                for i in range(inst[1]):
                    rope[0] = (rope[0][0], rope[0][1]+1)
                    for k in range(9):
                        diff = (rope[k][0] - rope[k+1][0], rope[k][1] - rope[k+1][1])
                        while not(abs(diff[0]) <= 1 and abs(diff[1]) <= 1):
                            if diff[0] != 0 and diff[1] != 0:
                                rope[k+1] = (rope[k+1][0]+int(diff[0]/abs(diff[0])), rope[k+1][1]+int(diff[1]/abs(diff[1])))
                            elif diff[0] == 0:
                                rope[k+1] = (rope[k+1][0], rope[k+1][1]+int(diff[1]/abs(diff[1])))
                            else:
                                rope[k+1] = (rope[k+1][0]+int(diff[0]/abs(diff[0])), rope[k+1][1])
                            if k+1 == 9:
                                tail_visited.add(rope[k+1])
                            diff = (rope[k][0] - rope[k+1][0], rope[k][1] - rope[k+1][1])
            elif inst[0] == "D":
                for i in range(inst[1]):
                    rope[0] = (rope[0][0], rope[0][1]-1)
                    for k in range(9):
                        diff = (rope[k][0] - rope[k+1][0], rope[k][1] - rope[k+1][1])
                        while not(abs(diff[0]) <= 1 and abs(diff[1]) <= 1):
                            if diff[0] != 0 and diff[1] != 0:
                                rope[k+1] = (rope[k+1][0]+int(diff[0]/abs(diff[0])), rope[k+1][1]+int(diff[1]/abs(diff[1])))
                            elif diff[0] == 0:
                                rope[k+1] = (rope[k+1][0], rope[k+1][1]+int(diff[1]/abs(diff[1])))
                            else:
                                rope[k+1] = (rope[k+1][0]+int(diff[0]/abs(diff[0])), rope[k+1][1])
                            if k+1 == 9:
                                tail_visited.add(rope[k+1])
                            diff = (rope[k][0] - rope[k+1][0], rope[k][1] - rope[k+1][1])
            elif inst[0] == "L":
                for i in range(inst[1]):
                    rope[0] = (rope[0][0]-1, rope[0][1])
                    for k in range(9):
                        diff = (rope[k][0] - rope[k+1][0], rope[k][1] - rope[k+1][1])
                        while not(abs(diff[0]) <= 1 and abs(diff[1]) <= 1):
                            if diff[0] != 0 and diff[1] != 0:
                                rope[k+1] = (rope[k+1][0]+int(diff[0]/abs(diff[0])), rope[k+1][1]+int(diff[1]/abs(diff[1])))
                            elif diff[0] == 0:
                                rope[k+1] = (rope[k+1][0], rope[k+1][1]+int(diff[1]/abs(diff[1])))
                            else:
                                rope[k+1] = (rope[k+1][0]+int(diff[0]/abs(diff[0])), rope[k+1][1])
                            if k+1 == 9:
                                tail_visited.add(rope[k+1])
                            diff = (rope[k][0] - rope[k+1][0], rope[k][1] - rope[k+1][1])
            elif inst[0] == "R":
                for i in range(inst[1]):
                    rope[0] = (rope[0][0]+1, rope[0][1])
                    for k in range(9):
                        diff = (rope[k][0] - rope[k+1][0], rope[k][1] - rope[k+1][1])
                        while not(abs(diff[0]) <= 1 and abs(diff[1]) <= 1):
                            if diff[0] != 0 and diff[1] != 0:
                                rope[k+1] = (rope[k+1][0]+int(diff[0]/abs(diff[0])), rope[k+1][1]+int(diff[1]/abs(diff[1])))
                            elif diff[0] == 0:
                                rope[k+1] = (rope[k+1][0], rope[k+1][1]+int(diff[1]/abs(diff[1])))
                            else:
                                rope[k+1] = (rope[k+1][0]+int(diff[0]/abs(diff[0])), rope[k+1][1])
                            if k+1 == 9:
                                tail_visited.add(rope[k+1])
                            diff = (rope[k][0] - rope[k+1][0], rope[k][1] - rope[k+1][1])

            

        print(len(tail_visited))

first_star();
second_star();