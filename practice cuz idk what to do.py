while True:
    print("Create your password:")
    saved_password = input("")

    if " " in saved_password:
        print("Password cannot contain spaces.\n")
    
    elif len(saved_password) < 8:
        print("Password must be 8 characters or more.\n")
    
    else:
        print("Password saved successfully.\n")
        break





while True:
    print("Enter your password to login:")
    entered_password = input("")

    if saved_password == entered_password:
        print("Login successfully.")
        break
 
    
    else:
        print("Incorrect password. Please try again.\n")
        
     
