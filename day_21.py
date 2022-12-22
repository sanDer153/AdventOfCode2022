import re


def first_star():
    lookup_table = {}
    with open('day_21_input') as f:
        for monkey in f.readlines():
            monkey = monkey.strip('\n')
            monkey = monkey.split(': ')
            if len(monkey[1]) == 11: monkey[1] = '('+monkey[1]+')'
            lookup_table[monkey[0]] = monkey[1]
    
    root = lookup_table['root']
    expressions = re.findall(r'\b[a-z]{4}\b', root)
    while len(expressions) != 0:
        for exp in expressions:
            root = root.replace(exp, lookup_table[exp])
        expressions = re.findall(r'\b[a-z]{4}\b', root)
    print(eval(root))

def second_star():
    lookup_table = {}
    with open('day_21_input') as f:
        for monkey in f.readlines():
            monkey = monkey.strip('\n')
            monkey = monkey.split(': ')
            if len(monkey[1]) == 11: monkey[1] = '('+monkey[1]+')'
            lookup_table[monkey[0]] = monkey[1]
    
    lookup_table['humn'] = 'humn'
    
    root = lookup_table['root']
    expressions = re.findall(r'\b[a-z]{4}\b', root)
    root1 = expressions[0]
    root2 = expressions[1]
    while set(expressions) != {'humn'}:
        for exp in expressions:
            root1 = root1.replace(exp, lookup_table[exp])
            root2 = root2.replace(exp, lookup_table[exp])
        expressions = re.findall(r'\b[a-z]{4}\b', root1) + re.findall(r'\b[a-z]{4}\b', root2)
    
    for number in range(3451534020000, 4000000000000):
        new_root1 = eval(root1.replace('humn', str(number)))
        new_root2 = eval(root2.replace('humn', str(number)))
        if new_root1 == new_root2: 
            print(number)
            break;
    

first_star()
second_star()