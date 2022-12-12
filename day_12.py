import bisect


def first_star():
    START = (20, 0)
    END = (20, 43)
    field = []
    frontier = [[START]]
    frontier_ends = {START}
    with open("day_12_input") as f:
        field = list(map(lambda n: list(map(lambda m: ord(m) - 97, n.strip("\n"))), f))
    while len(frontier) > 0:
        path = frontier.pop(0)
        value = field[path[-1][0]][path[-1][1]]
        frontier_ends.remove(path[-1])
        for vct in {(0, 1), (0, -1), (1, 0), (-1, 0)}:

            if 0 <= path[-1][0] + vct[0] < 41 and \
                0 <= path[-1][1] + vct[1] < 67 and \
                (path[-1][0] + vct[0], path[-1][1] + vct[1]) not in path and \
                (path[-1][0] + vct[0], path[-1][1] + vct[1]) not in frontier_ends and \
                field[path[-1][0] + vct[0]][path[-1][1] + vct[1]] <= value + 1:

                newpath = path + [(path[-1][0] + vct[0], path[-1][1] + vct[1])]
                frontier_ends.add(newpath[-1])

                if(END == newpath[-1]):
                    print_field(field, newpath)
                    print(len(newpath) - 1)
                    return
                else:
                    # bisect.insort_right(frontier, newpath, key=lambda n: n[0])
                    frontier.append(newpath)

def second_star():
    START = (26, 0)
    END = (20, 43)
    field = []
    frontier = [[START]]
    frontier_ends = {START}
    with open("day_12_input") as f:
        field = list(map(lambda n: list(map(lambda m: ord(m) - 97, n.strip("\n"))), f))
    while len(frontier) > 0:
        path = frontier.pop(0)
        value = field[path[-1][0]][path[-1][1]]
        frontier_ends.remove(path[-1])
        for vct in {(0, 1), (0, -1), (1, 0), (-1, 0)}:

            if 0 <= path[-1][0] + vct[0] < 41 and \
                0 <= path[-1][1] + vct[1] < 67 and \
                (path[-1][0] + vct[0], path[-1][1] + vct[1]) not in path and \
                (path[-1][0] + vct[0], path[-1][1] + vct[1]) not in frontier_ends and \
                field[path[-1][0] + vct[0]][path[-1][1] + vct[1]] <= value + 1:

                newpath = path + [(path[-1][0] + vct[0], path[-1][1] + vct[1])]
                frontier_ends.add(newpath[-1])

                if(END == newpath[-1]):
                    print_field(field, newpath)
                    print(len(newpath) - 1)
                    return
                else:
                    # bisect.insort_right(frontier, newpath, key=lambda n: n[0])
                    frontier.append(newpath)

def print_field(field, path):
    for i in range(len(field)):
        for j in range(len(field[i])):
            print(".", end="") if (i, j) not in path else print("#", end="")
        print("")

first_star()
second_star()