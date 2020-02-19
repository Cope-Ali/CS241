filename = input("Enter file: ")
fileref = open(filename, "r")
lineCount = 0
wordCount = 0
for line in fileref:
    lineCount += 1
    words = line.split(" ")
    for word in words:
        wordCount += 1
print("The file contains " + str(lineCount) + " lines and " + str(wordCount) + " words.")

fileref.close()