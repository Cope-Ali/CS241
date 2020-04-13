"""
File: check08a.py
Author: Ali Cope
This checkpoint is intended to help you practice getter and setter functions. 
You will create a class to represent a GPA and then make getters and setters 
to get and set both the value and also the letter grade equivalent.
"""

class GPA:
    def __init__(self):
        self.gpa = 0.0
    
    def get_gpa(self):
        return self.gpa

    def set_gpa(self, gpa):
        if gpa <= 0:
            self.gpa = 0.0
        elif gpa >= 4:
            self.gpa = 4
        else:
            self.gpa = gpa

    def get_letter(self):
        if self.gpa <= 0.99:
            return 'F'
        elif self.gpa <= 1.99:
            return 'D'
        elif self.gpa <= 2.99:
            return 'C'
        elif self.gpa <= 3.99:
            return 'B'
        else:
            return 'A'

    def set_letter(self, grade):
        if grade == 'F':
            self.gpa = 0.0
        elif grade == 'D':
            self.gpa = 1.0
        elif grade == 'C':
            self.gpa = 2.0
        elif grade == 'B':
            self.gpa = 3.0
        elif grade == 'A':
            self.gpa = 4.0
        else:
            pass


def main():
    student = GPA()

    print("Initial values:")
    print("GPA: {:.2f}".format(student.get_gpa()))
    print("Letter: {}".format(student.get_letter()))

    value = float(input("Enter a new GPA: "))

    student.set_gpa(value)

    print("After setting value:")
    print("GPA: {:.2f}".format(student.get_gpa()))
    print("Letter: {}".format(student.get_letter()))

    letter = input("Enter a new letter: ")

    student.set_letter(letter)

    print("After setting letter:")
    print("GPA: {:.2f}".format(student.get_gpa()))
    print("Letter: {}".format(student.get_letter()))

if __name__ == "__main__":
    main()