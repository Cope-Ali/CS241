"""
File: check08b.py
Author: Ali Cope
This checkpoint is intended to help you practice properties. You will start with the getters and 
setters you created in checkpoint A and convert them to properties.
"""

class GPA:
    def __init__(self):
        self._gpa = 0.0
        self._letter = 'F'
    
    

    def _get_gpa(self):
        return self._gpa

    def _set_gpa(self, gpa):
        if gpa <= 0:
            self._gpa = 0.0
        elif gpa >= 4:
            self._gpa = 4
        else:
            self._gpa = gpa
    gpa=property(_get_gpa, _set_gpa)
    
    @property
    def letter(self):
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

    @letter.setter
    def letter(self, grade):
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
    print("GPA: {:.2f}".format(student.gpa))
    print("Letter: {}".format(student.letter))

    value = float(input("Enter a new GPA: "))

    student.gpa = value

    print("After setting value:")
    print("GPA: {:.2f}".format(student.gpa))
    print("Letter: {}".format(student.letter))

    letter = input("Enter a new letter: ")

    student.letter = letter

    print("After setting letter:")
    print("GPA: {:.2f}".format(student.gpa))
    print("Letter: {}".format(student.letter))

if __name__ == "__main__":
    main()