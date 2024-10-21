"""
Exercise 8: Simple Search - 30 Marks advanced
"""
names=["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]
search=input("Enter a name: ")
if search in names:
    print(f"The name {search} was found in the list!")
else:
    print(f"The name {search} was not found in the list.")