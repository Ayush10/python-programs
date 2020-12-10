# Program to check whether the given number is palindrome or not
# Taking user input
low = int(input("Enter lower limit: "))
high = int(input("Enter upper limitr: "))


# Function for Palindrome numbers in range
def palindrome_numbers_in_range(l, h):
    # Creating an empty list to store palindrome numbers
    numbers = []

    for num in range(l, h):
        # Storing the value of num in a temporary container
        temp = num

        # Assigning the value to the reverse integer
        rev = 0

        # Palindrome Checker
        while num > 0:
            digit = num % 10
            rev = rev * 10 + digit
            num //= 10

        # Checking condition to see if the number is palindrome number or not
        if temp == rev:
            # Adding the value in the empty container if the number is palindrome
            numbers.append(rev)

        # Reassigning the value of num as the current value is 0
        num = temp + 1

    # print(numbers) # This was done to check if the resulting output satisfies or not

    return numbers


# Displaying the result
print("The palindrome numbers between the specified range of {0} and {1} are: {2}.".format(str(low), str(high),
                                            str(palindrome_numbers_in_range(low, high))[1:-1]))
