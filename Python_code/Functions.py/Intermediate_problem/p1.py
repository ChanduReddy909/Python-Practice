#1 Check number details like positive and Negative even or odd
def even_odd():
    number = int(input("Enter number: "))
    
    if number == 0: # retun zero if number equals to 0
        return number,"Zero"
        
    elif number > 0:  # greater than 0 means Positive
        if number % 2 == 0: # like 5 % 2 == 0(Remainder)
            return number,"Positive Even" 
        else:
            return number, "Positive Odd"
            
    else:  # return negative result if number less than zero
        if number % 2 == 0:
            return number, "Negative even"
        else:
            return number,"Negative odd"
           
number, result = even_odd() # assing input number into {number} and result as output into{result}

print(f"{number} is {result}") # displaying both user input number and result 