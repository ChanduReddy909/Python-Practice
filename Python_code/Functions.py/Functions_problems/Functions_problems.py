""" #Addition of two numbers
print("Addition of two numbers")
def add_two_numbers(num1, num2):
    print(f"Num1: {num1}")
    print(f"Num2: {num2}")
    result = num1 + num2
    return result
    

num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))
result = add_two_numbers(num1, num2) 
print(f"{num1} + {num2} = {result}")
 """

""" # Check even or odd
print("Check even or odd")

def even_odd(num):
    if num % 2 == 0:
        print(f"{num} is even")
    else:
        print(f"{num} is odd")

num = int(input("Enter number: "))
even_odd(num) """

# 3. Find square of a number
""" print("3. Find square of a number")

def sqaure(num):
    result = num * num
    return result

num = int(input("Enter number: "))
answer = sqaure(num)
print(f"Square of {num} is {answer}") """

#4. Check voting eligibility
""" print("4. Check voting eligibility")

def voting_eligiblity(age):
    if age > 18:
        print("You are eligible for voting")

    elif age == 18:
        print("Now you can apply for voter id ")    
    else:
        print("You are not eligible for voting")
age = int(input("Enter your age: "))
voting_eligiblity(age) """  

#5. Find total of a list
""" print("5. Find total of a list")
def total(limit):
    maximum = 0
    for i in range(limit+1):
        maximum += i
    return maximum
limit = int(input("Enter range of numbers: "))
answer = total(limit)
print(f"The sum of {limit} is {answer}")    
 """

#6. Find largest number in a list
""" print("6. Find largest number in a list")
def largest(nums):
    return max(nums)

maximum = largest([1,5,2,8,10,4])
print(f"The largest number is {maximum}") """

# 7. Count passed students
""" print("7. Count passed students")
def passed_students(marks):
    passed = 0
    failed = 0
    for mark in marks:
        if mark > 35:
            passed += 1
    
        else:
            failed += 1

    print(f"Passed students are: {passed}")        
    print(f"Failed students are {failed}")
passed_students([10, 45, 66, 34, 35, 90])
"""

# 8 Reverse a string
""" print("8 Reverse a string")
def reverse_string(word):
    data = ""
    for char in word:
        data = char + data
    print(f"The reverse string is: {data}")    
word = input("Enter word: ")
reverse_string(word) """

#9. Remove duplicates from a list
print("9. Remove duplicates from a list")
def duplicate(nums):
    print(f"Orginal elemets are: {nums}")
    unique = set(nums)
    return unique
result = duplicate([2,3,1,5,4,2,3,5,5,5])
print(f"Unique elements are: {result}")    


