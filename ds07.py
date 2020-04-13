"""
File: ds07.py
Author: Ali Cope
This purpose of this program is to use recursion to calculate the fibonacci number. The function will take just the nth number that we are looking for in fibonacci and return the result
"""
#first fibonacci number



def fib(nth):
    """
    fib function takes an index and returns the fibonacci number using recursion
    """
    if (nth <= 1):
       return 1
    return fib(nth-1) + fib(nth-2)

def main():
    """
    main function will prompt user for index and print result
    """
    #get nth number from user
    index = int(input("Enter a Fibonacci index:"))
    print("The Fibonacci number is: {}".format(fib(index-1)))

if __name__ == "__main__":
    main()