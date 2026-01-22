def grade(marks):
    if marks > 100 or marks < 0:
        return marks, "Invalid"
    elif marks > 90:
        return marks, "Grade A"
    elif marks > 75:
        return marks, "Grade B"
    elif marks > 50:
        return marks, "Grade C"
    else:
        return marks, "Fail"

while True:
    # Ask marks
    marks = int(input("Enter marks: "))
    marks, result = grade(marks)
    print(f"{marks} are {result}\n")
    
    # Nested loop for repeat question
    while True:
        repeat = input("Do you want to repeat (yes/no): ").strip().lower()
        if repeat == 'yes':
            # Break inner loop, continue outer loop (ask marks again)
            break
        elif repeat == 'no':
            # Break both loops and end program
            print("Program ended.")
            exit() # exit uesd for stop all the loops in file
        else:
            # Invalid input → stay in inner loop
            print("Invalid choice. Please type 'yes' or 'no'.")
            # continue inner loop without asking marks again
