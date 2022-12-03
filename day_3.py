

def first_star():
    with open("day_3_input") as f:
        compartments = list(map(lambda n: list(n.strip("\n")), f))
        compartments = list(map(lambda n: [set(n[:int(len(n)/2)]),set(n[int(len(n)/2):])], compartments))
        double_items = list(map(lambda n: list(n[0].intersection(n[1])), compartments))
        priorities = list(map(lambda n: ord(n[0])-38 if n[0].isupper() else ord(n[0])-96, double_items))
        print(sum(priorities))

def second_star():
    with open("day_3_input") as f:
        formatted_input = list(map(lambda n: set(list(n.strip("\n"))), f))
        groups = list()
        for i in range(0, len(formatted_input), 3):
            groups.append(formatted_input[i:i+3])
        badge_items = list(map(lambda n: list(n[0].intersection(n[1]).intersection(n[2])), groups))
        priorities = list(map(lambda n: ord(n[0])-38 if n[0].isupper() else ord(n[0])-96, badge_items))
        print(sum(priorities))

first_star()
second_star()