# Program to check whether the given number is odd or even
# Taking user input
number = int(input("Enter any number: "))

# Checking even condition
if number % 2 == 0:
    print("The given number %d is even." % number)
# If a given number is not even then it will always be odd.
# Law of Mathematics
else:
    print("The given number %d is odd." % number)