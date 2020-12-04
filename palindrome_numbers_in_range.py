# Program to check whether the given number is palindrome or not
# Taking user input
low = int(input("Enter lower limit: "))
high = int(input("Enter upper limitr: "))


def palindrome_numbers_in_range(l, h):
    # Creating an empty list to store palindrome numbers
    numbers = []

    while l <= h:
        # Storing the value of num in a temporary container
        temp = l

        # Assigning the value to the reverse integer
        rev = 0

        while l > 0:
            digit = l % 10
            rev = rev * 10 + digit
            l //= 10

        if temp == rev:
            numbers.append(l)
            
        l += l

    return numbers


# Displaying the result
print("The palindrome numbers between the specified range of {0} and {1} are: {2}.".format(str(low), str(high),
                                                                                           str(
                                                                                               palindrome_numbers_in_range(
                                                                                                   low, high))[1:-1]))
