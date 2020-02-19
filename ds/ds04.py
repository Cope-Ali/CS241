from collections import deque

class Song():
    """Creates a song class with variables: title and artist and methods:prompt() and display()"""

    def __init__(self):
        self.title=""
        self.artist=""

    def prompt(self):
        self.title=input("\nEnter the title: ")
        self.artist=input("Enter the artist: ")
    
    def display(self):
        print("{} by {}".format(self.title, self.artist))

def getAction():
    choice = 0
    print("\nOptions: ")
    print("1. Add a new song to the end of the playlist")
    print("2. Insert a new song to the beginning of the playlist")
    print("3. Play the next song")
    print("4. Quit")
    choice = int(input("Enter selection: "))
    return choice

def main():
    playlist = deque()
    loop = "yes"
    while loop != "no":
        action = getAction()
        if action == 1:
            new = Song()
            new.prompt()
            playlist.append(new)
        elif action == 2:
            new = Song()
            new.prompt()
            playlist.appendleft(new)
        elif action == 3:
            if len(playlist)>0:
                next = Song()
                next = playlist.popleft()
                print("\nPlaying song: ")
                next.display()
            else:
                print("\nThe playlist is currently empty.")
        elif action == 4:
            print("Goodbye")
            loop = "no"
        else:
            print("\nInvalid selection")

if __name__ == "__main__":
    main()