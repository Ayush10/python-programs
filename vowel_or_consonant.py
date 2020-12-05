# Program to check if the given alphabet is vowel or consonant
# Taking user input
alphabet = input("Enter any alphabet: ")


# Function to check if the given alphabet is vowel or consonant
def check_alphabets(letter):
    lower_case_letter = letter.lower()
    if lower_case_letter == 'a' or lower_case_letter == 'e' or lower_case_letter == 'i' or lower_case_letter == 'o' \
            or lower_case_letter == 'u':
        # or lower_case_letter == 'A' or lower_case_letter == 'E' or lower_case_letter == \
        # 'I' or lower_case_letter == 'U':
        return "vowel"
    else:
        return "consonant"


# Checking if the first character is an alphabet or not:
if 65 <= ord(alphabet[0]) <= 90 or 97 <= ord(alphabet[0]) <= 122:
    # Checking if there are more than 1 characters in the given string.
    if len(alphabet) > 1:
        print("Please enter only one character!")
        print("The first character {0} of the given string {1} is {2}.".format(alphabet[0], alphabet,
                                                                               check_alphabets(alphabet[0])))
    # If only one character in the given string.
    else:
        print("The given character {0} is {1}.".format(alphabet, check_alphabets(alphabet)))
# If the condition is not satisfied then returning the error to the user without calculation.
else:
    print("Please enter a valid alphabet. The character {0} is not an alphabet.".format(alphabet[0]))
