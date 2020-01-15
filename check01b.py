# write a program that asks the user how old they are, displays that information back 
# and then informs them how old they will be on their next birthday

#get user input
print ("Please enter your name: ")
name = input()
print ("Please enter your age: ")
age = input()

#calculate age on next birthday
birthday = int(age)+1

#output back to user
print ("Hello " + name + ", you are " + age + " years old.")
print ("On your next birthday, you will be " + str(birthday) + ".")