

def first_star():
    Y = 2000000
    sensors = set()
    beacons = set()
    beacon_dist = dict()
    no_beacon_positions = set()
    with open("day_15_input") as f:
        for line in f.readlines():
            line = line.strip("Sensor at ").strip("\n")
            line = line.split(": ")
            line[1] = line[1].strip("closest beacon is at ")
            line[0] = (int(line[0].split(", ")[0].strip("x=")), int(line[0].split(", ")[1].strip("y=")))
            line[1] = (int(line[1].split(", ")[0].strip("x=")), int(line[1].split(", ")[1].strip("y=")))
            sensors.add(line[0])
            beacons.add(line[1])
            beacon_dist[line[0]] = abs(line[1][0] - line[0][0]) + abs(line[1][1] - line[0][1])

    for sensor in sensors:
        x_dist = beacon_dist[sensor] - abs(sensor[1] - Y)
        if x_dist >= 0:
            for x in range(sensor[0]-x_dist, sensor[0]+x_dist+1):
                no_beacon_positions.add((x, Y))

    for beacon in beacons:
        no_beacon_positions.discard(beacon)

    print(len(no_beacon_positions))

def second_star():
    sensors = set()
    beacons = set()
    beacon_dist = dict()
    with open("day_15_input") as f:
        for line in f.readlines():
            line = line.strip("Sensor at ").strip("\n")
            line = line.split(": ")
            line[1] = line[1].strip("closest beacon is at ")
            line[0] = (int(line[0].split(", ")[0].strip("x=")), int(line[0].split(", ")[1].strip("y=")))
            line[1] = (int(line[1].split(", ")[0].strip("x=")), int(line[1].split(", ")[1].strip("y=")))
            sensors.add(line[0])
            beacons.add(line[1])
            beacon_dist[line[0]] = abs(line[1][0] - line[0][0]) + abs(line[1][1] - line[0][1])

    MAX_COORD = 4000000
    for y in range(MAX_COORD + 1):
        covered = []
        for sensor in sensors:
            x_dist = beacon_dist[sensor] - abs(sensor[1] - y)
            if x_dist >= 0:
                covered.append((max(0, sensor[0]-x_dist), min(MAX_COORD + 1, sensor[0]+x_dist+1)))
        x = 0
        i = 0
        while i < len(covered):
            if covered[i][0] <= x:
                x = max(x, covered[i][1])
                covered.remove(covered[i])
                i=0
            else:
                i += 1
        if x != MAX_COORD + 1:
            print(x * MAX_COORD + y)
            break


first_star()
second_star()