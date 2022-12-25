TRANSLATION = {'2': 2, '1': 1, '0': 0, '-': -1, '=': -2}

def decode(snafu_number):
    current_decimal_number = 0
    for number in snafu_number:
        current_decimal_number *= 5
        current_decimal_number += TRANSLATION[number]
    return current_decimal_number

def encode(decimal_number):
    pental_number = ''
    while decimal_number != 0:
        pental_number = str(decimal_number % 5) + pental_number
        decimal_number //= 5

    snafu_number = list(pental_number)
    n = len(pental_number)
    while n != 0:
        n -= 1
        if snafu_number[n] == '3':
            snafu_number[n] = '='
            rest = 1
        elif snafu_number[n] == '4':
            snafu_number[n] = '-'
            rest = 1
        else:
            rest = 0
        
        x = n
        while x != 0 and rest != 0:
            x -= 1
            temp = int(snafu_number[x]) + rest
            rest = 0
            if temp > 4: temp, rest = temp % 5, temp // 5
            snafu_number[x] = str(temp)
        if rest != 0: snafu_number = [str(rest)] + snafu_number
    
    return ''.join(snafu_number)

def first_star():
    with open('day_25_input') as f:
        solution = sum([decode(number.strip('\n')) for number in f.readlines()])
        print(encode(solution))

first_star()