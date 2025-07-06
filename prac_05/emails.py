"""
emails
Estimate: 10 minutes
Actual:   30 minutes
"""

def main():
    name_to_email = {}
    email_address = input("Email: ")
    while email_address != "":
        name = take_name_from_email(email_address)
        if name == "no":
            name = input("Name:")
            name_to_email[name] = email_address
        else:
            name_to_email[name] = email_address
        email_address = input("Email: ")

    for name, email in name_to_email.items():
        print(f"{name} ({email})")

def take_name_from_email(email_address):
     user_name = email_address.split('@')
     full_name = user_name[0].split('.')
     name = f"{full_name[0]} {full_name[1]}".title()

     user_confirm = input(f"Is your name {name}? (Y/n) ")
     if user_confirm == "Y" or user_confirm == "":
         return name
     else:
         return "no"

main()