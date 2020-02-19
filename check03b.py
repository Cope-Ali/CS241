
class Complex():
    """Complex class for complex number made up of two variables "real" and "imaginary" """

    def __init__(self):
        self.real = 0
        self.imaginary = 0

    def setReal(self):
        """set the real number"""
        self.real = input("Please enter the real part: ")

    def setImaginary(self):
        """set the imaginary number"""
        self.imaginary = input("Please enter the imaginary part: ")

    def getReal(self):
        """return the real number"""
        return self.real

    def getImaginary(self):
        """return the imaginary number"""
        return self.imaginary

    def display(self):
        """display the Complex number in form real = imaginaryi"""
        print("{} + {}i" .format(self.getReal(), self.getImaginary()))   


def main():
    #create two complex numbers
    first = Complex()
    second = Complex()
    #display the two complex numbers
    print("The values are:")
    first.display()
    second.display()
    print('')
    #set the two numbers using user input
    first.setReal()
    first.setImaginary()
    print('')
    second.setReal()
    second.setImaginary()
    print("")
    #display the updated numbers
    print("The values are:")
    first.display()
    second.display()

#used to call the main function
if __name__ == "__main__":
    main()