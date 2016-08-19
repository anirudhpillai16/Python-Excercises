# Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user.

# Extras:

# If the number is a multiple of 4, print out a different message.
# Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). 
# If check divides evenly into num, tell that to the user. If not, print a different appropriate message.

num = input("Enter any number:")
check = input("Enter check:")
if num%2 == 0:
    print "Number is even"
else:
    print "Number is odd"
if num %4 == 0:
    print "Number is divisible by 4"
if num%check == 0:
    print str(num) + "is divisible by" + str(check)
else:
    print str(num) + " is not divisible by " + str(check)