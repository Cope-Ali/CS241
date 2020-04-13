"""
File: check09b.py
Author: Ali Cope
This checkpoint is intended to help you practice the syntax of exceptions.
Assignment: Write a program that computes the value of 1/n for different values of n.
"""

class NegativeNumberError(Exception):
    def __init__(self,message):
        super().__init__(message)

def get_inverse(n):
    if int(n) < 0:
        raise NegativeNumberError("The number must be positive")
    elif not n.isnumeric():
        raise ValueError("The value must be a number")
    elif int(n) == 0:
        raise ZeroDivisionError ("Error: Cannot divide by zero")
    else:
        return 1/float(n)

def main():
    num = input("Enter a number: ")

    try:
        inverse = get_inverse(num)
        print("The result is: {}".format(inverse))
  
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()