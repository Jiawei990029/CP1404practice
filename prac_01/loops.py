for i in range(1, 21, 2):
    print(i, end=' ')
print()

# a
for n in range(0, 101, 10):
    print(n, end =' ')
print()

# b
for k in range(20, 0, -1):
    print(k, end=' ')
print()

# c
number = int(input("Number of stars: "))
print("*" * number)
print()

# d
lines = int(input("Number of lines: "))
for h in range(1, lines + 1):
    for t in range(h):
        print("*", end='')
    print()
