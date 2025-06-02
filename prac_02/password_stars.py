def main():
    length = 5
    password = get_password(length)
    password_stars(password)

def get_password(length):
    password = input("What is your password: ")
    while len(password) < length:
        print("Password is not long enough.")
        password = input("What is your password: ")
    return password


def password_stars(password):
    print_style = "*"
    print(len(password) * print_style)

main()