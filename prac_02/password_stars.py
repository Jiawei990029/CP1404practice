def main():
    length = 5
    password = input("What is your password: ")
    while len(password) < length:
        print("Password is not long enough.")
        password = input("What is your password: ")
    password_stars(password)

def password_stars(password):
    print(len(password) * "*")

main()