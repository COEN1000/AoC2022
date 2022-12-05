import numpy as np
import os,sys
from difflib import SequenceMatcher
import difflib

def day1(filename: str):
    elves = []
    calories = 0

    with open(filename, "r") as f:
        while True:
            line = f.readline()
            if not line:
                break
            if line == "" or line == "\n":
                elves.append(calories)
                calories = 0
            else:
                calories += int(line)     
    print("D1 Part1 ",np.max(elves)) #pt1
    elves.sort(reverse=True)

    top3 = 0 
    for x in range(3):
        top3+=elves[x]
    print("D1 Part2 ",top3) #pt2

def day2(filename: str):
    PT2_STRAT = dict(A = dict(X = 4, Y = 8, Z = 3),B = dict(X = 1, Y = 5, Z = 9),C = dict(X = 7, Y = 2, Z = 6))
    PT1_STRAT = dict(A = dict(X = 3, Y = 4, Z = 8),B = dict(X = 1, Y = 5, Z = 9),C = dict(X = 2, Y = 6, Z = 7))

    with open(filename, "r") as f:
        
        lines = f.readlines()
        pt1_score = 0
        pt2_score = 0
        for line in lines:
            pt1_score += PT1_STRAT[line[0]][line[2]]
            pt2_score += PT2_STRAT[line[0]][line[2]]
        print("D2 Part1: ",pt1_score, " D2 Part2: ",pt2_score)

def day3(filename: str):
    sum = 0
    with open(filename, "r") as f:        
        for line in f:
            mid = len(line)
            str1 = line[0:mid//2]
            str2 = line[mid//2:]
            
            matcher = difflib.SequenceMatcher(a=str1, b=str2)
            match = matcher.find_longest_match(0, len(matcher.a), 0, len(matcher.b))

            if str1[match.a].isupper() :
                sum+=ord(str1[match.a])-38
            else:
                sum+=ord(str1[match.a])-96

    print("D3 part1:", sum)

if __name__ == '__main__':
    #day1("input/day1.txt")
    #day2("input/day2.txt")
    day3("input/day3.txt")