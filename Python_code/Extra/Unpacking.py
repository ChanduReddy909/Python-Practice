#Unpacking elements using *


# Problem 1
data1 = (5, 10, 15, 20, 25, 30)
first, *middle, last = data1
print(f"first: {first}")
print(f"Middle: {middle}")
print(f"last: {last}")
print()

# Problem 2
data2 = ("ID123", "TEMP", 100, 200, 300, 400)
first, second, *remaining = data2
print(f"first: {first}")
print(f"second: {second}")
print(f"remaining: {remaining}")
print()

# Problem 3
data3 = input("Enter details (name age city country role ...): ").split()

name, age, *remaining_data3 = data3
age = int(age)
print(f"name: {name}")
print(f"age: {age}")
print(f"Remaining: {remaining_data3}")
print()

# Problem 4

order = ("OrderID-991", "Laptop", 55000, "Delivered", "Hyderabad", "India")

product_id, product, price, *other_details = order
details = [product_id] + other_details

print("Product Name:", product)
print("Price:", price)
print("Other Details:", details)







