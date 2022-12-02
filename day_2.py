#A: Rock, B: Paper, C: Scissors
#X: Rock 1, Y: Paper 2, Z: Scissors 3
SCORE_TABLE_1 = {"A X": 4, "A Y": 8, "A Z": 3, "B X": 1, "B Y": 5, "B Z": 9, "C X": 7, "C Y": 2, "C Z": 6}
#X: Lose, Y: Draw, Z: Win
SCORE_TABLE_2 = {"A X": 3, "A Y": 4, "A Z": 8, "B X": 1, "B Y": 5, "B Z": 9, "C X": 2, "C Y": 6, "C Z": 7}

def first_star():
    with open("day_2_input") as f:
        scores = list(map(lambda n: SCORE_TABLE_1[n],map(lambda n: n.strip("\n"), f)))
        print(sum(scores))

def second_star():
    with open("day_2_input") as f:
        scores = list(map(lambda n: SCORE_TABLE_2[n],map(lambda n: n.strip("\n"), f)))
        print(sum(scores))

first_star()
second_star()