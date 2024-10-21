"""
exercise 4: Primitive Quiz - 30 Marks advanced
"""
quiz = {
    "France": "Paris",
    "Germany": "Berlin",
    "Spain": "Madrid",
    "Austria": "Vienna",
    "Georgia": "Tbilisi",
    "Italy": "Rome",
    "Norway": "Oslo",
    "Russia": "Moscow",
    "Sweden": "Stockholm",
    "United Kingdom": "London"
    } #dictionary
correctanswers=0 #set the correct answers to zero
    #assign country and capital to the keys and values respectively
for country, capital in quiz.items(): #use loop and ".items()" to cover all of the keys and values in the dict
    answer=input(f"What is the capital of {country}? ")
    if answer==capital.lower():
        """
        use an if condition to check if the answer is correct and add the .lower() method
        to ignore capitalization
        """
        print(f"Correct! The capital of {country} is {capital}.")
        
        correctanswers+=1 #if the answer is correct it will add a score to 'correctanswers'
    else:
        print(f"Wrong, the capital of {country} is {capital}.")
        #if it's wrong it won't add a score and will reveal the correct answer
print(f"\nQuiz completed! You got {correctanswers} out of {len(quiz)}.")
#print results while using len() method to get the number of item in the dictionary