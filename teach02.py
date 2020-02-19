#function to get filename from user
def prompt_filename():
    filename = input("Please enter a filename: ")
    return filename

#prompt user for a search word
def get_search_word():
    sw = input("Please enter a word to search for: ")
    low_sw = sw.lower()
    return low_sw

#function parses the file and prints it to the screen
def parse_file(file, search_word):
    count = 0
    f = open(file, "r")
    for line in f:
        lower = line.lower()
        words = lower.split(" ")
        count += words.count(search_word)
        #for word in words:
        #   print(word)
    f.close()    
    return count

#main function
def main():
    fname = prompt_filename()
    print("Opening file " + fname)
    search_word = get_search_word()
    total = parse_file(fname, search_word)
    print("The word " + str(search_word) + " occurs " + str(total) + " times in this file.")

#used to call the main function (i think)
if __name__ == "__main__":
    main()
