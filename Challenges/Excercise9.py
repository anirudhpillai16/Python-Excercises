# Ask the user for a number and determine whether the number is prime or not.
number = input("Enter any number other than Zero:")
count =0
for i in range(1,number+1):
    if number%i == 0:
        count= count +1
if count == 2:
    print "Number is prime"
else:
    print "Number is not prime"
        