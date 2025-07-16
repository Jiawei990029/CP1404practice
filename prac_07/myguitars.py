import csv
from guitar import Guitar

def main():
    guitars = []
    with open('guitars.csv', 'r') as in_file:
        for line in in_file:
            rows = line.strip().split(',')
            guitar = Guitar(rows[0], int(rows[1]), float(rows[2]))
            guitars.append(guitar)

    for guitar in guitars:
        print(guitar)



main()