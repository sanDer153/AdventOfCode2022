

def first_star():
    with open("day_10_input") as f:
        commands = list(map(lambda n: n.strip("\n").split(), f))

        X = 1
        cycle = 0
        signal_strength = 0
        for c in commands:
            cycle += 1
            if cycle in {20, 60, 100, 140, 180, 220}:
                signal_strength += cycle * X

            if c[0] == "addx":
                cycle += 1
                if cycle in {20, 60, 100, 140, 180, 220}:
                    signal_strength += cycle * X
                X += int(c[1])
            
        print(signal_strength)

def second_star():
    with open("day_10_input") as f:
        commands = list(map(lambda n: n.strip("\n").split(), f))

        X = 1
        cycle = 0
        screen = [["." for j in range(40)] for i in range(6)]
        for c in commands:
            cycle += 1
            if (cycle - 1) % 40 in {X-1, X, X+1}:
                screen[(cycle - 1) // 40][(cycle - 1) % 40] = "#"

            if c[0] == "addx":
                cycle += 1
                if (cycle - 1) % 40 in {X-1, X, X+1}:
                    screen[(cycle - 1) // 40][(cycle - 1) % 40] = "#"
                X += int(c[1])
            
        for row in screen:
            for pix in row:
                print(pix, end="")
            print("")

first_star()
second_star()