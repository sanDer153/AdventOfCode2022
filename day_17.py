

BLOCKS = [[(0, 0), (0, 1), (0, 2), (0, 3)],
        [(0, 1), (1, 0), (1, 1), (1, 2), (2, 1)],
        [(0, 0), (0, 1), (0, 2), (1, 2), (2, 2)],
        [(0, 0), (1, 0), (2, 0), (3, 0)],
        [(0, 0), (0, 1), (1, 0), (1, 1)]]

def simulate_tetris(number_of_blocks, air_flow):
    cave = {(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6)}
    timer = 0
    highest_block = 0
    height_evolution = [0]

    for block_n in range(number_of_blocks):
        block = BLOCKS[block_n%5].copy()
        for i in range(len(block)):
            block[i] = (block[i][0]+highest_block+4, block[i][1]+2)
        
        blocked = False
        while not blocked:
            vct = (0, 0)
            #horizontal shift
            if air_flow[timer%len(air_flow)] == '<': vct = (0, -1)
            if air_flow[timer%len(air_flow)] == '>': vct = (0, 1)
            timer += 1

            block_next = block.copy()
            for i in range(len(block_next)):
                block_next[i] = (block_next[i][0] + vct[0], block_next[i][1] + vct[1])
            if all(rock not in cave and 0 <= rock[1] <= 6 for rock in block_next): block = block_next

            #vertical shift
            vct = (-1, 0)
            block_next = block.copy()
            for i in range(len(block_next)):
                block_next[i] = (block_next[i][0] + vct[0], block_next[i][1] + vct[1])
            if all(rock not in cave and 0 <= rock[1] <= 6 for rock in block_next): 
                block = block_next
            else:
                blocked = True
                highest_block = max(highest_block, max([rock[0] for rock in block]))
                height_evolution.append(highest_block)
                cave = cave.union(set(block))

    return cave, timer, highest_block, height_evolution

def print_row(row_encoded):
    row = str(bin(row_encoded))
    row = row[2:]
    row = '0' * (7-len(row)) + row
    row = row.replace('0', '.').replace('1', '#')
    print(row)

def first_star():
    air_flow = []
    with open('day_17_input') as f:
        air_flow = list(f.readline().strip('\n'))
    
    print(simulate_tetris(2022, air_flow)[2])

def second_star():
    air_flow = []
    with open('day_17_input') as f:
        air_flow = list(f.readline().strip('\n'))
    
    (cave, timer, highest_block, height_evolution) = simulate_tetris(4000, air_flow)
    cave_encoded = []
    for row in range(highest_block + 1):
        row_encoded = 0
        for x in [6-b for (a, b) in cave if a == row]:
            row_encoded += (1 << x)
        cave_encoded.append(row_encoded)
        # print_row(row_encoded)
    
    print('encoded, starting pattern search')
    str_cave_encoded = list(map(str, cave_encoded))
    pattern = None
    for start in range(len(str_cave_encoded) // 2):
        for end in range(len(str_cave_encoded) // 2, len(str_cave_encoded)):
            string = '-'.join(str_cave_encoded[start:end+1])
            temp = (string + '-' + string).find(string, 1, -1)
            if temp != -1:
                pattern = string[:temp]
                break
        if pattern is not None: break
    pattern_start_height = start
    pattern_height = len(pattern[:-1].split('-'))
    print('pattern found')

    blocks_start_part = height_evolution.index(pattern_start_height) - 1
    blocks_in_pattern = height_evolution.index(pattern_start_height+pattern_height) - 1 - blocks_start_part

    height = 0
    blocks_to_go = 1000000000000
    height += pattern_start_height - 1
    blocks_to_go -= blocks_start_part

    height += (blocks_to_go//blocks_in_pattern) * pattern_height
    blocks_to_go %= blocks_in_pattern

    height += height_evolution[blocks_start_part+blocks_to_go]-(pattern_start_height-1)

    print(height)
    

first_star()
second_star()

