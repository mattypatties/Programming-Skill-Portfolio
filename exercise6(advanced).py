"""
Exercise 6: Brute Force Attack - 30 Marks advanced
"""
crrctpass= ("PogiAko123") #set the correct password
maxattempts= 5 #set max attempts
attempts= 0 #set the starting attempt to 0
while attempts<maxattempts: # loop until the user reaches 5 attempts
    psswrd=input("Enter your password: ") #ask for password
    if psswrd==crrctpass: #check if it's correct
        print("Successfully Logged in")          
        break #if it's correct break the loop
    else:
        attempts+=1 #if it's incorrect add 1 to attempts
        remainingattempts= maxattempts-attempts 
        #set the remaining attempts by subtracting the attempts to max attempts
        if remainingattempts>0: 
            #inform the user of their remaining attempts
            print(f"Password Incorrect. You have {remainingattempts} remaining attempt(s) left.") 
        else:
            #if remaining attempts is 0. thus, reaching the max attempts, the loop will end. 
            print("Max attempts reached. Authorities have been alerted.")