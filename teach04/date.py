class Date():
    
    def __init__(self):
        self.day = 1
        self.month = 1
        self.year = 2000
        
    def prompt(self):
        self.day = input("Day: ")
        self.month = int(input("Month: "))
        if self.month > 12 or self.month <0:
            print("Invalid month. Please enter a month number between 1 and 12")
            self.month = input("Month: ")
        self.year = int(input("Year: "))
        if self.year < 2000:
            print("Invalid year. Please enter a year after 2000")
            self.year = input("Year: ")

        
    def display(self):
        if int(self.month) < 10:
            self.month = str("0" + str(self.month))
        if int(self.day) < 10:
            self.day = str("0" + str(self.day))
        print("{}/{}/{}".format(self.month, self.day, self.year))