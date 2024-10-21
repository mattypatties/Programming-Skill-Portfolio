"""
Exercise 6: Brute Force Attack - 30 Marks
"""
crrctpass= ("PogiAko123") #set the correct password
while True: 
#while loop with the boolean "true" will loop forever. thus, asking the user for the password until it's correct
    psswrd=input("Enter your password: ") #ask for password
    if psswrd==crrctpass: #check if it's correct
        print("Successfully Logged in")          
        break #if it's correct break the loop
    else:
        print("Password Incorrect") 
        #otherwise if the password is incorrect the loop will run again

    