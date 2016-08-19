# Ask the user for a string and print out whether this string is a palindrome or not.
# (A palindrome is a string that reads the same forwards and backwards.)

var = raw_input("Enter any string: ")
var = var.upper()
if var == var[::-1]:
    print var + " is Palindrome"
else:
    print var + " is not Palindrome"
    