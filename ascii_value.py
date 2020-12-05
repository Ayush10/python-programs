# Program to find the ASCII value of a given character
# Taking user input
character = input("Enter any character: ")

# Checking if there are more than 1 characters in the given string.
if len(character) > 1:
    print("Please enter only one character!")
    print("The ASCII value of the first character {0} of the given string {1} is {2}.".format(character[0], character,
                                                                                              ord(character[0])))
# If only one character in the given string.
else:
    print("The ASCII value of the given character {0} is {1}.".format(character, ord(character)))
