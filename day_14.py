SOURCE = (500, 0)


def norm(x):
    if x != 0: return x // abs(x)
    return 0

def first_star():
    rocks = set()
    sand = set()
    with open("day_14_input") as f:
        rock_schemas = list(map(lambda n: n.split(" -> "), map(lambda m: m.strip("\n"), f)))
        rock_schemas = [[(int(node.split(',')[0]), int(node.split(',')[1]))for node in schema]for schema in rock_schemas]
            
        for schema in rock_schemas:
            for i in range(len(schema) - 1):
                start = schema[i]
                end = schema[i+1]
                vct = (norm(end[0] - start[0]), norm(end[1] - start[1]))
                while start != end:
                    rocks.add(start)
                    start = (start[0] + vct[0], start[1] + vct[1])
                rocks.add(start)
        max_y = max([rock[1] for rock in rocks])
        stop = False
        while not stop:
            if SOURCE in sand: stop = True
            sand_unit = SOURCE
            objects = rocks.union(sand)
            blocked = False
            while not blocked:
                if sand_unit[1] > max_y:
                    blocked = True
                    stop = True
                elif (sand_unit[0], sand_unit[1] + 1) not in objects:
                    sand_unit = (sand_unit[0], sand_unit[1] + 1)
                elif (sand_unit[0] - 1, sand_unit[1] + 1) not in objects:
                    sand_unit = (sand_unit[0] - 1, sand_unit[1] + 1)
                elif (sand_unit[0] + 1, sand_unit[1] + 1) not in objects:
                    sand_unit = (sand_unit[0] + 1, sand_unit[1] + 1)
                else:
                    blocked = True
                    sand.add(sand_unit)
        print(len(sand))

def second_star():
    rocks = set()
    sand = set()
    with open("day_14_input") as f:
        rock_schemas = list(map(lambda n: n.split(" -> "), map(lambda m: m.strip("\n"), f)))
        rock_schemas = [[(int(node.split(',')[0]), int(node.split(',')[1]))for node in schema]for schema in rock_schemas]
            
        for schema in rock_schemas:
            for i in range(len(schema) - 1):
                start = schema[i]
                end = schema[i+1]
                vct = (norm(end[0] - start[0]), norm(end[1] - start[1]))
                while start != end:
                    rocks.add(start)
                    start = (start[0] + vct[0], start[1] + vct[1])
                rocks.add(start)
        floor = max([rock[1] for rock in rocks]) + 2
        stop = False
        while not stop:
            if SOURCE in sand: stop = True
            sand_unit = SOURCE
            objects = rocks.union(sand)
            blocked = False
            while not blocked:
                if (sand_unit[0], sand_unit[1] + 1) not in objects and sand_unit[1] + 1 != floor:
                    sand_unit = (sand_unit[0], sand_unit[1] + 1)
                elif (sand_unit[0] - 1, sand_unit[1] + 1) not in objects and sand_unit[1] + 1 != floor:
                    sand_unit = (sand_unit[0] - 1, sand_unit[1] + 1)
                elif (sand_unit[0] + 1, sand_unit[1] + 1) not in objects and sand_unit[1] + 1 != floor:
                    sand_unit = (sand_unit[0] + 1, sand_unit[1] + 1)
                else:
                    blocked = True
                    sand.add(sand_unit)
        print(len(sand))
            
first_star()
second_star()