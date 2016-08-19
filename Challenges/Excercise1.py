#Create a program that asks the user to enter their name and their age. 
#Print out a message addressed to them that tells them the year that they will turn 100 years old.

name = raw_input("Enter your name :")
age = input("Enter your age :")
year = str((2016 - age) + 100)
print name + " will be 100 years in the year " + year