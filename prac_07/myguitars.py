import csv
from guitar import Guitar

def main():
    guitars = []
    with open('guitars.csv', 'r') as in_file:
        for line in in_file:
            rows = line.strip().split(',')
            guitar = Guitar(rows[0], int(rows[1]), float(rows[2]))
            guitars.append(guitar)

    guitars.sort()

    for guitar in guitars:
        print(guitar)

    add_guitar()


def add_guitar():
    name = input("Name: ")
    year = int(input("Year: "))
    cost = float(input("Cost:$ "))
    with open('guitars.csv', 'a') as add_file:
        add_file.write(f"{name},{year},{cost}\n")


main()