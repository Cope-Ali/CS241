"""
File ds05.py
Author: Ali Cope
This is an excercise in how to use Lists as Stacks for python. 
This program will read a file, enter the contents into a list
and determine if the braces in the file are balanced.
"""
stack = []

def test(brace):
    if len(stack)>0:
        top = stack.pop()
        if top == "(" and brace == ")":
            #print("Match")
            return 1
        if top == "[" and brace == "]":
           # print("Match")
            return 1
        if top == "{" and brace == "}":
           # print("Match")
            return 1
        else:
            #print("No Match")
            return 0
        return 1    
    else:
        #print ("Not balanced")
        return 0

def prompt_filename():
    filename = input("File: ")
    return filename

def get_file(filename):
    f = open(filename, "r")
 
    for line in f:
        for brace in line:
            if brace == "(" or brace == "{" or brace == "[":
                stack.append(brace)
            elif brace == ")" or brace == "}" or brace == "]":
               # print(stack)
                match = test(brace)
                if match == 0:
                    print("Not balanced") 
                    return

           
    f.close()    
    if len(stack) == 0:
        print("Balanced")
    else:
        print("Not balanced")

def main():
    filename = prompt_filename()
    get_file(filename)
    return


#used to call the main function
if __name__ == "__main__":
    main()