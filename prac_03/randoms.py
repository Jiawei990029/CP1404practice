import random
dir(random)

print(random.randint(5, 20))  # line 1
print(random.randrange(3, 10, 2))  # line 2
print(random.uniform(2.5, 5.5))  # line 3

# Randomly print an integer between 5 and 20. smallest: 5 largest: 20

# Randomly print an odd number between 3 and 10. smallest: 3 largest: 9. can not print 4

# Randomly print any number between 2.5 and 5.5. smallest: 2.5 largest: 5.5.

print(random.randint(1, 100))