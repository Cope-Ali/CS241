"""
File: check06b.py
Author: Ali Cope
This program creates a Phone class that contains the following:
area_code : int
prefix : int
suffix : int
prompt_number() : void
display() : void
It also creates a SmartPhone class which extends the phone class and adds the following
email : string
prompt() : void
display() : void
"""

class Phone():
    """
    This class contains: 
    area_code : int
    prefix : int
    suffix : int
    prompt_number() : void
    display() : void
    """
    def __init__(self):
        self.area_code = 0
        self.prefix = 0
        self.suffix = 0

    def prompt_number(self):
        """
        Prompts user for the three parts of a phone and sets them
        """
        self.area_code = int(input("Area Code: "))
        self.prefix = int(input("Prefix: "))
        self.suffix = int(input("Suffix: "))

    def display(self):
        """
        Display the number in the format "(areaCode)prefix-suffix"
        """
        print("\nPhone info:")
        print("({}){}-{}".format(self.area_code, self.prefix, self.suffix))

class SmartPhone(Phone):
    """
    SmartPhone class extends the Phone class and adds the following:
    email : string
    prompt() : void
    display() : void
    """
    def __init__(self):
        #call the base class
        super().__init__()
        #add member variables
        self.email = ""

    def prompt(self):
        """
        Calls the prompt_number method from the Phone class and also prompts for email address
        """
        super().prompt_number()
        self.email = str(input("Email: "))

    def display(self):
        """
        Calls the display method from the Phone class and also displays the email address
        """
        super().display()
        print(self.email)

def main():
    """
    This is the main class. 
    We will create  a Phone object, call its prompt_number method, and then its display method.
    We will create a SmartPhone object, call its prompt method, and then its display method.
    """

    #create a phone object
    phone = Phone()
    # call its prompt_number method
    print("Phone:")
    phone.prompt_number()
    #display the phone info
    phone.display()

    #create a SmartPhone object
    print("")
    print("Smart phone:")
    smart = SmartPhone()
    #prompt user for info
    smart.prompt()
    #display smartphone info
    smart.display()

#used to call the main function
if __name__ == "__main__":
    main()

