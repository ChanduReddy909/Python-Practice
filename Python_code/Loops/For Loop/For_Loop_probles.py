""" # 1.printing 1 t0 100
print("1. 1 to 100 )
for i in range(1, 101):
    print(i) """

""" # 2.Multiplication
print("2. multiplication\n")
num = int(input("Enter a number: "))

for table in range(1, 11):
   result = num * table
   print(f"{num} x {table} = {result}") # or print(f"{num} x {table} =", result) """

""" # 3. Even or Odd numbers with exit
while True:
    choice = input("Do you want Even, Odd, or Exit: ").strip().lower()
    
    if choice == "even": 
        print("\nEven numbers:")
        for i in range(1, 10):
            if i % 2 == 0:
                print(i, end=" ")
        print("\n")

    elif choice == "odd":
        print("\nOdd numbers:")
        for i in range(1, 10):
            if i % 2 != 0:
                print(i, end=" ")
        print("\n")

    elif choice == "exit":
        print("Exiting program... thanks for using")
        break  

    else:
        print("Invalid choice! Please type Even, Odd, or Exit.\n") """


  

# 4.  Sum of numbers
n = int(input("Enter a number: "))
total = 0
for i in range(1, n+1):
    total +=i
    print(f"After adding {i}, sum = {total}")

print(f"the sum of nubers from 1 to {n} is : {total}")    


print("  ")

for i in range(1, 8):
    print("#" * i)
    
print(" ")   
for j in range(8):
    for k in range(8):
        print("#", end=" ")
    print(" ")
 
print(" ")   
num = int(input("Enter a number: "))
for i in range(1, 11):
    print(f" {num} x {i} = {num * i}")
    #print(num, "x", i,"=", num * i)
    
    
print(" for loop")

for i in range(1, 11):
    print(i)
    
print("while loop ") 
n = 1
while (n < 11):
    print(n)
    n += 1
    
print(" ")
print(" Reverse for loop")
for i in range(10,0, -1):
    print(i)
    
print(" ")
print("Reverse while loop")
n = 10
while (n > 0):
    print(n)
    n -= 1
      


print(" ")
print("Even and Odd sum")
even_sum = 0
odd_sum = 0

for i in range(0,101):
    if i % 2 == 0:
        even_sum += i
    else:
        odd_sum += i
print("Even sum is: ", even_sum)
print("odd sum is: ", odd_sum)            


print(" ")
print("Loop through the countries and extract all the countries containing the word land.")

countries = [
    'Finland',
    'Iceland',
    'Ireland',
    'Netherlands',
    'New Zealand',
    'Poland',
    'Swaziland',
    'Switzerland',
    'Thailand',
    'Liechtenstein'
]

country_land = []

for con in countries:
    if 'land' in con:
        country_land.append(con)

print("Countries containing 'land':", country_land)



   