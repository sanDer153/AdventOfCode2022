

def first_star():
    sides_exposed = set()
    with open('day_18_input') as f:
        for cube in f.readlines():
            cube = cube.strip('\n')
            cube = list(map(int, cube.split(',')))
            for i in range(len(cube)):
                side1 = cube.copy()
                side1[i] = (cube[i] - 1, cube[i])
                side1 = tuple(side1)
                side2 = cube.copy()
                side2[i] = (cube[i], cube[i] + 1)
                side2 = tuple(side2)

                if side1 in sides_exposed:
                    sides_exposed.remove(side1)
                else:
                    sides_exposed.add(side1)
                
                if side2 in sides_exposed:
                    sides_exposed.remove(side2)
                else:
                    sides_exposed.add(side2)
        print(len(sides_exposed))

def second_star():
    min_cube = (0, 0, 0)
    max_cube = (0, 0, 0)
    cubes = set()
    with open('day_18_input') as f:
        for cube in f.readlines():
            cube = cube.strip('\n')
            cube = tuple(map(int, cube.split(',')))
            cubes.add(cube)
            min_cube = (min(min_cube[0], cube[0]), min(min_cube[1], cube[1]), min(min_cube[2], cube[2]))
            max_cube = (max(max_cube[0], cube[0]), max(max_cube[1], cube[1]), max(max_cube[2], cube[2]))
    
    max_cube = (max_cube[0]+1, max_cube[1]+1, max_cube[2]+1)
    steam_to_expand = {min_cube}
    steam = set()
    while len(steam_to_expand) != 0:
        steam_cube = list(steam_to_expand).pop(0)
        steam_to_expand.remove(steam_cube)
        steam.add(steam_cube)
        for vct in {(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)}:
            new_steam_cube = (steam_cube[0] + vct[0], steam_cube[1] + vct[1], steam_cube[2] + vct[2])
            if min_cube[0] <= new_steam_cube[0] <= max_cube[0] and \
                min_cube[1] <= new_steam_cube[1] <= max_cube[1] and \
                min_cube[2] <= new_steam_cube[2] <= max_cube[2] and \
                new_steam_cube not in cubes and new_steam_cube not in steam:
                steam_to_expand.add(new_steam_cube)
    
    zone = {(x, y, z) for x in range(min_cube[0], max_cube[0]+1) for y in range(min_cube[1], max_cube[1]+1) for z in range(min_cube[2], max_cube[2]+1)}
    cubes = zone.difference(steam)
    sides_exposed = set()
    for cube in cubes:
        for i in range(len(cube)):
            side1 = list(cube)
            side1[i] = (cube[i] - 1, cube[i])
            side1 = tuple(side1)
            side2 = list(cube)
            side2[i] = (cube[i], cube[i] + 1)
            side2 = tuple(side2)

            if side1 in sides_exposed:
                sides_exposed.remove(side1)
            else:
                sides_exposed.add(side1)
            
            if side2 in sides_exposed:
                sides_exposed.remove(side2)
            else:
                sides_exposed.add(side2)
    print(len(sides_exposed))
            

first_star()
second_star()