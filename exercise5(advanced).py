"""
Exercise 5: Days of the Month - 30 Marks advanced
"""
months_days={
        1:31,
        2:28,
        3:31,
        4:30,
        5:31,
        6:30,
        7:31,
        8:31,
        9:30,
        10:31,
        11:30,
        12:31        
        }
mnth=int(input("Enter a month number: ")) #ask for user input
if mnth in months_days: #condition to make sure the user input can actually be found in the dictionary
    if mnth==2: #check if the input is '2' which pertains to February
        leap=input("Is it a leap year, Yes or No? ") #ask if it's a leap year
        if leap=='Yes'.lower(): #check their answer while ignoring capitalization by using ".lower()"
            print("The month of February has 29 days in a leap year.") 
            #if the asnwer is yes, print the number of days in February in a leap year
            
        else:
            print(f"The month of February has {months_days[mnth]} days")
            #otherwise, print the number of days in February in a standard year
    else:
        print(f"The number of days in month {mnth} is {months_days[mnth]}") 
    #if the input is not '2' or February, simply print the month and days
else:
    print("Please enter a valid month number from 1-12")
    
"""
by using nested if else conditions I was able to check whether the user entered the month
of february and if it's a leap year, then coded based on that.
"""