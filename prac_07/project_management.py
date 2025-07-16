"""
project
Estimate: 30 minutes
Actual:   20 minutes
"""

import datetime
from project import Project

def main():
    MENU = ("- (L)oad projects\n"
            "- (S)ave projects \n"
            "- (D)isplay projects \n"
            "- (F)ilter projects by date\n"
            "- (A)dd new project\n"
            "- (U)pdate project\n"
            "- (Q)uit")

    print("Welcome to Pythonic Project Management")
    projects = []
    with open('projects.txt', 'r') as out_file:
        out_file.readline()
        for line in out_file:
            row = line.strip().split('\t')
            project = Project(row[0], row[1], int(row[2]), float(row[3]), int(row[4]))
            projects.append(project)
    print(f"Loaded {len(projects)} projects from projects.txt")
    print(MENU)
    choice = input(">>> ").lower()
    while choice != "q":
        if choice == "d":
            display_projects(self.percentage)


def display_projects(percentage):
    for project in projects:
        if percentage != 100:
            print(project)
        else:
            print(project)


main()