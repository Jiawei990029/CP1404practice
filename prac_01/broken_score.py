"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

# : Fix this!

score = float(input("Enter score: "))
if score < 0 or score > 100:
    print("Invalid score")
else:
    if score < 50:
        print("Bad")
    elif score < 90:
        print("Passable")
    elif score >= 90:
        print("Excellent")
