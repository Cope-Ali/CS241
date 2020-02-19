class Person():
    """Person class contains a name and birth year"""
    def __init__(self):
        self.name = "anonymous"
        self.birthyear = "unknown"

    def __str__(self):
        return self.name + " (b. " + self.birthyear + ")"

class Book():
    """Book class contains a title and an author (Person class), and a publisher"""
    def __init__(self):
        self.title = "untitled"
        self.author = Person()
        self.publisher = "unpublished"

    def __str__(self):
        authStr = str(self.author)
        return self.title + "\nPublisher:\n" + self.publisher + "\nAuthor:\n" + authStr

    def setBook(self):
        print("")
        print("Please enter the following:")
        self.author.name = input("Name: ")
        self.author.birthyear = input("Year: ")
        self.title = input("Title: ")
        self.publisher = input("Publisher: ")
        print("")


def main():
    book = Book()
    print(book)
    book.setBook()
    print(book)


#used to call the main function
if __name__ == "__main__":
    main()