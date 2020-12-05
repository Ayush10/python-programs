# Program to check whether a number is armstrong or not
# Taking user input
number = input("Enter any number: ")

# Strong the length of the string for later use
length = len(number)

# Instantiating the sum as 0
total = 0

# Converting the string input into integer
number = int(number)

# Assigning the value of input to temp for calculation
temp = number
# Finding the sum of the nth power of each digit
while temp > 0:
    digit = temp % 10
    total += digit ** length
    temp //= 10

# Displaying the result
if number == total:
    print("The given number {0} is armstrong.".format(str(number)))
else:
    print("The given number {0} is not armstrong.".format(str(number)))
