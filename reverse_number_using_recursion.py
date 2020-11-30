# Program to reverse input number using recursion
# Importing the regular expression library
# import re
# Taking user input
number = int(input("Enter any number with more than two digits: "))

# negative_number = re.findall(r"[+\-*/]", str(number))
# Checking if the number is more than 2 digits or not
if 9 > number > -9:
    print("The input number is %d, which is one digit number." % number)
    print("Please input at least 2 digits.")
else:
    # Carrying out the intended operation using recursion
    def reverse(n, r):
        if n == 0:
            return r
        else:
            return reverse(n // 10, r * 10 + n % 10)


    # Function Call
    reverse_number = reverse(abs(number), 0)

    # Displaying the result according to the type of it
    if number > 9:
        print("The reverse number of %d is %d" % (number, reverse_number))
    elif number < -9:
        print("The reverse number of %d is -%d" % (number, reverse_number))
