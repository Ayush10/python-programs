# Program about cases
# Taking user input
text = input("Enter any string: ")


# Function to check the case of the given string
def case_checker(t):
    # Initializing an empty list to return multiple values
    values = []

    # Initializing two empty string to store second returnable value
    result = ''
    case = ''

    # Checking the specified condition
    if t == t.upper():
        t = t.lower()
        case = "uppercase"
        result = "converted to lowercase"
    elif t == t.lower():
        t = t.upper()
        case = "lowercase"
        result = "converted to uppercase"
    else:
        case = "not any case"
        result = "same"

    values.append(t)
    values.append(case)
    values.append(result)
        
    return values


# Checking condition for displaying result
if case_checker(text)[1] == "same":
    print("The given string {0} is now being printed as the same string {1}"
          "as it doesnt satisfy the given condition.".format(text, text))
else:
    print("The given string {0} which was {1} is now {2} as {3}.".format(text,
                            case_checker(text)[1], case_checker(text)[2],
                            case_checker(text)[0]))
