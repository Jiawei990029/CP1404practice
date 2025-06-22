HEX_COLOURS = {"Absolute Zero": "#0048ba", "Baby Blue": "89cff0", "Banana Yellow": "#ffe135", "Black": "#000000",
               "Bittersweet Shimmer": "#bf4f51", "Brick Red": "#cb4154", "Bright Green": "#66ff00", "Bulgarian Rose": "#480607",
               "Cadet Blue": "#5f9ea0", "Celadon": "#ace1af"}

colour_name = input("Enter colour name: ").title()
while colour_name != "":
    try:
        print(f"{colour_name}'s code is {HEX_COLOURS[colour_name]}")
    except KeyError:
        print("Invalid colour name")
    colour_name = input("Enter colour name: ").title()