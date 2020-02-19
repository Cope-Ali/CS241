
class Student:
    """ Student class contains student id, first name and last name"""

    def __init__(self, f_name, l_name, id_num):
        """Create a new Student """
        self.firstName = f_name
        self.lastName = l_name
        self.idNum = id_num

    def getFirst(self):
        """get the first name of the Student"""
        return self.firstName

    def getLast(self):
        """get the last name of the Student"""
        return self.lastName

    def getIdNum(self):
        """get the ID number of the Student"""
        return self.idNum    

def prompt_student():
    """Prompts user for info and saves it as a student object"""
    first = input("Please enter your first name: ")
    last = input("Please enter your last name: ")
    num = int(input("Please enter your id number: "))
    
    studentInfo = Student(first, last, num)
    return studentInfo


def display_student(student):
    """ function displays student info from Student object"""
    print("")
    print("Your information:")
    print("{} - {} {}" .format(student.getIdNum(), student.getFirst(), student.getLast()))



def main():
    user = prompt_student()
    display_student(user)




#used to call the main function
if __name__ == "__main__":
    main()