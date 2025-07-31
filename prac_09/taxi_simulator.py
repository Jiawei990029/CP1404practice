from prac_09.taxi import Taxi
from prac_09.silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose taxi, d)rive"

def main():
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    current_taxi = None
    total_bill = 0.0

    print("Let's drive!")
    print(MENU)
    choice = input(">>> ").lower()

    while choice != "q":
        if choice == "c":
            current_taxi = choose_taxi(taxis)


def choose_taxi(taxis):
    print("Taxis available: ")
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")
    try:
        choice = int(input("Choose taxi: "))
        if 0 <= choice < len(taxis):
            return taxis[choice]
        else:
            print("Invalid taxi choice")
    except ValueError:
        print("Invalid taxi choice")
    return None


main()