# Practical 07

# I am a Python beginner, try to be better.
## some nice code(I think)

def get_valid_number_players():
    number = int(input(prompt))
    while number < 1 or number > 10:
        print("Invalid input. Please enter a number between 1 and 10.")
        number = int(input(prompt))
    return number

with open('projects.txt', 'w') as in_file:
     in_file.write("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage\n")
     for project in projects:
         new_line = f"{project.name}\t{project.date}\t{project.priority}\t{project.cost}\t{project.percentage}\n"
         in_file.write(new_line)

def __lt__(self, other):
    return self.year < other.year

Programming Patterns page: https://github.com/dashboard
CP1404 Practicals: https://github.com/Jiawei990029/CP1404practice