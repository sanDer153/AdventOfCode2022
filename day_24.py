import bisect

UP = (-1, 0)
DOWN = (1, 0)
LEFT = (0, -1)
RIGHT = (0, 1)

def parse_input():
    with open('day_24_input') as f:
        matrix = list(map(lambda l: list(l.strip('\n')), f))
        matrix = [row[1: -1] for row in matrix[1: -1]]
        blizzard = set()
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == '^': blizzard.add((row, col, UP))
                elif matrix[row][col] == 'v': blizzard.add((row, col, DOWN))
                elif matrix[row][col] == '<': blizzard.add((row, col, LEFT))
                elif matrix[row][col] == '>': blizzard.add((row, col, RIGHT))
        return len(matrix), len(matrix[0]), blizzard

def get_heuristic(pos, goal):
    return abs(goal[0] - pos[0]) + abs(goal[1] + pos[1])

def calc_blizzard(map_height, map_width, initial_blizzard, time):
    return {((x+time*facing[0])%map_height, (y+time*facing[1])%map_width) for x, y, facing in initial_blizzard}

def find_shortest_path(part_2):
    blizzards = []
    map_height, map_width, initial_blizzard =  parse_input()
    start_pos = (-1, 0)
    goal_pos = (map_height, map_width-1)
    path = [0, (start_pos, goal_pos)]
    if part_2: path = [0, (start_pos, goal_pos), (goal_pos, start_pos), (start_pos, goal_pos)]

    for i in range(1, len(path)):
        start_pos = path[i][0]
        goal_pos = path[i][1]
        #state: (f_value = time + heuristic, position, time)
        queue = [(path[i-1] + get_heuristic(start_pos, goal_pos), start_pos, path[i-1])]
        while queue:
            f_value, position, time = queue.pop(0)
            if position == goal_pos: 
                path[i] = time
                break

            if time+1 < len(blizzards):
                next_blizzard = blizzards[time+1]
            else:
                next_blizzard = calc_blizzard(map_height, map_width, initial_blizzard, time+1)
                blizzards.append(next_blizzard)

            possible_next_positions = {position}.union({(position[0] + d[0], position[1] + d[1]) for d in {UP, DOWN, LEFT, RIGHT} if (position[0] + d[0] in range(map_height) and position[1] + d[1] in range(map_width)) or (position[0] + d[0], position[1] + d[1]) == goal_pos})
            for next_pos in possible_next_positions.difference(next_blizzard):
                next_state = (time+1 + get_heuristic(next_pos, goal_pos), next_pos, time+1)
                if next_state not in queue:
                    bisect.insort_left(queue, next_state, key= lambda n: n[0])

    return path[-1]

def first_star():
    shortest_path = find_shortest_path(False)
    print(shortest_path)

def second_star():
    shortest_path = find_shortest_path(True)
    print(shortest_path)

first_star()
second_star()