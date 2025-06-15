numbers = []
print("Enter 5 numbers.")
for i in range(5):
    number = float(input("Number: "))
    numbers.append(number)
for number in numbers:
    print(number)

print(f"The first number is {numbers[0]}")
print(f"The last number is {numbers[-1]}")
print(f"The smallest number is {min(numbers)}")
print(f"The largest number is {max(numbers)}")
print(f"The average of the numbers is {sum(numbers) / len(numbers):.1f}")


usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
             'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']

name = input("Enter your username: ")
while name not in usernames:
    print("Access denied")
    name = input("Enter your username: ")

print("Access granted")
