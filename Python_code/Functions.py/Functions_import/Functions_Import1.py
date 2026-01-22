
# Program 1
""" 
def student(name, age, *address):
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"Address: {address}")
    print()
    
student("Chandu", 22, "Bengaluru", "Marathahalli", "Multiplex")   """

 
#Program 2
""" 
name = "ChanduReddy"
password = "chandu@0011"

def user(name, password):
    while True:
    
        user_name = input("Enter user name: ")
        pssd = input("Enter password: ")
        

        
        if name == user_name and password == pssd:
            print("Login Successfull")
            print(f"Welcome {name}\n")
            break
        else:
            print("Incorrect user name and password\n")
user(name, password) """

# Program 3
# Chicken fry recipe
""" 
def recipe():
    items = ["Tomato", "Onions", "Chilli", "Ginger", "Garlic", "Whole garam masala"]
    
    steps = {
        1 : "Madianate chicken 30 minutes with turmaric and salt",
        2 : "Add oil, whole masala",
        3 : "Add onions, chili, garlic and ginger paste",
        4 : "Tomato paste",
        5 : "Now add madianate chicken",
        6 : "Mix it well wait  5 minutes",
        7: "Add salt, chilli powder, Chicken masala, coriander masala and curd",
        8 : "Add garam masala",
        9 : "Add coriander leaves",
        10 : "Add one lemon"
        
    }
    print("Chicken fry\n")
    print("Required Ingrediants")
    for num, item in enumerate(items, 1):
        print(f"{num} : {item}")
        
    print()
    
    print("Steps for making chicken")
    for num, process in steps.items():
        print(f"{num} : {process}")
    print()  """
    
       
 # Program 4
 
def cal():
    num1 = int(input("Enter number1: "))
    num2 = int(input("Enter number2: "))
    print()
    
    def addition():
        return num1 + num2
        
    def substraction():
        return num1 - num2
    
    def multplication():
        return num1 * num2
    
    def division():
        if num2 == 0:
            return f"{num1} Cannot divide by {num2}"
        else:
            return num1 / num2
        
    
    
    print(f"Addition: {addition()}")
    print(f"Substraction: {substraction()}")
    print(f"Multplication: {multplication()}")
    print(f"Division: {division()}\n")
    
cal()   
cal()
        
        
        
           


        