"""
File: ds09.py
Author: Ali Cope
Use Hash Tables (sets and dictionaries) in Python to solve problems.
Assignment: Write a program to read through a census file and keep track of the number of people in different education levels.
"""

def get_filename():
    name = input("Please enter a filename: ")
    return name

def readFile(filename):
    #create hash table
    education_level = {}
    f = open(filename, "r")
    for line in f:
        x = line.split(",")
        education = x[3]
        if education in education_level:
            education_level[education] += 1
        else: 
            education_level[education] = 1

    f.close()
    return education_level
def main():
    file = get_filename()
    results = readFile(file)
    for level, number in results.items():
        print("{} -- {}".format(number, level))

if __name__ == "__main__":
    main()