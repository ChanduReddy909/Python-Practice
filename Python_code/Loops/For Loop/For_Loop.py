
""" #1. list with for loop

lists = ['apple', 'banana', 'cherry']
print(lists)
for i in lists:
    print("list in for loop is: ", i) """

""" #2. string with for loop

name = "chandu"
for names in name:
    print(names) """

""" #3.1 The break statement
fruits = ['apple', 'banana', 'cherry', 'dragon', 'grapes', 'kiwi', 'mango']
print("Before break is: ", fruits) 

for fruit in fruits:
 print("After break: ",fruit)
 if fruit == 'dragon':
    break """
 
#3.2 The break statement
""" print("Break statement")
numbers = [1,2,3,4,5,6,7,8,9]
print("\norginal numbers are: ", numbers)
print("after break numbers are: ")


for num in numbers:
   print(num)
   if num == 6:
     break """
  


#4. Continue statement
""" print("4. continue statement")
drinks = ["Fanta", "Slice", "Frooti", "Sprite", "Mazaa"]
print("\nOriginal drinks are:", drinks)

print("Drinks before continue:")
for drink in drinks:
    if drink == "Slice":
        print("After continue drinks are:")
        continue
    print(drink) """


""" #5. Pass statement
print("5. pass statement")
for values in range(2, 10, 2):
    pass """


""" #6. Nested Loop

for num1 in range(1, 10):
    for num2 in range(2,8):
        print(num1, num2) """

""" data = {"name" : "Chandu", "age" : 23, "Branch" : "MCA"}

for dat in data:
    print(dat, ":", data[dat]) """



labels = ["Name", "Age", "Branch"]
user_data = []

# Input values
for label in labels:
    value = input(f"Enter your {label}: ")
    user_data.append(value)

# Display
print("\nUser Details:")
for i in range(len(labels)):
    print(f"{labels[i]}: {user_data[i]}")



