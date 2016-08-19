# Create a program that asks the user for a number and then prints out a list of all the divisors of that number. 
num = input("Enter any number :")
div = list(range(1,num+1))
divisor_list = []
for number in div:
    if num%number ==0:
        divisor_list.append(number)
print str(num) + " is divisible by " + str(divisor_list)