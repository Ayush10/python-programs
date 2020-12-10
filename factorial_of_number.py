# Program to find the factorial of a given number
# Taking user input
number = int(input("Enter any number: "))


# Factorial Function
def factorial(n):
    # Initializing the value of fact for later use
    fact = 1

    # Factorial Algorithm
    while n >= 1:
        fact = fact * n
        n -= 1

    return fact


# Displaying the result
print("The factorial of the given number %d is %d." % (number, factorial(number)))
