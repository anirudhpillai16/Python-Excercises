# -*- coding: utf-8 -*-
# Generate a random number between 1 and 9 (including 1 and 9). 
# Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right.

# Keep the game going until the user types “exit”
# Keep track of how many guesses the user has taken, and when the game ends, print this out.
import random

number = random.randint(1,9)
guess = 0
count = 0

while guess != "exit" or guess != number:
    guess = input("Enter any number:")
    
    if guess == "exit":
        break
    guess = int(guess)
    count+=1
    
    if guess < number:
        print "Too Low"
    elif guess > number:
        print "Too High"
    else:
        print "You got it right! and it took you " + str(count) + " tries"
input()

