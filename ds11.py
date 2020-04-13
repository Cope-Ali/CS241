"""
File: ds11.py
Author: Ali Cope
Purpose: This file is a starting point to help you practice list comprehensions.
"""

def get_part1_list():
    """
    Returns a list of the squares of the numbers [0-99], e.g., 0, 1, 4, 9, 16, 25 ...]
    """
    numbers = [x**2 for x in range(100)] # TODO: Change this line to be a list comprehension

    return numbers

def get_part2_list():
    """
    Returns a list of the the numbers [0-99] that are divisible by either 5 or 7
    """
    numbers = [n for n in range(100) if n%5==0 or n%7 == 0] # TODO: Change this line to be a list comprehension

    return numbers

def get_part3_list():
    """
    Filters a list of words to return only those that are at least 4 letters long and contain an 'e'
    """
    old_words = ["tacos", "knowledge", "water", "on", "the", "I", "is", "hilarious", "tie", "coat", "white", "covenants", "phone", "rubric", "send", "restrictions"]

    new_words = [n for n in old_words if len(n)>=4 if n.count("e")>0] # TODO: Change this line to be a list comprehension

    return new_words

def main():
    """
    This function calls the above functions and displays their result.
    """
    print(get_part1_list())
    print(get_part2_list())
    print(get_part3_list())


if __name__ == "__main__":
    main()