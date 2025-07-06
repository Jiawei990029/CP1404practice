from prac_06.guitar import Guitar

def main():
    guitar1 = Guitar("Gibson L-5 CES", 1922, 16035.40)
    guitar2 = Guitar("Another Guitar", 2013, 16035.40)

    age1 = guitar1.get_age(guitar1.year)
    age2 = guitar2.get_age(guitar2.year)
    print(f"Expected 103. Got {age1}")
    print(f"Expected 12. Got {age2}")
    print(f"Expected True. Got {guitar1.is_vintage(age1)}")
    print(f"Expected False. Got {guitar2.is_vintage(age2)}")

main()