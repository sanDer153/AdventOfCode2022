

class Number:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None
        self.prev = None

    def set_links(self, prev, next):
        self.prev = prev
        self.next = next

    def move(self):
        if self.value < 0:
            self.move_left((-1*self.value)%4999)
        else:
            self.move_right((self.value)%4999)
    
    def move_left(self, steps):
        while steps > 0:
            left_number = self.prev
            self.prev = left_number.prev
            left_number.prev.next = self
            left_number.next = self.next
            self.next.prev = left_number
            self.next = left_number
            left_number.prev = self
            
            steps -= 1

    def move_right(self, steps):
        while steps > 0:
            right_number = self.next
            self.next = right_number.next
            right_number.next.prev = self
            right_number.prev = self.prev
            self.prev.next = right_number
            self.prev = right_number
            right_number.next = self
            
            steps -= 1

def first_star():
    original_order = []
    zero = None
    with open('day_20_input') as f:
        original_order = list(map(lambda n: Number(int(n.strip('\n'))), f))
    for i in range(len(original_order)):
        original_order[i].set_links(original_order[i-1], original_order[(i+1)%len(original_order)])
        if original_order[i].value == 0: zero = original_order[i]

    for number in original_order:
        number.move()

    current = zero
    solution = 0
    for i in range(1, 3001):
        current = current.next
        if i % 1000 == 0:
            solution += current.value
    print(solution)

def second_star():
    DECRYPTION_KEY = 811589153
    original_order = []
    zero = None
    with open('day_20_input') as f:
        original_order = list(map(lambda n: Number(DECRYPTION_KEY * int(n.strip('\n'))), f))
    for i in range(len(original_order)):
        original_order[i].set_links(original_order[i-1], original_order[(i+1)%len(original_order)])
        if original_order[i].value == 0: zero = original_order[i]
    
    for i in range(10):
        for number in original_order:
            number.move()

    current = zero
    solution = 0
    for i in range(1, 3001):
        current = current.next
        if i % 1000 == 0:
            solution += current.value
    print(solution)

first_star()
second_star()