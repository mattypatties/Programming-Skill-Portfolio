"""
Exercise 5: Days of the Month - 30 Marks
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
    #if the condition is met print the month and number of days
    
    print(f"The number of days in month {mnth} is {months_days[mnth]}") 
    
    #if the condition is not met, ask for a valid input
else:
    print("Please enter a valid month number from 1-12")