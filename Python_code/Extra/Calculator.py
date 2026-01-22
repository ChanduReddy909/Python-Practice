""" print("Calculator 1\n")

print("----- Simple Calculator -----\n")

number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))
print()

print("1. Addition")
print("2. Substaction")
print("3. Multiplication")
print("4. Division")
print("5. Modulers")
print("6. Reminder")
print("7. Exponential")
print("8. Exit")

while True:
    choice = int(input("Enter your choice: "))
    
    if choice < 1 or choice > 8:
        print("Invalid choice!")
        continue
        
    # Addition
    if choice == 1:
        print(f"{number1} + {number2} = {number1 + number2}")
        print()
        
    # Substarction 
    elif choice == 2:
        print(f"{number1} - {number2} = {number1 - number2}")
        print()  
        
    # Multiplication
    elif choice == 3:
        print(f"{number1} * {number2} = {number1 * number2}")
        print() 
        
    # Division
    elif choice == 4:
        if number2 ==0:
            print(f"{number1} Cannot divide by zero")
            print()
            
        else:
            print(f"{number1} / {number2} = {number1 / number2}")
            print()
    
    #  Modulers      
    elif choice == 5:
        print(f"{number1} // {number2} = {number1 // number2}")
        print()
    
    # Reminder    
    elif choice == 6:
         print(f"{number1} % {number2} = {number1 % number2}")
         print()
     
    # Exponential     
    elif choice == 7:
         print(f"{number1} ** {number2} = {number1 ** number2}")
         print()
        
    elif choice == 8:
        print("Calculator closed. Thank you!")
        break
    
 """

print("Calculator 2")
print("----- Simple Calculator -----\n")

print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Floor Division")
print("6. Modulus")
print("7. Exponential")
print("8. Exit\n")

while True:
    choice = int(input("Enter your choice: "))

    if choice == 8:
        print("Calculator closed. Thank you!")
        break

    if choice < 1 or choice > 8:
        print("Invalid choice!\n")
        continue

    number1 = int(input("Enter first number: "))
    number2 = int(input("Enter second number: "))
    print()

    if choice == 1:
        print(f"{number1} + {number2} = {number1 + number2}")

    elif choice == 2:
        print(f"{number1} - {number2} = {number1 - number2}")

    elif choice == 3:
        print(f"{number1} * {number2} = {number1 * number2}")

    elif choice == 4:
        if number2 == 0:
            print("Cannot divide by zero")
        else:
            print(f"{number1} / {number2} = {number1 / number2}")

    elif choice == 5:
        if number2 == 0:
            print("Cannot divide by zero")
        else:
            print(f"{number1} // {number2} = {number1 // number2}")

    elif choice == 6:
        if number2 == 0:
            print("Cannot divide by zero")
        else:
            print(f"{number1} % {number2} = {number1 % number2}")

    elif choice == 7:
        print(f"{number1} ** {number2} = {number1 ** number2}")

    print()

