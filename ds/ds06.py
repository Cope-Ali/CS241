"""
File: ds06.py
Author: Ali Cope
This program creates a system to track students who need help with their coursework.
This program created two classes; a Student Class and a HelpSystem Class.
The HelpSystem class is designed to use the queue data structure by utilizing the Deque object with its .append() and .popleft() methods.
"""
from collections import deque

class Student():
    """
    Student class creates a Student which contains
    name : string
    course : string
    __init__()
    prompt()
    display()
    """
    def __init__(self):
        """
        initilize the object
        """
        self.name = ""
        self.course = ""

    def prompt(self):
        """
        prompt() method gets student information from the user and saves it to student object
        """
        self.name = str(input("Enter name: "))
        self.course = str(input("Enter course: "))

    def display(self):
        """
        display() method displays the student name and course information
        """
        print("")
        print("Now helping {} with {}".format(self.name, self.course))
        

class HelpSystem():
    """
    HelpSystem creates a queue of students needing help by using a deque. It has the following properties:
    waiting_list : deque
    __init__()
    is_student_waiting() : boolean
    add_to_waiting_list(Student)
    help_next_student()
    """
    def __init__(self):
        """
        initilize the object by creating a deque for our waiting list
        """
        self.waiting_list = deque()

    def is_student_waiting(self):
        """
        Checks to see if there are any students in queue, if there are returns true, if not returns false
        """
        if len(self.waiting_list):
            return True
        else:
            return False

    def add_to_waiting_list(self, Student):
        """
        Receives a student as a parameter and adds it to the queue
        """
        self.waiting_list.append(Student)

    def help_next_student(self):
        """
        checks if there is a student in queue
        if there is a student, the student is removed from queue and their information is displayed
        if there is not a student in queue "No one to help" is displayed
        """
        #check to see if there is anyone in queue
        if len(self.waiting_list):
            #remove the first student from the queue
            next = self.waiting_list.popleft()
            #display their information
            next.display()
        #if there is no student, display "no one to help"
        else:
            print("")
            print("No one to help")

def options():
    """
    options function presents the user with three options and passes back their selection
    """
    #present user with options
    print("")
    print("Options:")
    print("1. Add a new student")
    print("2. Help next student")
    print ("3. Quit")
    #get user's choice
    choice = int(input("Enter selection: "))
    #return choice as int
    return choice

def main():
    """
    main function. Create a helpSystem. Call options function and call the appropriate helpSystem method for the user's choice. 
    """
    system = HelpSystem()
    choice = 0
    #until the user chooses to quit loop through
    while choice != 3:
        choice = options()
        #check if user chose to add a new student
        if choice == 1:
            #create new student
            student = Student()
            #get student information from user
            student.prompt()
            #add student to the queue
            system.add_to_waiting_list(student)
        #check if user chose to help next student
        elif choice == 2:
            system.help_next_student()
    print("")
    print("Goodbye")

#used to call the main function
if __name__ == "__main__":
    main()