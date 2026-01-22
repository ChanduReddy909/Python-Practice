""" list = [1,2.5,33,False, True, "chandu reddy","xyz"]
print("list is :  ",list)

#append
print("1. Append")
list.append("reddy")
print("append list is : ",list)
print("\n")

#extend
print("2. Extend")
fruits = ["apple", "banana", "cherry"]
cars = ["Ford", "BMW", "Volvo"]
fruits.extend(cars)
print("index list is : ",fruits)
print("\n")

#remove
print("3. Remove")
list.remove("reddy")
print("remove list is : ", list)
print("\n")

#pop
print("4. Pop")
list.pop(2)
print("pop list is : ", list)
print("\n")

#count
print("4. count")
print("count is : ", list.count("chandu reddy"))
print("\n")

#index
print("5. index")
print("index list is ",list.index( "chandu reddy"))
print("\n")

#insert
print("6. Insert") 
list.insert(0,"RSL Reddy")
print("insert list is : ", list)
print("\n")


 #sort
print("7. Sort")
numbers = [2,4,5,1,3,6,8,7]
print("Orginal list : ",numbers)
numbers.sort()
print("sort numbers are : ", numbers)
print("\n")


# reverse()
print("8. Reverse")
alphabets = ['a', 'b', 'c', 'd', 'e', 'f']
print(alphabets)

alphabets.reverse()
print("Reversed alphabets are : ", alphabets)
print("\n")

#clear
print("9. clear")
val1 = [1,2,3,4,5,6]
print("val1 are : ", val1)

val1.clear()
print("clear is empty : ", val1)
print("\n")

#Max Min Sum
nums = [1,2,3,4,5,6,7,8,]
print("Orginal nums are : ", nums)
print("\n")

#1 Max
print("...Max...")
print("Max value is : ", max(nums))
print("\n")

#2 Min
print("...Min...")
print("Min value is : ", min(nums))
print("\n")

#3 Sum
print("...Sum...")
print("Sum are : ", sum(nums))
print("\n")

""" 

""" #****Slcing**** 

print("****Slicing****")

content = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
print("content are : 0", content)

print("\n")
print(content[:])

#odd numbers
print(content[:20:2])

#even numbers
print(content[1:20:2])

print(content[-1:-20:-3])
 """

 
""" nums = [1,2,3,4,5,6]
nums[1:3] = [8,9]
print(nums)

nums1 = [1,2,3,4,5,6]
nums1[1:2] = [7,8]
print(nums1) """

data = []

print("1. Add Name")
print("2. Remove Name")
print("3. Update Name")
print("4. Show Data")
print("5. Exit")

while True:
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
         name = input("Enter name: ").capitalize()
         data.append(name)
         print(f"{name} Added.")
         print()
    
    elif choice == 2:
        name = input("Enter name to remove: ").capitalize()
        
        if name in data:
            data.remove(name)
            print(f"{name} Removed!")
        
        else:
            print(f"{name} Not found")
            print()
            
    elif choice == 3:
        
        name = input("Enter name: ").capitalize()
        
        if name in data:
            index = data.index(name)
            new_name = input("Enter update name: ").capitalize()
            data[index] = new_name
            
            print(f"{name} Updated as {new_name} ")
            print()
        else:
            print(f"{name} Not found")
            
    elif choice == 4:
        print("+------------------+")
        print("|      Names       |")
        print("+------------------+")

        for name in data:
            print(f"| {name:<10} |")

        print("+------------+")

            
    
    elif choice == 5:
        print("Thanks for using.")
        break
    
    else:
        print("Invalid choice")
        
    

   
