"""
project
Estimate: 30 minutes
Actual:   20 minutes
"""

from datetime import datetime
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

        if choice == "l":
            load_filename = input("Which file do you want to load? ")
            load_file(load_filename)
            print(MENU)
            choice = input(">>> ").lower()

        elif choice == "s":
            save_choice = input("Which file do you want to save? ").lower()
            save_file(save_choice, projects)
            print(MENU)
            choice = input(">>> ").lower()

        elif choice == "d":
            display_projects(projects)
            print(MENU)
            choice = input(">>> ").lower()

        elif choice == "f":
            filter_project(projects)
            print(MENU)
            choice = input(">>> ").lower()

        elif choice == "a":
            add_project(projects)
            print(MENU)
            choice = input(">>> ").lower()

        elif choice == "u":
            update_project(projects)
            print(MENU)
            choice = input(">>> ").lower()

    save_choice = input("Would you like to save to projects.txt? ").lower()
    save_file(save_choice, projects)
    print("Thank you for using custom-built project management software.")


def save_file(save_choice, projects):
    if "no" in save_choice:
        pass
    elif "yes" in save_choice:
        with open('projects.txt', 'w') as in_file:
            in_file.write("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage\n")
            for project in projects:
                new_line = f"{project.name}\t{project.date}\t{project.priority}\t{project.cost}\t{project.percentage}\n"
                in_file.write(new_line)
    else:
        pass

def load_file(load_filename):
    projects = []
    with open(load_filename, 'r') as out_file:
        out_file.readline()
        for line in out_file:
            row = line.strip().split('\t')
            project = Project(row[0], row[1], int(row[2]), float(row[3]), int(row[4]))
            projects.append(project)
    print(f"Loaded {len(projects)} projects from projects.txt")

def filter_project(projects):
    input_date = input("Show projects that start after date (dd/mm/yy): ")
    filter_date = datetime.strptime(input_date, "%d/%m/%Y")
    for project in projects:
        if project.compare_data >= filter_date:
            print(project)

def add_project(projects):
    print("Let's add a new project")
    name = input("Name: ")
    date = input("Start date (dd/mm/yy): ")
    priority = int(input("Priority: "))
    cost = int(input("Cost estimate: $"))
    percentage = int(input("Percent complete: "))
    project = Project(name, date, priority, cost, percentage)
    projects.append(project)

def update_project(projects):
    for i in range(len(projects)):
        print(f"{i} {projects[i]}")
    project_choice = int(input("Project choice: "))
    print(projects[project_choice])
    new_percentage = int(input("New Percentage: "))
    projects[project_choice].percentage = new_percentage
    new_priority = input("New Priority: ")
    try:
        projects[project_choice].priority = int(new_priority)
    except ValueError:
        pass

def display_projects(projects):
    projects.sort()
    print("Incomplete projects:")
    for project in projects:
        if 0 < project.percentage < 100:
            print(f"  {project}")
    for project in projects:
        if project.percentage == 0:
            print(f"  {project}")
    print("Completed projects:")
    for project in projects:
        if project.percentage == 100:
            print(f"  {project}")

main()