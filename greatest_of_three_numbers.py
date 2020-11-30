# Program to find greatest among three numbers
# Taking user input
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

# Comparison Algorithm and displaying result
if a > b > c:
    print("%d is the greatest number among %d, %d and %d." % (a, a, b, c))
elif b > a > c:
    print("%d is the greatest number among %d, %d and %d." % (b, a, b, c))
else:
    print("%d is the greatest number among %d, %d and %d." % (c, a, b, c))
