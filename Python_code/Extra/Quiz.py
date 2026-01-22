quiz = {
    #question 1
    "What is Python?" : {
        "options" : {
            "A" : "Operating System",
            "B" : "Programming Language",
            "C" : "Web Browser",
            "D" : "Database"
        },
        "Answer" : "B"
        
    },
    #question 2
    "Which keyword is used to define a function in Python?" : {
        "options" : {
            "A" : "function",
            "B" : "define",
            "C" : "def",
            "D" : "fun"
            
        },
        "Answer" : "C"
    },
    #question 3
     "Which data type stores data in key–value pairs?" : {
        "options" : {
            "A" : "List",
            "B" : "Tuple",
            "C" : "Set",
            "D" : "Dictionary"
            
        },
        "Answer" : "D"
    },
    
    #question 4
     "What is the output of 2 + 3 * 2?" : {
        "options" : {
            "A" : "10",
            "B" : "7",
            "C" : "8",
            "D" : "12"
            
        },
        "Answer" : "C"
    },
    
    #question 5
     "Which function is used to take input from the user?" : {
        "options" : {
            "A" : "scan()",
            "B" : "input()",
            "C" : "read()",
            "D" : "get()"
            
        },
        "Answer" : "B"
    },
  
}

right = 0
wrong = 0
score = 0

while True:
    
    for question,data in quiz.items():
        print(question)
        
        
        for option, value in data["options"].items():
            print(f"{option} : {value}")
        print()
        answer = input("Enter answer (A/B/C/D): ").upper()
        
    
        if answer == data["Answer"]:
            print(f"{answer} is right answer.")
            right += 1
            score += 1
            print() 
           
    
        else:
            print(f"Answer is {data['Answer']}")
            wrong += 1
            print()
    break        
        
print("Quiz Completed")
print(f"Right Ansers: {right}\nWrong Answers: {wrong}")
print(f"Your Score: {score} out of {len(quiz)}")
    