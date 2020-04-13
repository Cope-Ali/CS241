
    
odd = []
even = []
num = 1

while num != 0:
    num = int(input ("Enter a number (0 to quit): "))
    if num != 0:
        if num % 2 == 0:
            even.append(num)
        else:
            odd.append(num)

print("Even numbers:")
for number in even:
    print(number)

print("Odd numbers:")
for number in odd:
    print(number)