class Rational():
    """Rational class holds rational numbers with a top number/ numerator 
    and a bottom number/ denominatior"""
    def __init__(self):
        self.top = 0
        self.bottom = 1

    def display(self):
        if(int(self.bottom) > int(self.top)):
            print("{}/{}".format(int(self.top), int(self.bottom)))
        else:
            whole = int(self.top)/int(self.bottom)
            remainder = int(self.top)%int(self.bottom)
            if (remainder > 0):
                print("{} {}/{}".format(int(whole), int(remainder), self.bottom))
            else:
                print(int(whole))
    
    def prompt(self):
        self.top = input("Enter the numerator: ")
        self.bottom = input("Enter the denominator: ")

    def decimal(self):
        print(int(self.top)/int(self.bottom))

    def reduceNum(self):
        #if(int(self.top) >= int(self.bottom)):
        i = 1
        divisable = 0
        while (i<=int(self.bottom)):
            redTop = int(self.top)%i
            redBot = int(self.bottom)%i
            if (int(redBot) == 0 and int(redTop) == 0):
                divisable = i
            i += 1
        if (int(divisable) > 1):
            self.top = int(self.top)/int(divisable)
            self.bottom = int(self.bottom)/int(divisable)

def multiply_by(firstNumber):
        secondNumber = Rational()
        secondNumber.prompt()
        newTop = int(firstNumber.top) * int(secondNumber.top)
        newBottom = int(firstNumber.bottom) * int(secondNumber.bottom)
        return newTop, newBottom


def main():
    number = Rational()
    number.display()
    number.prompt()
    number.display()
    number.decimal()
    number.reduceNum()
    number.display()
    multipled = Rational()
    mTop, mBottom = multiply_by(number)
    multipled.top = mTop
    multipled.bottom = mBottom
    multipled.display()


#used to call the main function
if __name__ == "__main__":
    main()