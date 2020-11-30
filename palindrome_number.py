# Program to check whether the given number is palindrome or not
# Taking user input
number = int(input("Enter any number: "))

# Assigning the value of input to temp for calculation
temp = number

# Assigning the value to the reverse integer
rev = 0
# Finding the sum of the nth power of each digit
while number > 0:
    digit = number % 10
    rev = rev * 10 + digit
    number //= 10

# Displaying the result
if temp == rev:
    print("The number {0} is palindrome.".format(temp))
else:
    print("The number {0} is not palindrome.".format(number))

