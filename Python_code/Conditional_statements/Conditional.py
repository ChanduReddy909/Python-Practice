
""" # Example 1
marks = int(input("Enter your marks: "))
print("Your maks are : ", marks)
print("Your result is ")

if marks >90 and marks <= 100:
    print("Grade 'A'")

elif marks > 80 and marks <= 90:
    print("Grade 'B'")

elif marks > 60 and marks <= 80:
    print("Grade 'C'") 

elif marks > 40 and marks <= 60:
    print("Grade 'Average'")

elif marks >= 35 and marks <= 40:
    print("Just Pass")    

elif marks >=0 and  marks < 35:
    print("You are fail")

else:
    print("Invalid marks!")  """   


""" # Exaple 2
new_password = input("Enter new password: ")
re_enter = input("Re-enter the password: ")

if new_password == re_enter:
    print("Your password is matches")
else:
    print("Your password is not matached! please re-enter the password") """    


""" # Example 3

new_user_name = input("Enter new user name: ")
new_password = input("Enter new your password: ")

user_name = input("Enter user name: ")
password = input("Enter password: ")
if new_user_name == user_name and new_password == password:
    print("Login successful!")
else:
    print("Invalid user name and password!")  """    


""" # Exaple 4 
valid_card = "Canara"
pin_code = 1234

card = input("Enter you Bank name: ").title()
if card.strip() == valid_card:
    
    pin = int(input("Enter PIN: "))

    if pin == pin_code:
        print("Access granted, you can withdraw money, ckeck balance")
    else:
        print("Invalid password!")
else:
    print("This machine only support to 'Canara bank!'")        

 """


# Eample 5

#ATM
correct_pin = 2580
balance = 10_000

def ask_int(prompt, min_val=None, max_val=None):
    #Keep asking until the user types a valid integer (optionally in a range).
    while True:
        try:
            value = int(input(prompt))
            if (min_val is None or value >= min_val) and (max_val is None or value <= max_val):
                return value
            print(f"❌  Please enter a number between {min_val} and {max_val}.")
        except ValueError:
            print("❌  Numbers only, please!")

# --- main flow ---------------------------------------------------------------
pin = ask_int("Enter the 4‑digit PIN: ")

if pin == correct_pin:
    print("✅  Access granted")

    while True:
        print("\n-- Menu --")
        print("1. Check balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = ask_int("Enter your choice (1‑4): ", 1, 4)

        if choice == 1:                                    # Check balance
            print(f"💰  Current balance: ₹{balance}")

        elif choice == 2:                                  # Deposit
            amount = ask_int("Enter amount to deposit: ", 1)
            balance += amount
            print(f"✅  ₹{amount} deposited. New balance: ₹{balance}")

        elif choice == 3:                                  # Withdraw
            amount = ask_int("Enter withdrawal amount: ", 1)
            if amount <= balance:
                balance -= amount
                print(f"✅  ₹{amount} withdrawn. New balance: ₹{balance}")
            else:
                print("❌  Insufficient balance.")

        elif choice == 4:                                  # Exit
            print("👋  Thank you! Session ended.")
            break
else:
    print("❌  Invalid PIN")
