# in_file = open("name.txt", "w")
# name = input("Name: ")
# in_file.write(name)
# in_file.close()


# out_file = open("name.txt", "r")
# name = out_file.read()
# out_file.close()
# print(name)


numbers = [17, 42, 400]
number_file = open("numbers.txt", 'w')
for number in numbers:
    number_file.write(f"{number}\n")
number_file.close()

with open("numbers.txt", "r") as out_file:
    number_1 = float(out_file.readline())
    number_2 = float(out_file.readline())
result = number_1 + number_2
print(f"{result:.0f}")


with open("numbers.txt", "r") as all_number_file:
    print(sum(float(line) for line in all_number_file))