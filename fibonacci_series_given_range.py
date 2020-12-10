# Program to print Fibonacci series in the given range
# Taking range as per the choice of the user
low = int(input("Enter lower limit: "))
high = int(input("Enter upper limit: "))


# Fibonacci Function
def fibonacci_numbers(low, high):
    a = 0
    b = 1
    c = 1

    # Empty list to store the fibonacci numbers between the specified range
    numbers = []

    # Specifying range
    while a <= high:
        # If the number falls between the range then inserting it into the list
        if a >= low:
            numbers.append(a)

        # Fibonacci Algorithm
        a = b
        b = c
        c = a + b

    return numbers


# Displaying the result
print("The fibonacci numbers between the specified range of " + str(low) + " and " + str(high) +
      " are: " + str(fibonacci_numbers(low, high))[1:-1] + ".")
