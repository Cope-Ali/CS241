#get a positive number from the user and make sure it is valid (positive)
def prompt_number():
    num = "invalid"
    while num != "valid":
        number = int(input("Enter a positive number: "))
        if number > 0 :
            num = "valid"
            return number
        else:
            print("Invalid entry. The number must be positive.")

#calculate the sum of three numbers that are passed into the function
def compute_sum(a, b, c):
    total = int(a) + int(b) + int(c)
    return total

#the main function use to collect three numbers by calling prompt_number and 
# calculate their sum by calling compute_sum then outputting the result
def main():
    a = prompt_number()
    print('')
    b = prompt_number()
    print('')
    c = prompt_number()
    print('')
    total = compute_sum(a, b, c)
    print("The sum is: " + str(total))

#used to call the main function (i think)
if __name__ == "__main__":
    main()