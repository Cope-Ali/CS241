""" 
File: check06a.py
Author: Ali Cope
This checkpoint is intended to help you practice the syntax of basic inheritance.
Create a (parent) Book class and two (child) classes that inherite from it, a TextBook class
and a PictureBook class.
"""

class Book():
    """
    This class contains three member variables
    title : string
    author : string
    publication_year : int

    This class contains two methods
    prompt_book_info()
    display_book_info()
    """
    def __init__(self):
        self.title = ""
        self.author = ""
        self.publication_year = 0

    def prompt_book_info(self):
        """
        Prompts the user for the title, author and publication year
        and assigns them to the book
        """
        self.title = str(input("Title: "))
        self.author = str(input("Author: "))
        self.publication_year = int(input("Publication Year: "))

    def display_book_info(self):
        """
        Displays the title, author, and publication year in the format: "Title (publication_year) by Author"
        """
        print("{} ({}) by {}".format(self.title, self.publication_year, self.author))

class TextBook(Book):
    """ 
    Textbook class extends Book class and adds one memeber variable
    subject : string

    TextBook class contains two methods
    prompt_subject()
    display_subject()
    """
    def __init__(self):
        # call the base class 
        super().__init__()
        # add member variable
        self.subject = ""

    def prompt_subject(self):
        """
        This method prompts the user for the subject and saves it to textbook
        """
        self.subject = str(input("Subject: "))

    def display_subject(self):
        """
        This method displays the TextBook subject
        """
        print("Subject: {}".format(self.subject))

class PictureBook(Book):
    """
    PictureBook class extends a Book and adds the following member variable:
    illustrator : string

    PictureBook adds two methods
    prompt_illustrator()
    display_illustrator()
    """
    def __init__(self):
        #call the base class
        super().__init__()
        #add member variable
        self.illustrator = ""

    def prompt_illustrator(self):
        """
        This method prompts the user for the illustrator and saves it to PictureBook
        """
        self.illustrator = str(input("Illustrator: "))

    def display_illustrator(self):
        """
        This method displays the PictureBook Illustrator
        """
        print("Illustrated by {}".format(self.illustrator))


def main():
    """
    Main function will create a Book object, prompt the user for info and display the book info.
    It will create a TextBook object, prompt the user and display info
    It will create a PictureBook object, prompt the user and display the info
    """
    #Create a Book object
    book = Book()
    #prompt the user for the book's information
    book.prompt_book_info()
    #display the book's information back to the user
    print("")
    book.display_book_info()
    print("")
    
    #create a TextBook object
    text = TextBook()
    #Prompt the user for the book information
    text.prompt_book_info()
    #prompt the user for the textbook subject
    text.prompt_subject()
    #display the book info
    print("")
    text.display_book_info()
    #display the textbook subject
    text.display_subject()
    print("")

    #Create a PictureBook object
    picture = PictureBook()
    #Prompt the user for the book information
    picture.prompt_book_info()
    #prompt the user for the picturebook illustrator
    picture.prompt_illustrator()
    #display the book information
    print("")
    picture.display_book_info()
    #display the picturebook illustrator
    picture.display_illustrator()
    

#used to call the main function
if __name__ == "__main__":
    main()
