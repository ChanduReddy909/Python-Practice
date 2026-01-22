""" password = input("Enter password: ")

has_upper = False
has_lower = False
has_digit = False

    
for char in password:
    if char.isupper():
        has_upper = True
    elif char.islower():
        has_lower = True
    elif char.isdigit():
        has_digit = True




if has_upper and has_lower and has_digit and len(password) > 8:
    print("Strong password!")
    
else:
    if not has_upper:
        print("Missing upper letter!")
    elif not has_lower:
        print("Missing lower letter!")
    elif not has_digit:
        print("Missing Digit")
    elif len(password) < 8:
        print("length must be atleast 8 characters!")
    else:
        print("Weak Password")    

 """


login = {
    "Chandu011": "Chandu@1100"
}

limit = 3

while limit > 0:
    name = input("User Name: ")
    password = input("Enter Password: ")

    if name in login:
        if login[name] == password:
            print("Login Success!")
            break
        else:
            limit -= 1
            print("Incorrect password")
            print(f"{limit} chances left\n")
    else:
        limit -= 1
        print("Username not found")
        print(f"{limit} chances left\n")

if limit == 0:
    print("Account locked. Too many failed attempts.")
