

def parse_input():
    connec = {}
    flow = {}
    dist = {}
    with open("day_16_input") as f:
        split_input = list(map(lambda n: n.strip("\n").split(" "), f))
        for entry in split_input:
            valve = entry[1]
            valve_flow = int(entry[4].strip("rate=").strip(";"))
            if valve_flow > 0: 
                flow[valve] = valve_flow
                dist[valve] = {}
            connec[valve] = list(map(lambda n: n.strip(","), entry[9:]))
        dist["AA"] = {}
        for valve in dist.keys():
            distances = {valve: 0}
            new_distances = distances.copy()
            d = 0
            while d in distances.values():
                for v in distances.keys():
                    if distances[v] == d:
                        for link in connec[v]:
                            if link not in distances.keys():
                                new_distances[link] = d+1
                distances = new_distances.copy()
                d += 1
            distances = {v : distances[v] for v in distances.keys() if v in flow.keys()}
            dist[valve] = distances
    return flow, dist

def construct_paths1(time_left, current_path, distances):
    last = current_path[-1]
    new_paths = [current_path+[valve] for valve in distances[last].keys() if valve not in current_path and time_left - (distances[last][valve] + 1) > 0]
    if len(new_paths) == 0:
        return [current_path]
    else:
        p = []
        for path in new_paths:
            p += construct_paths1(time_left - (distances[last][path[-1]] + 1), path, distances)
        return p

def construct_paths2(time_left_1, time_left_2, current_path, distances):
    last1 = current_path[0][-1]
    last2 = current_path[1][-1]
    new_paths1 = [current_path[0]+[valve] for valve in distances[last1].keys() if valve not in current_path[0] and valve not in current_path[1] and time_left_1 - (distances[last1][valve] + 1) > 0]
    new_paths2 = [current_path[1]+[valve] for valve in distances[last2].keys() if valve not in current_path[0] and valve not in current_path[1] and time_left_2 - (distances[last2][valve] + 1) > 0]
    if len(new_paths1) == 0 and len(new_paths2) == 0: 
        return [current_path]
    elif len(new_paths1) == 0:
        p = []
        for path in new_paths2:
            p += construct_paths2(time_left_1, time_left_2 - (distances[last2][path[-1]] + 1), [current_path[0], path], distances)
        return p
    elif len(new_paths2) == 0:
        p = []
        for path in new_paths1:
            p += construct_paths2(time_left_1 - (distances[last1][path[-1]] + 1), time_left_2, [path, current_path[1]], distances)
        return p
    else:
        p = []
        for path1 in new_paths1:
            for path2 in new_paths2:
                if path1[-1] != path2[-1]:
                    p += construct_paths2(time_left_1 - (distances[last1][path1[-1]] + 1), time_left_2 - (distances[last2][path2[-1]] + 1), [path1, path2], distances)
        return p



def first_star():
    (flow, dist) = parse_input()
    paths = construct_paths1(30, ["AA"], dist)
    max_pressure = 0
    for path in paths:
        time_left = 30
        pressure = 0
        for i in range(1, len(path)):
            time_left -= dist[path[i-1]][path[i]] + 1
            pressure += flow[path[i]] * time_left
        max_pressure = max(max_pressure, pressure)
    print(max_pressure)

def second_star():
    (flow, dist) = parse_input()
    paths = construct_paths2(26, 26, [["AA"], ["AA"]], dist)
    print("paths constructed")
    print(len(paths))
    max_pressure = 0
    for path in paths:
        time_left1 = 26
        time_left2 = 26
        pressure = 0
        for i in range(1, len(path[0])):
            time_left1 -= dist[path[0][i-1]][path[0][i]] + 1
            pressure += flow[path[0][i]] * time_left1
        for i in range(1, len(path[1])):
            time_left2 -= dist[path[1][i-1]][path[1][i]] + 1
            pressure += flow[path[1][i]] * time_left2
        max_pressure = max(max_pressure, pressure)
    print(max_pressure)



first_star()
second_star()