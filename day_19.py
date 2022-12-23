from math import ceil


def calc_time_till_enough(robot, resources, robots, price):
    return max([ceil(max(0, (price[robot][r] - resources[r])) / robots[r]) for r in price[robot]])

def potential_geodes(price, robots, resources, time):
    additional_robots = {'E': 0, 'K': 0, 'O': 0, 'G': 0}
    potential_materials = resources.copy()
    for _ in range(time):
        for robot in robots.keys():
            potential_materials[robot] += robots[robot] + additional_robots[robot]
        
        for robot, robot_price in price.items():
            if all(potential_materials[r] >= robot_price[r] * (additional_robots[robot] + 1) for r in robot_price.keys()):
                additional_robots[robot] += 1
    return potential_materials["G"]

def get_most_geodes(price, time):
    max_values = {'E': 0, 'K': 0, 'O': 0, 'G': 0}
    for robot_price in price.values():
        for r in robot_price.keys():
            max_values[r] = max(max_values[r], robot_price[r])
    max_values['G'] = 1000000

    best = 0
    queue = [({'E': 1, 'K': 0, 'O': 0, 'G': 0}, {'E': 0, 'K': 0, 'O': 0, 'G': 0}, time)]

    while queue:
        robots, resources, time = queue.pop()
        if potential_geodes(price, robots, resources, time) < best:
            continue

        estimate = resources["G"] + robots["G"] * time
        if estimate > best:
            best = estimate

        buildable_robots = ['E', 'K']
        if robots['K'] > 0: buildable_robots.append('O')
        if robots['O'] > 0: buildable_robots.append('G')
        for robot in buildable_robots:
            robot_price = price[robot]
            if robots[robot] >= max_values[robot]:
                continue

            delta = calc_time_till_enough(robot, resources, robots, price)

            if delta < time:
                new_robots = robots.copy()
                new_robots[robot] += 1
                new_resources = resources.copy()
                for r in robots.keys():
                    new_resources[r] += robots[r] * (delta + 1)
                for r in robot_price.keys():
                    new_resources[r] -= robot_price[r]
                queue.append((new_robots, new_resources, time - delta - 1))

    return best

def first_star():
    solution = []
    with open('day_19_input') as f:
        for blueprint in f.readlines():

            price = {'E': {'E': 0,}, 
                    'K': {'E': 0,}, 
                    'O': {'E': 0, 'K': 0},
                    'G': {'E': 0, 'O': 0}}

            blueprint = blueprint.strip('\n').strip('Blueprint ').strip('.')
            blueprint_id = int(blueprint.split(': ')[0])
            blueprint = blueprint.replace('ore', 'E').replace('clay', 'K').replace('obsidian', 'O').replace('geode', 'G')
            blueprint = list(map(lambda n: n.split(' '), blueprint.split(': ')[1].split('. ')))
            
            for robot in blueprint:
                price[robot[1]][robot[5]] = int(robot[4])
                if len(robot) > 6: price[robot[1]][robot[8]] = int(robot[7])

            solution.append(blueprint_id * get_most_geodes(price, 24))
    print(sum(solution)) 

def second_star():
    solution = 1
    with open('day_19_input') as f:
        for blueprint in f.readlines():

            price = {'E': {'E': 0,}, 
                    'K': {'E': 0,}, 
                    'O': {'E': 0, 'K': 0},
                    'G': {'E': 0, 'O': 0}}

            blueprint = blueprint.strip('\n').strip('Blueprint ').strip('.')
            blueprint_id = int(blueprint.split(': ')[0])
            blueprint = blueprint.replace('ore', 'E').replace('clay', 'K').replace('obsidian', 'O').replace('geode', 'G')
            blueprint = list(map(lambda n: n.split(' '), blueprint.split(': ')[1].split('. ')))
            
            if blueprint_id > 3: break

            for robot in blueprint:
                price[robot[1]][robot[5]] = int(robot[4])
                if len(robot) > 6: price[robot[1]][robot[8]] = int(robot[7])

            solution *= get_most_geodes(price, 32)
    print(solution)

first_star()
second_star()