import numpy as np
import os,sys


def day1(filename: str):
    elves = []
    calories = 0

    with open(os.path.join(sys.path[0],filename), "r") as f:
        while True:
            line = f.readline()
            if not line:
                break
            if line == "" or line == "\n":
                elves.append(calories)
                calories = 0
            else:
                calories += int(line)     
    print(np.max(elves)) #pt1
    elves.sort(reverse=True)

    top3 = 0 
    for x in range(3):
        top3+=elves[x]
    print(top3) #pt2

def day2(filename: str):
    PT2_STRAT = dict(A = dict(X = 4, Y = 8, Z = 3),B = dict(X = 1, Y = 5, Z = 9),C = dict(X = 7, Y = 2, Z = 6))
    PT1_STRAT = dict(A = dict(X = 3, Y = 4, Z = 8),B = dict(X = 1, Y = 5, Z = 9),C = dict(X = 2, Y = 6, Z = 7))

    with open(os.path.join(sys.path[0],filename), "r") as f:
        
        lines = f.readlines()
        pt1_score = 0
        pt2_score = 0
        for line in lines:
            pt1_score += PT1_STRAT[line[0]][line[2]]
            pt2_score += PT2_STRAT[line[0]][line[2]]
        print(pt1_score, pt2_score)


if __name__ == '__main__':
    day1("input/day1.txt")
    day2("input/day2.txt")