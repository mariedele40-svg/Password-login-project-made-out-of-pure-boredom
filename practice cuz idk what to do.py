print("Create your password:")
saved_password = input("")

if " " in saved_password:
    print("Password cannot contain spaces.")

elif len(saved_password) < 8:
    print("Password must be atleast 8 characters long.")

else:
    print("Password saved successfully.")

    print("Enter your password to login:")
    entered_password = input("")

    if entered_password == saved_password:
        print("Login successfully.")

    else:
        print("Incorrect password. Please try again.")