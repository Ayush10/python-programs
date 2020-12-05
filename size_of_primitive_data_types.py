# Program to find the size of Primitive Numeric Data Types
# Importing System-Specific Parameter and Functions module
import sys

# Taking user input
choice = int(input("""Choose the data type that you want to find the size of: 
according to the numeric value given at its beginning below:
1. int
2. float
3. double
4. char
Example: 
Choose 1 if you want to find the size of int
Choose 2 if you want to find the size of float
Choose 3 if you want to find the size of double
Choose 4 if you want to find the size of char
Your Answer: 
"""))

# Checking the specified condition
if choice == 1:
    print("The size of the integer data type is: {0}.".format(sys.getsizeof(int())))
elif choice == 2:
    print("The size of the float data type is: {0}.".format(sys.getsizeof(float())))
elif choice == 3 or choice == 4:
    print("Double and Char are not Python data types so there is no size of these data types.")
else:
    print("Please enter a valid choice.")
