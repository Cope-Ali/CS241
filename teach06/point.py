"""
File: point.py
Author: Ali Cope
Create the Point class containing and x (float) and y (float)
"""
class Point():
    def __init__(self):
        self.x = 0.0
        self.y = 0.0

    def prompt_for_point(self):
        self.x = float(input("Enter x: "))
        self.y = float(input("Enter y: "))

    def display(self):
        """
        """
        print("({},{})".format(self.x, self.y))