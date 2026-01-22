lst = []
print("1.insert\n2.print\n3.remove\n4.append\n5.sort\n6.pop\n7.reverse\n8.exit")



print("Enter 0 to start the program")
while True:
    
    
    choice = int(input("Enter choice: "))
    
    if choice == 0:
        print
        n = int(input("Enter Range: "))
    else:
        print("Invalid choice please choose 0!")
        continue
    
    for _ in range(n):
       cmd = input(" ").split()
    
    if choice == 1:
        
        if cmd[0] == "insert":
            pos = int(input("Enter position: "))
            val = int(input("Enter value: "))
            lst.insert(pos, val)
        
    elif choice == 2:
        if cmd[0] == "print":
           print(lst)
        
    elif choice == 3:
        if cmd[0] ==  "remove":
           lst.remove(int(cmd[1]))
        
    elif choice == 4:
         if cmd[0] == "append":
            lst.append(int(cmd[1]))
        
    elif choice == 5:
        if cmd[0] == "sort":
           lst.sort()
    
    elif choice == 6:
        if cmd[0] == "pop":
           lst.pop()
        
    elif choice == 7:
        if cmd[0] == "reverse":
           lst.reverse()
    
    elif choice == 8:
        break
    
    else:
        print("Invalid choice!")
        
        
        
    