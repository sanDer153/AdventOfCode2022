import re

stacks =    [['W','D','G','B','H','R','V'],
            ['J','N','G','C','R','F'],
            ['L','S','F','H','D','N','J'],
            ['J','D','S','V'],
            ['S','H','D','R','Q','W','N','V'],
            ['P','G','H','C','M'],
            ['F','J','B','G','L','Z','H','C'],
            ['S','J','R'],
            ['L','G','S','R','B','N','V','M']]

def first_star():
    with open("day_5_input") as f:
        commands = list(map(lambda n: re.split(" from | to ", n.strip("\n").strip("move ")), f))
        for command in commands:
            amount = int(command[0])
            orig = int(command[1]) - 1
            dest = int(command[2]) - 1
            for i in range(amount):
                stacks[dest].append(stacks[orig].pop())
        for stack in stacks:
            print(stack.pop(), end="")
        print("")

def second_star():
    with open("day_5_input") as f:
        commands = list(map(lambda n: re.split(" from | to ", n.strip("\n").strip("move ")), f))
        for command in commands:
            amount = int(command[0])
            orig = int(command[1]) - 1
            dest = int(command[2]) - 1
            for i in range(amount):
                stacks[dest].append(stacks[orig].pop(-amount+i))
        for stack in stacks:
            print(stack.pop(), end="")
        print("")
    

# first_star()
second_star()