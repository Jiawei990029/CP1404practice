import random

MIN_NUMBER = 1
MAX_NUMBER = 45
RANDOM_NUMBERS = 6

def main():
    space_length = len(str(MAX_NUMBER))
    number_picks = int(input("How many quick picks? "))
    for i in range(number_picks):
        lines_output = generate_quick_picks()
        print(" ".join(f"{number:{space_length}}" for number in lines_output))

def generate_quick_picks():
    quick_picks = []
    while len(quick_picks) < RANDOM_NUMBERS:
        number = random.randint(MIN_NUMBER, MAX_NUMBER)
        if number not in quick_picks:
            quick_picks.append(number)
    return sorted(quick_picks)

main()