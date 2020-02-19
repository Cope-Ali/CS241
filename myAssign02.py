#based on walkthrough from video "RecordingOfWorkingThroughAssignment2"
#function to get filename from user
def prompt_filename():
    filename = input("Please enter the data file: ")
    return filename

#open file, parse the file, and find the min, max and average rates
def get_file(filename):
    f = open(filename, "r")
    ratesSum = 0
    minRate = 5.0
    maxRate = 0.0
    lineTotal = 0
    minLine = ''
    maxLine = ''

    for line in f:
        if(lineTotal >0):
            p = float(line.split(",")[6])
            ratesSum += p
            if (maxRate < p):
                maxRate = p
                maxLine = line
            if (minRate > p):
                minRate = p
                minLine = line
        lineTotal += 1
    averageRate = ratesSum / float(lineTotal -1)
    f.close()
    return averageRate, maxRate, minRate, maxLine, minLine

#display the rate in the desired format
def display (line):
    lineArray = line.split(",")
    print("{} ({}, {}) - ${}" .format(lineArray[2],lineArray[0],lineArray[3],float(lineArray[6])))    
    #print (lineArray)

#main function
def main():
    fname = prompt_filename()
    print('')
    averageRate, maxRate, minRate, maxLine, minLine = get_file(fname)
    print("The average commercial rate is: {}" .format(averageRate))
    print('')
    print("The highest rate is:")
    display(maxLine)
    print('') 
    print("The lowest rate is:")
    display(minLine)



#used to call the main function (i think)
if __name__ == "__main__":
    main()