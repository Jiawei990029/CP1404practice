MENU = (f"(H)ello\n"
        f"(G)oodbye\n"
        "(Q)uit")

name = input("Enter name: ")
print(MENU)
choice = input(">>> ").upper()
while choice != "Q":
    if choice == "H":
        print(f"Hello {name}")
    elif choice == "G":
        print(f"Goodbye {name}")
    else:
        print("Invalid choice")
    print(MENU)
    choice = input(">>> ").upper()
print("Finished.")