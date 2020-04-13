"""
File: ds10.py
Author: Ali Cope
Practice using list manipulation and slicing in Python.
"""

def main():
    numbers = [12, 18, 128, 48, 2348, 21, 18, 3, 2, 42, 96, 11, 42, 12, 18]

    numbers.insert(0,5)
    print(numbers)

    numbers.remove(2348)
    print(numbers)

    newList = [1, 2, 3, 4, 5]
    numbers.extend(newList)
    print(numbers)

    numbers.sort()
    print(numbers)

    numbers.reverse()
    print(numbers)

    print(numbers.count(12))

    print(numbers.index(96))

    half = int(len(numbers)/2)
    length = int(len(numbers))
    print("first half of the list: {}".format(numbers[0:half]))
    print("second half of the list: {}".format(numbers[half:length]))

    newList = numbers[0:len(numbers):2]
    print(newList)

    print(numbers[-5:])

if __name__ == "__main__":
    main()