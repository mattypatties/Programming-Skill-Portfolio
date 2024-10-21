"""
Exercise 10: Is it even? - 35 Marks
"""
#create a function to check if the number is even or odd
def evenorodd(number):
    if number % 2==0:
        return f"The number {number} is even"
    else:
        return f"The number {number} is odd"
    
# main() function is to ask for user input and call the evenorodd function
def main():
    number=int(input("Please enter a number: ")) #user input
    result=evenorodd(number) #call evenorodd fuction to check if it's even or odd
    print(result)

#this is so that when the code is ran directly it will call the main() function
if __name__ == "__main__":
    main()