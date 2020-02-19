
class Robot():
    """Robot class to create and move robot around"""

    def __init__(self):
        self.x = 10
        self.y = 10
        self.fuel = 100
    
    def moveLeft(self):
        if self.fuel >= 5:
            self.x -= 1
            self.fuel -= 5
        else:
            print("Insufficient fuel to perform action")

    def moveRight(self):
        if self.fuel >= 5:
            self.x += 1
            self.fuel -= 5
        else:
            print("Insufficient fuel to perform action")

    def moveUp(self):
        if self.fuel >= 5:
            self.y -= 1
            self.fuel -= 5
        else:
            print("Insufficient fuel to perform action")

    def moveDown(self):
        if self.fuel >= 5:
            self.y += 1
            self.fuel -= 5
        else:
            print("Insufficient fuel to perform action")

    def display(self):
        print("({}, {}) - Fuel: {}" .format(self.x, self.y, self.fuel))

    def fire(self):
        if self.fuel >= 15:
            print("Pew! Pew!")
            self.fuel -= 15
        else:
            print("Insufficient fuel to perform action")

def interact(robot):
    play = "yes"
    while play == "yes":
        action = input("Enter command: ")
        if action == "status":
            robot.display()
        elif action == "fire":
            robot.fire()
        elif action == "left":
            robot.moveLeft()
        elif action == "right":
            robot.moveRight()
        elif action == "up":
            robot.moveUp()
        elif action == "down":
            robot.moveDown()
        elif action == "quit":
            print("Goodbye.")
            play = "no"
            break
        else:
            #if invalid command is entered, restart loop to prompt again
            play = "yes"
            #print("Invalid Command")

def main():
    robot = Robot()
    interact(robot)




#used to call the main function
if __name__ == "__main__":
    main()