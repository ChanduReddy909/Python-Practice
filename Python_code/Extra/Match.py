""" choice = int(input("Enter your choice: "))

match choice:
    case 1:
        print("Monday")

    case 2:
        print("Tuesday")

    case 3:
        print("Wednesday")

    case 4:
        print("Thursday")    

    case 5:
        print("Friday")

    case 6:
        print("saturday")   

    case 7:
        print("Sunday")  

    case _:
        print("Invalid choice!") 
         
if choice <= 6:
    print("its weekday! do your work")
else:
    print("Its weekend! just chill")   """


marks = int(input("Enter marks: "))

match marks:
    case _ if marks >90 and marks <=100:
        print("Grade A")
        
    case _ if marks >80 and marks <=90:
        print("Grade B")
        
    case _ if marks >70 and marks <=80:
        print("Grade C") 
        
    case _ if marks >40 and marks <=70:
        print("Grade D") 
        
    case _ if marks >=35 and marks <=40:
        print("Just pass")
        
    case _ if marks >=0 and marks <35:
        print("Fail")  
        
    case  _ :
        print("Invalid marks")
        
   
