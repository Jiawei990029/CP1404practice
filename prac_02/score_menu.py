import random

def main():
    menu = (f"(G)et\n"
            f"(P)rint\n"
            f"(S)how\n"
             "(Q)uit")

    print(menu)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            print (define_result(score))
        elif choice == "S":
            score_stars(score)
        print(menu)
        choice = input(">>> ").upper()
    print("Farewell.")

def get_valid_score():
    score = int(input("Enter score: "))
    while score < 0 or score > 100:
        print("Invalid score")
        score = int(input("Enter score: "))
    return score

def define_result(score):
    if score < 50:
        score_result = "Bad"
    elif score < 90:
        score_result = "Passable"
    elif score >= 90:
        score_result = "Excellent"
    return score_result

def score_stars(score):
    print_style = "*"
    print(score * print_style)

main()