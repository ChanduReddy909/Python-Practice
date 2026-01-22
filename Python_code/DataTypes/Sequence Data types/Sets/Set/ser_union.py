""" #problem 1
nums = list(map(int, input("Enter values separated by space: ").split()))

print("Original values:", nums)

unique = set(nums)
print("Unique elements:", unique) """

#problem 2

limit = int(input("Enter range: "))
i = 1
nums = []

while i <= limit:
    value = int(input("Enter value: "))
    nums.append(value)
    i += 1
print(f"All values: {nums}")

unique = set(nums)
print(f"Unique elements: {unique}")
