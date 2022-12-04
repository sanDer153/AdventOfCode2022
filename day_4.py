

def first_star():
    with open("day_4_input") as f:
        pairs = list(map(lambda n: [list(map(int, n.strip("\n").split(',')[0].split('-'))), list(map(int, n.strip("\n").split(',')[1].split('-')))], f))
        fully_contains = 0
        for pair in pairs:
            elf_1 = pair[0]
            elf_2 = pair[1]
            if elf_1[0] <= elf_2[0] and elf_1[1] >= elf_2[1]:
                fully_contains += 1
            elif elf_1[0] >= elf_2[0] and elf_1[1] <= elf_2[1]:
                fully_contains += 1
        print(fully_contains)

def second_star():
    with open("day_4_input") as f:
        pairs = list(map(lambda n: [list(map(int, n.strip("\n").split(',')[0].split('-'))), list(map(int, n.strip("\n").split(',')[1].split('-')))], f))
        overlap = 0
        for pair in pairs:
            overlap += 1
            elf_1 = pair[0]
            elf_2 = pair[1]
            if elf_1[0] < elf_2[0] and elf_1[1] < elf_2[0]:
                overlap -= 1
            elif elf_1[0] > elf_2[1] and elf_1[1] > elf_2[1]:
                overlap -= 1
        print(overlap)

first_star()
second_star()
