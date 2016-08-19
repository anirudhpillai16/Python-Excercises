# Write a program that asks the user how many Fibonacci numbers to generate and then generates them
number = input("How many numbers do you want in Fibonacci series:")
fibonacci = [1,1]
if number == 0:
    fibonacci=[]
elif number == 1:
    fibonacci = [1]
elif number == 2:
    fibonacci = [1,1]
else:
    for i in range(1,number-1):
        fibonacci.append(fibonacci[i-1] + fibonacci[i])
print "\nHere is your fibonacci series -->" + str(fibonacci)
        
    