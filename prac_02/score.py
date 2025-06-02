"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

# : Fix this!

import random
from random import randint


def main():

    score = float(input("Enter score: "))
    while score < 0 or score > 100:
        print("Invalid score")
        score = float(input("Enter score: "))
    print(define_result(score))

    random_score = random.randint(1,100)
    print(random_score)
    print(define_result(random_score))

def define_result(score):
    if score < 50:
        score_result = "Bad"
    elif score < 90:
        score_result = "Passable"
    elif score >= 90:
        score_result = "Excellent"
    return score_result

main()