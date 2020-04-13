"""
File: check09a.py
Author: Ali Cope
This checkpoint is intended to help you practice the syntax of exceptions. 
Assignment: Write a program that prompts the user for a number and then displays back that number multiplied by 2. Your program should continue to reprompt them as long as they enter a string
"""

def main():
    valid_input = False
    while not valid_input:
        try:
            num = int(input("Enter a number: "))
            valid_input = True     
        except ValueError:
            print("The value entered is not valid")

    result = (num * 2)
    print("The result is: {}".format(result))

if __name__ == "__main__":
    main()