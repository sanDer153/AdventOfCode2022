

BLOCKS = [[(0, 0), (0, 1), (0, 2), (0, 3)],
        [(0, 1), (1, 0), (1, 1), (1, 2), (2, 1)],
        [(0, 0), (0, 1), (0, 2), (1, 2), (2, 2)],
        [(0, 0), (1, 0), (2, 0), (3, 0)],
        [(0, 0), (0, 1), (1, 0), (1, 1)]]

def first_star():
    cave = {(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6)}
    air_flow = []
    with open('day_17_input') as f:
        air_flow = list(f.readline().strip('\n'))
    timer = 0
    highest_block = 0

    for block_n in range(2022):
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
                cave = cave.union(set(block))
    
    print(highest_block)

def second_star():
    cave = {(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6)}
    air_flow = []
    with open('day_17_input') as f:
        air_flow = list(f.readline().strip('\n'))

    timers_on_start = {}
    timer = 0
    highest_block = 0
    for block_n in range(1000000000000):
        if block_n % 5 == 0:
            if timer%len(air_flow) in timers_on_start.keys():
                print(timers_on_start[timer%len(air_flow)])
                break;
            else:
                timers_on_start[timer%len(air_flow)] = (block_n, highest_block)

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
                cave = cave.union(set(block))

    pattern_height = highest_block - timers_on_start[timer%len(air_flow)][1]
    pattern_blocks = block_n - timers_on_start[timer%len(air_flow)][0]

    highest_block = ((1000000000000 - timers_on_start[timer%len(air_flow)][0])//pattern_blocks)*pattern_height + timers_on_start[timer%len(air_flow)][1]
    cave = {(highest_block, 0), (highest_block, 1), (highest_block, 2), (highest_block, 3), (highest_block, 4), (highest_block, 5), (highest_block, 6)}
    
    for block_n in range((1000000000000 - timers_on_start[timer%len(air_flow)][0])%pattern_blocks):
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
                cave = cave.union(set(block))
    
    print(highest_block)

first_star()
second_star()

