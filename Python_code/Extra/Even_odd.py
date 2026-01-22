numbers = int(input("Enter limit: "))
even_numbers = []
odd_numbers = []

for num in range(numbers):
    if num % 2 == 0:
        even_numbers.append(num)
    
    else:
        odd_numbers.append(num)
print()
print(f"Even Numbers: ",  " ".join(map(str, even_numbers)))

print(f"odd Numbers: ", " ".join(map(str, odd_numbers)))

