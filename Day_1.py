

def first_star():
    with open("day_1_input") as f:
        elfs = list(map(lambda n: list(map(int, n.split("\n"))), "".join(f).split("\n\n")))
        max = 0
        for elf in elfs:
            if sum(elf) > max:
                max = sum(elf)
        print(max)

def second_star():
    with open("day_1_input") as f:
        elfs = list(map(lambda n: list(map(int, n.split("\n"))), "".join(f).split("\n\n")))
        first = 0
        second = 0
        third = 0
        for elf in elfs:
            cal = sum(elf)
            if cal > first:
                third = second
                second = first
                first = cal
            elif cal > second:
                third = second
                second = cal
            elif cal > third:
                third = cal

        print(first + second + third)


first_star()
second_star()