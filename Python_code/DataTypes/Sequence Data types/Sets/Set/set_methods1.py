nums = {1,2,3,4,5,6,7,8,9,10}

print("Original set")
print(' '.join(map(str, sorted(nums))))
print()

print("1 Remove element (remove)")
print("2 Discard element")
print("3 Pop element")
print("4 Add")
print("5 Clear the elements")
print("6 Exit")
print()

while True:
    choice = int(input("Enter 1/2/3/4: "))
    print()

    if choice == 1:
        element = int(input("Enter digit to remove: "))
        try:
            nums.remove(element)
            print(f"{element} removed!")
        except KeyError:
            print(f"{element} not found in set!")

    elif choice == 2:
        element = int(input("Enter digit to discard: "))
        nums.discard(element)
        print(f"{element} discarded (no error if not present)")

    elif choice == 3:
        if nums:
            removed = nums.pop()
            print(f"Popped element: {removed}")
        else:
            print("Set is empty, nothing to pop")
            
    
    elif choice == 4:
        value = int(input("Enter element to add: "))
        if value not in nums:
            nums.add(value)
            print(f"{value} added")
        else:
            print(f"{value} Already exist!")
        
    elif choice == 5:
        if nums:
           nums.clear()
           print("Empty ")
        else:
            print("already empty")
            
        

    else:
        print("Final data:")
        print(' '.join(map(str,sorted(nums))))
        break
