from point import Point

class Circle(Point):
    def __init__ (self):
        super().__init__()
        self.radius = 0.0
    
    def prompt_for_circle(self):
        """
        """
        super().prompt_for_point()
        self.radius = float(input("Enter radius: "))

    def display_circle(self):
        print("Center:")
        super().display()
        print("Radius: {}".format(self.radius))
    
    
def main():
    circle = Circle()
    circle.prompt_for_circle()
    circle.display_circle()



#used to call the main function
if __name__ == "__main__":
    main()
