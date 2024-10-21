"""
Exercise 8: Simple Search - 30 Marks advanced
"""
names=["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"] #set a list
search=input("Enter a name: ") #ask for user input
if search in names: #check if the user input is in the list
    print(f"The name {search} was found in the list!")
else: #if the input is not in the list provide feedback
    print(f"The name {search} was not found in the list.")