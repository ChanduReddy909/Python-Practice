print("Library Management\n")

print("1. Add Book")
print("2. Remove Book")
print("3. View Books")
print("4. Take Book")
print("5. Return Book")
print("6. Show Receiver's History")
print("7. Show Returning History")
print("8. Exit\n")

library = {
    "Python" : "Avaiable",
    "Java" : "Avaiable",
    "PHP" : "Avaiable",
    "JavaScript" : "Avaiable",

}
person = {}
return_history = {}

while True:
    choice = int(input("Enter your choice: "))

    # 1. Add Book
    if choice == 1:
        book = input("Add Book: ").capitalize()
        if book not in library:
            library[book] = "Available"
            print(f"{book} Added\n")
        else:
            print(f"{book} Already Exists in Library\n")

    # 2. Remove Book
    elif choice == 2:
        book = input("Remove Book: ").capitalize()
        if book in library:
            del library[book]
            print(f"{book} Removed\n")
        else:
            print(f"{book} Not Available\n")

    # 3. View Books
    elif choice == 3:
        if library:
            print("+-------------------------------+")
            print("| Book Name        | Status     |")
            print("+-------------------------------+")
            for book, status in library.items():
                print(f"| {book:<15}  | {status:<10} |")
            print("+-------------------------------+\n")
        else:
            print("Empty Library\n")

    # 4. Take Book
    elif choice == 4:
        name = input("Enter your name: ").capitalize()
        book = input("Enter Book: ").capitalize()
        
        if name in person:
            print(f"{name} has already taken a book ({person[name]}). return it first.\n")
        
        elif book in library:
            if library[book] == "Available":
                library[book] = "Issued"
                person[name] = book
                print(f"{book} Issued to {name}\n")
            else:
                print(f"{book} Already Issued\n")
        else:
            print(f"{book} Not Available in Library\n")

    # 5. Return Book (direct return)
    elif choice == 5:
        name = input("Enter your name: ").capitalize()

        if name in person:
            book = person[name]
            library[book] = "Available"
            return_history[name] = book
            del person[name]
            print(f"{book} Returned Successfully by {name}\n")
        else:
            print("You have not taken any book\n")

    # 6. Receiver's History
    elif choice == 6:
        if person:
            print("Receiver's History")
            print("+--------------------------------+")
            print("| Person Name     | Book Name    |")
            print("+--------------------------------+")
            for name, book in person.items():
                print(f"| {name:<15} | {book:<12} |")
            print("+--------------------------------+\n")
        else:
            print("No one has received a book\n")

    # 7. Returning History
    elif choice == 7:
        if return_history:
            print("Returning History")
            print("+--------------------------------+")
            print("| Person Name     | Book Name    |")
            print("+--------------------------------+")
            for name, book in return_history.items():
                print(f"| {name:<15} | {book:<12} |")
            print("+--------------------------------+\n")
        else:
            print("No return history available\n")

    # 8. Exit
    elif choice == 8:
        print("Thanks for using the Library System\n")
        break

    else:
        print("Invalid Choice\n")
