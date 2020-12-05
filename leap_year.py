# Python program to check leap year
# Taking user input
year = int(input("Enter the year you want to check: "))

# Checking mechanism
if (year % 4) == 0:
    if (year % 100) == 0:
        if (year % 400) == 0:
            print("{0} is a leap year".format(year))
        else:
            print("{0} is not a leap year".format(year))
    else:
        print("{0} is a leap year".format(year))
else:
    print(f"{year} is not a leap year")
