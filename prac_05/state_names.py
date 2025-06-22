"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""
from Tools.scripts.make_ctype import values

# Reformat this file so the dictionary code follows PEP 8 convention
CODE_TO_NAME = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory", "WA": "Western Australia",
                "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania", "SA": "South Australia"}
print(CODE_TO_NAME)

max_keys_length = max(len(key) for key in CODE_TO_NAME.keys())
max_values_length = max(len(value) for value in CODE_TO_NAME.values())
for name in CODE_TO_NAME:
    print(f"{name:{max_keys_length}} is {CODE_TO_NAME[name]:{max_values_length}}")

state_code = input("Enter short state: ").upper()
while state_code != "":
    # if state_code in CODE_TO_NAME:
    try:
        print(state_code, "is", CODE_TO_NAME[state_code])
    # else:
    except KeyError:
        print("Invalid short state")
    state_code = input("Enter short state: ").upper()
