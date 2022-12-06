

def first_star():
    with open("day_6_input") as f:
        buff = f.readline()
        for i in range(4, len(buff)):
            if len(set(buff[i-4:i])) == 4:
                print(i)
                break;

def second_star():
    with open("day_6_input") as f:
        buff = f.readline()
        for i in range(14, len(buff)):
            if len(set(buff[i-14:i])) == 14:
                print(i)
                break;

first_star()
second_star()