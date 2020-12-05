# Python program to find the sum of n natural numbers
# Taking user input
num = int(input("Enter any number: "))

# Checking condition if the number is less than 0
if num < 0:
    print("Enter a positive number.")
else:
    # Initializing the sum to 0
    total = 0

    # Using loop to iterate till num turns 0
    while num > 0:
        total += num
        num -= 1

    print("The sum is: {0}.".format(total))
