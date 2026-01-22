# *args and **kwargs

#1 *args
""" By default, a function must be called with the correct number of arguments.

However, sometimes you may not know how many arguments that will be passed into your function.

*args and **kwargs allow functions to accept a unknown number of arguments.
Arbitrary Arguments - *args

If you do not know how many arguments will be passed into your function, add a * before the parameter name.

This way, the function will receive a tuple of arguments and can access the items accordingly """


# student info with *args
def std(name, course, *address):
    print(f"Name: {name}\nCourse: {course}\nAddress: {address}\n")
    
std("Chandu", "MCA", "Multiplex",  "Marathalli", "Bengaluru") 

# addition of numbers
def addition(*nums):
    total = 0 
    for num in nums:
        total += num
    return total

print("Addition of nums" ,addition(1,2,3,4,5,6,7,8,9))

result = addition(2,4,6,8,10)
print("Addition of Even nums: ",result)

print("Addition of odd nums: ",addition(1,3,5,7,9))

# max number
print()
def maximum(*numbers):
    if len(numbers) == 0:
        return None
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num

print("maximum number: ",maximum(2,4,5,8,1,9,4))    


# **kwargs
""" If you do not know how many keyword arguments will be passed into your function, add two asterisks ** before the parameter name.

This way, the function will receive a dictionary of arguments and can access the items accordingly.

If you do not know how many keyword arguments will be passed into your function, add two asterisks ** before the parameter name.

This way, the function will receive a dictionary of arguments and can access the items accordingly:"""

# example 1
""" def my_function(**myvar):
  print("Type:", type(myvar))
  print("Name:", myvar["name"])
  print("Age:", myvar["age"])
  print("All data:", myvar)

my_function(name = "Tobias", age = 30, city = "Bergen") """
print()
# example 2
def std(stdname, *phone, college = "CIT",**details): # college is default arguments
    print(f"Student Name: {stdname}")
    print(f"College Name: {college}")
    print(f"Phone Number: {phone}\n")
    print("**Other details**")
    for key, value in details.items():
        print(f"{key} : {value}")
    print()    
std("Chandu",9999999,8888888,USN = "1CD24MCA19", Course = "PG", Branch = "MCA", Section = "A", Quota = "Managment")        
std("Chandan",666666,7676776,84848484,USN = "1CD24MCA18", Course = "PG", Branch = "MCA", Section = "A", Quota = "PGCET")        
std("Kiran",10000000,USN = "1CD24MCA41", Course = "PG", Branch = "MCA", Section = "A", Quota = "Managment")        
std("Raju",111111,222222,USN = "1CD24MCA75", Course = "PG", Branch = "MCA", Section = "B", Quota = "Managment")        

