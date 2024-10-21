"""
Exercise 3: Biography - 25 Marks advanced
"""
name=input("Enter your full name: ")#user input
ht=input("Enter your hometown: ")#user input 
while True:#using a lopp to ask for a valid number until the user enters one.
    age=input("Enter your age: ")#user input
    if age.isdigit():# the if finction and the "age.isdigit" finds out if the input is all numbers
        break#if the 'if' condition is met or is true, then the loop will break
    else:#if the conditon is false it will ask for a valid number until the use inputs one
        print("Please enter a valid number")
print(f"Name: {name}\nHometown: {ht}\nAge: {age}")
#format printing while using '\n' to print them in seperate lines :)