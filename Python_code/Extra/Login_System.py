account = {
            'ChanduReddy' : 'chandu@0011' 
            }
     
max_attempt = 3
attempt = 0

while attempt < max_attempt:
    name = input("Enter user name: ")
    password = input("Enter password: ")

    
    if name in account:
        if  password == account[name]:
            print(f"Login successfull - welcome, {name}")
            break
        else:
            attempt +=1
            print(f"Incorrect password. attempts left: {max_attempt - attempt}")
    else:
        attempt +=1
        print(f"Username {name} not found. Attempts left: {max_attempt - attempt}")
        
else:
    print("Too many failed attempts. Try again later")



