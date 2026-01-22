data = {}

print("1 Add")
print("2 View")
print("3 Search")
print("4 Update")
print("5 Delete")
print("6 Analysis")
print("7 Exit\n")

while True:
    
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        name = input("Enter Name: ")
        roll = int(input("Enter Roll Number: "))
        marks = int(input("Enter marks: "))

        if roll in data:
           print("Roll number already exists! Use Update option instead.\n")
        else:
           data[roll] = {"name": name, "marks": marks}
           print("Student added.\n")
        
        
        
    elif choice == 2:
        if not data:
            print("Student data is empty!")
        else:
            print("Students Information")
            print("_" * 20)
            for roll, info in data.items():
                print(f"Roll: {roll}")
                print(f"Name: {info['name']}")
                print(f"marks: {info['marks']}")
                print("_" * 20)
            print()
            
    elif choice == 3:
        roll = int(input("Enter Roll Number to search: "))
        if roll in data:
            info = data[roll]
            print(f"Roll: {roll}")
            print(f"Name: {info['name']}")
            print(f"marks: {info['marks']}")
            print("_" * 20)
            print()
        else:
            print(f"{roll} Not found")
            
    elif choice == 4:
        roll = int(input("Enter Roll Number to update: "))
        print()
        
        if roll in data:
            updated_marks = int(input("Enter new marks: "))
            
            data[roll] ["marks"] = updated_marks
            print("Marks updated successfully.")
        else:
            print(f"{roll} not found!")
            
    elif choice == 5:
        roll = int(input("Enter Roll Number to remove: "))
        
        if roll in data:
            data.pop(roll) # or del data[roll]
            print("Student removed successfully.")
            print()
        else:
            print(f"{roll} Not found. so cannot delete,")
            print()
            
    elif choice == 6:
        
        print("1 Topper")
        print("2 First class")
        print("3 Avearage")
        print("4 Fail")
        
        choose = int(input("Choose any one: "))
        
        if choose == 1:
            if not data:
                print("No students data available.")
            else:
                highest = max(info["marks"] for info in data.values())

                print("Toppers")
                for roll, info in data.items():
                   if info["marks"] == highest:
                     print(f"Name  : {info['name']}")
                     print(f"Marks : {info['marks']}")
                     print("_" * 20)
                    
        elif choose == 2:
            
            print("Students with marks > 70.")
            found = False
            
            for roll, info in data.items():
                if info["marks"] > 70:
                    print(f"Roll  : {roll}")
                    print(f"Name  : {info['name']}")
                    print(f"Marks : {info['marks']}")
                    print("_" * 20)
                    found = True
                    
                if not found:
                  print("No students scored above 80.\n")
            else:
                print()
                
        elif choose == 3:
            
            marks_list = [info["marks"] for info in data.values()]
            avg = sum(marks_list) / len(marks_list) 
            
            
            print(f"Class Average: {avg: .2f}\n")
            print("Average students\n")
            
            for roll, info in data.items():
                if info["marks"] >= avg:
                    print(f"Roll  : {roll}")
                    print(f"Name  : {info['name']}")
                    print(f"Marks : {info['marks']}")
                    print("_" * 20)
            print()
            
        elif choose == 4:
            pass_marks = 35
            found = False
            
            for roll, info in data.items():
                if info["marks"] < pass_marks:
                    print(f"Roll  : {roll}")
                    print(f"Name  : {info['name']}")
                    print(f"Marks : {info['marks']}")
                    print("_" * 20)
                    found = True

            if not found:
                print("No failed students.\n")
            else:
                print()
        else:
            print("Invalid choose")
            
    elif choice == 7:
        break
    
    else:
        print("Invalid choice!")
            
        