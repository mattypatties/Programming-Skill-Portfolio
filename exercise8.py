"""
Exercise 8: Simple Search - 30 Marks
"""
names=["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"] #create a list
search=("Sam") #fix a variable to "Sam"
if search in names: #check if Sam is in the list
    print(f"The name {search} was found in the list!")
else: #if Sam is not in the list, provide feedback
    print(f"The name {search} was not found in the list.")