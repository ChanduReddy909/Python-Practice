print("Welcome to Quiz")
print("Each question has 4 options: A, B, C, D")
print("1 mark for each correct answer")
print("No negative marking")
print()

score = 0
correct_score = 0
wrong_score = 0

questions = {
    'q1' : {"question" : "Which data type is used to store true/false values in Python?", 
            "A" : "int",
            "B" : "str", 
            "C" : "bool",
            "D" : "float",
            "answer" : "C"
        },

    'q2' : {"question" : "Which symbol is used for comments in Python?",
            "A" : "//",
            "B" : "<!-- -->", 
            "C" : "#", 
            "D" : "/**/",
            "answer" : "C"
            }
}

name = input("Enter name: ")
print(f"{name} Now taking Quiz.\n")



for q_id, options in questions.items():
        print(options["question"])

        print("A",options["A"])
        print("B",options["B"])
        print("C",options["C"])
        print("D",options["D"])

        answer = input("Enter option: ").upper()
        if answer == options["answer"]:
            print("Right answer")
            print()    

            score += 1
            correct_score += 1
        else:
            print(f"Wrong answer ❌ Correct is {options['answer']}\n")
            wrong_score += 1  


print("Quiz Finished")
print(f"Name : {name}")
print(f"Score : {score}")
print(f"Correct : {correct_score}")
print(f"Wrong : {wrong_score}\n")     
     

    