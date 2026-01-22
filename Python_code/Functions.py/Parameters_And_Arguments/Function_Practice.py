#Function types
print("Function Types\n")

#1 Without parameter and without return value
print("1 Without parameter and without return value")
def message():
    print("Login Success!")
    print("Welcome to application\n")
message()    

#2 Without parameter and with return value
print("2 Without parameter and with return value")

def sum_of_nums():
    sum = 0
    for i in range(0, 11):
        sum += i
    return sum
answer = sum_of_nums()    
print(f"Sum of 10 numbers is: {answer}\n")    

#3 with parameter and without retuen value
print("3 with parameter and without retuen value")
def user(name, gender):
    if gender == "M":
        print(f"Welcome Mr. {name}")
    elif gender == "F":
        print(f"Welcome Mrs. {name}")
        
    else:
        print("Incorrect gender type. Please enter only (M/F)")
       
       
name = input("Enter name: ").capitalize()
gender = input("Enter your gemder (M/F): ")
user(name, gender)

# 4 with parameter and with return value
print()
print("4 with parameter and with return value")

def add(a,b):
    total = a + b
    return total

result = add(2,3)
print(result)



# calculator using nested functions 
def cal(a, b):
    def adds():
        return a + b
    
    def subs():
        return a - b
    
    def mul():
        return a * b
    
    def dev():
        return a / b

    # return ALL inner functions
    return adds, subs, mul, dev


# call outer function and catch inner functions
add_fn, sub_fn, mul_fn, div_fn = cal(10, 10)

# print results OUTSIDE the outer function
print("Addition:", add_fn())
print("Subtraction:", sub_fn())
print("Multiplication:", mul_fn())
print("Division:", div_fn())

    
    



