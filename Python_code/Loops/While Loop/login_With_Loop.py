un = "Chandu12"
pssd = "Chandu@12"
attempt = 0
while  True:
    username = input("Enter user name: ").strip()
    password = input("Enter password: ").strip()
    
    if username == un and password == pssd:
        print("Login Successfull!")
        break
    else:
        print("Incorrect username and password!")
        
        attempt += 1
        
        
        print(f"Attempts left {3 - attempt}")
        
    if attempt == 3:
       print("Account locked due to too many failed attempts.")
       break
    
    
    
    