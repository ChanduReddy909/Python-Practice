contacts = {}

print("1 Add Contact")
print("2 view Contacts")
print("3 Search By Name")
print("4 Delete Contact")
print("5 Update Contact")
print("6 Exit\n")

while True:
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        name = input("Enter Name: ").capitalize()
        number = int(input("Enter Phone Number: "))
        
        contacts[name] = number
        print(f"{name} Added Successfully!")
        print()
        
    elif choice == 2:
        if not contacts:
            print("Contacts Emty")
            
        else:
            
            print("+----------------+----------------+")
            print("| Name           | Number         |")
            print("+----------------+----------------+")

            for name, number in contacts.items():
                print(f"| {name:<14} | {number:<14} |")

            print("+----------------+----------------+")
            print()

    
    elif choice == 3:
        name = input("Enter Name: ").capitalize()
        
        if name in contacts:
            print(f"Name: {name} Number: {contacts[name]} ")
        else:
            print(f"{name} Not Found")
            print()
            
    elif choice == 4:
        name = input("Enter Name: ").capitalize()
        
        if name in contacts:
            contacts.pop(name)
            print(f"{name} Removed")
        
        else:
            print(f"{name} Not Found")
            print()
            
        
    
    
    elif choice == 5:
        name = input("Enter Name: ").capitalize()
        if name in contacts:
            choose = input("Enter (Name/Number): ").lower()
            
            if choose == "name":
                new_name = input("Enter new name: ").capitalize()
                number = contacts[name]
               
                del contacts[name]
               
                contacts[new_name] = number
                print(f"{new_name} Updated successfully!")
            
            elif choose == "number":
                new_number = int(input("Enter new number: "))
                contacts[name] = new_number
                print(f"{new_number} Updated successfully ")
                
            else:
                print("Please enter only name or number")
    
        else:
              print(f"{name} Not found")
            
    elif choice == 6:
        print("Thanks for using.")
        break
    
    else:
        print("Invalid choice")
   
            
        
        
        