

class Monkey:

    def __init__(self, items, operation, test_divider) -> None:
        self.items = items.copy()
        self.operation = operation
        self.test_divider = test_divider
        self.inspected = 0
    
    def get_inspected(self):
        return self.inspected

    def set_monkey_if_true(self, monkey_if_true):
        self.monkey_if_true = monkey_if_true

    def set_monkey_if_false(self, monkey_if_false):
        self.monkey_if_false = monkey_if_false

    def take_turn_1(self):
        for i in range(len(self.items)):
            item = self.items.pop(0)
            if self.operation[0] == "*":
                item *= self.operation[1]
            elif self.operation[0] == "+":
                item += self.operation[1]
            elif self.operation[0] == "**":
                item **= 2
            item //= 3
            self.inspected += 1

            if item % self.test_divider == 0:
                self.monkey_if_true.recieve_item(item)
            else:
                self.monkey_if_false.recieve_item(item)

    def take_turn_2(self):
        for i in range(len(self.items)):
            item = self.items.pop(0)
            if self.operation[0] == "*":
                item *= self.operation[1]
            elif self.operation[0] == "+":
                item += self.operation[1]
            elif self.operation[0] == "**":
                item **= 2
            self.inspected += 1

            if item % self.test_divider == 0:
                self.monkey_if_true.recieve_item(item % (2*3*5*7*11*13*17*19))
            else:
                self.monkey_if_false.recieve_item(item % (2*3*5*7*11*13*17*19))

    def recieve_item(self, item):
        self.items.append(item)


MONKEYS = [Monkey([97, 81, 57, 57, 91, 61], ('*', 7), 11),
            Monkey([88, 62, 68, 90], ('*', 17), 19),
            Monkey([74, 87], ('+', 2), 5),
            Monkey([53, 81, 60, 87, 90, 99, 75], ('+', 1), 2),
            Monkey([57], ('+', 6), 13),
            Monkey([54, 84, 91, 55, 59, 72, 75, 70], ('**', None), 7),
            Monkey([95, 79, 79, 68, 78], ('+', 3), 3),
            Monkey([61, 97, 67], ('+', 4), 17)]

TEST_MONKEYS = [Monkey([79, 98], ('*', 19), 23),
                Monkey([54, 65, 75, 74], ('+', 6), 19),
                Monkey([79, 60, 97], ('**', None), 13),
                Monkey([74], ('+', 3), 17)]

def set_monkeys():
    MONKEYS[0].set_monkey_if_true(MONKEYS[5])
    MONKEYS[0].set_monkey_if_false(MONKEYS[6])

    MONKEYS[1].set_monkey_if_true(MONKEYS[4])
    MONKEYS[1].set_monkey_if_false(MONKEYS[2])

    MONKEYS[2].set_monkey_if_true(MONKEYS[7])
    MONKEYS[2].set_monkey_if_false(MONKEYS[4])

    MONKEYS[3].set_monkey_if_true(MONKEYS[2])
    MONKEYS[3].set_monkey_if_false(MONKEYS[1])

    MONKEYS[4].set_monkey_if_true(MONKEYS[7])
    MONKEYS[4].set_monkey_if_false(MONKEYS[0])

    MONKEYS[5].set_monkey_if_true(MONKEYS[6])
    MONKEYS[5].set_monkey_if_false(MONKEYS[3])

    MONKEYS[6].set_monkey_if_true(MONKEYS[1])
    MONKEYS[6].set_monkey_if_false(MONKEYS[3])

    MONKEYS[7].set_monkey_if_true(MONKEYS[0])
    MONKEYS[7].set_monkey_if_false(MONKEYS[5])

    TEST_MONKEYS[0].set_monkey_if_true(TEST_MONKEYS[2])
    TEST_MONKEYS[0].set_monkey_if_false(TEST_MONKEYS[3])

    TEST_MONKEYS[1].set_monkey_if_true(TEST_MONKEYS[2])
    TEST_MONKEYS[1].set_monkey_if_false(TEST_MONKEYS[0])

    TEST_MONKEYS[2].set_monkey_if_true(TEST_MONKEYS[1])
    TEST_MONKEYS[2].set_monkey_if_false(TEST_MONKEYS[3])

    TEST_MONKEYS[3].set_monkey_if_true(TEST_MONKEYS[0])
    TEST_MONKEYS[3].set_monkey_if_false(TEST_MONKEYS[1])

def first_star():
    set_monkeys()

    for round in range(20):
        for monkey in MONKEYS:
            monkey.take_turn_1()

    inspected = sorted([monkey.get_inspected() for monkey in MONKEYS])
    print(inspected[-1]*inspected[-2])

def second_star():
    set_monkeys()

    for round in range(10000):
        for monkey in MONKEYS:
            monkey.take_turn_2()

    inspected = sorted([monkey.get_inspected() for monkey in MONKEYS])
    print(inspected[-1]*inspected[-2])

# first_star()
second_star()

    