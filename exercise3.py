"""
Exercise 3: Biography - 25 Marks
"""
print("User Info:")
user= { # create a dictionary, basically it's like where you store all of your variables
"Name": "Mathias S. Rivera",
"Hometown": "Bulakan, Bulacan, Philippines",
"Age": 18
}
print(f"Name: {user['Name']}\nHometown: {user['Hometown']}\nAge: {user['Age']}")

"""To print every values in seperate lines, we can use \n inside an f-string.
Basically, \n will put your next value in a new line. Therefore, everytime I use
\n, the next value will be printed in a seperate line."""