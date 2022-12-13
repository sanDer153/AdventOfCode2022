import re


def parse_input(packet):
    if packet[0] != '[': return int(packet)
    if len(packet) == 2: return []

    stack = []
    packet = packet[1: -1]
    packet_result = []
    last_comma_idx = -1

    for i in range(len(packet)):
        if packet[i] == '[':
            stack.append('[')
        elif packet[i] == ']':
            stack.pop()
        elif packet[i] == ',' and len(stack) == 0:
            packet_result.append(parse_input(packet[last_comma_idx+1:i]))
            last_comma_idx = i
    packet_result.append(parse_input(packet[last_comma_idx+1:]))

    return packet_result

def compare(left, right):
    for i in range(max(len(left), len(right))):
        if i == len(left): return 1
        if i == len(right): return -1
        if type(left[i]) == int and type(right[i]) == int:
            if left[i] < right[i]: return 1
            if left[i] > right[i]: return -1
        else:
            if type(left[i]) == int: left[i] = [left[i]]
            if type(right[i]) == int: right[i] = [right[i]]
            res = compare(left[i], right[i])
            if res != 0: return res
    return 0

def first_star():
    with open("day_13_input") as f:
        pairs = list(map(lambda n: n.split("\n"), f.read().split("\n\n")))

        print(sum([index + 1 for index in range(len(pairs)) if compare(parse_input(pairs[index][0]), parse_input(pairs[index][1])) == 1]))

def second_star():
    ordered_packets = []
    with open("day_13_input") as f:
        packets = [packet.strip("\n") for packet in f.readlines() if packet != "\n\n"]
        while '' in packets: packets.remove('')

        for packet in packets:
            ordered_packets.append(packet)
            i = len(ordered_packets) - 1
            while i > 0 and compare(parse_input(ordered_packets[i-1]), parse_input(ordered_packets[i])) != 1:
                temp = ordered_packets[i]
                ordered_packets[i] = ordered_packets[i-1]
                ordered_packets[i-1] = temp
                i-=1
        solution = 1
        for key in ['[[2]]', '[[6]]']:
            ordered_packets.append(key)
            i = len(ordered_packets) - 1
            while i > 0 and compare(parse_input(ordered_packets[i-1]), parse_input(ordered_packets[i])) != 1:
                temp = ordered_packets[i]
                ordered_packets[i] = ordered_packets[i-1]
                ordered_packets[i-1] = temp
                i-=1
            solution *= i + 1
        print(solution)


first_star()
second_star()