#syntax = variable name = [expression if condition for i tem in sequence ]

print("With list comparision")
nums = [1,2,3,4,5,6,7,8,9,10]
even = [x for x in nums if x % 2 == 0]
odd  = [x for x in nums if x % 2 != 0]
print(even)
print(odd)
print()

print("Without list comparision")
even_loop = []
odd_loop = []

for num in nums:
    if num % 2 == 0:
        even_loop.append(num)
    else:
        odd_loop.append(num)
print(even_loop)
print(odd_loop)

print()
list = [f"{x} is Even" if x % 2 == 0 else f"{x} is Odd" for x in range(1,10+1)]
print(list)