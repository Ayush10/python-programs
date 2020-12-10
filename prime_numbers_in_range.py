# Program to find prime numbers in a given range
# Taking range as per the choice of the user
low = int(input("Enter lower limit: "))
high = int(input("Enter upper limit: "))


# Function for finding prime numbers in given range
def prime_numbers(l, h):
    # Creating an empty list to store prime numbers
    numbers = []

    # Specifying range
    for num in range(l, h):
        # Starting from 2 as 0 and 1 can never be considered as prime
        if num > 1:
            for i in range(2, num):
                # Because 2 will always be a prime number and not including it
                # can often hamper the logic of the code
                if num == 2:
                    numbers.append(num)
                elif num % i == 0:
                    break
            else:
                numbers.append(num)

    return numbers


# Displaying the result
print("The prime numbers between the specified range of {0} and {1} are: {2}.".format(str(low), str(high),
                                                                                     str(prime_numbers(low, high))[
                                                                                     1:-1]))
