#importing the random library
import random

print("-----Let's play the Number Guessing game -----")

#asking user the max number we wants to guess
upper_limit = int(input("Enter the upper limit of the number: "))

#creating the random number 
random_number = random.randint(0,upper_limit)

#keeping th count the number of guess 
total_guess = 0

while True:
    #adding 1 to total_guess everytime the loop runs
    total_guess +=1
    #asking user to make a guess 
    user_guess = int(input("Make your Guess: "))

    if user_guess == random_number:
        print("Vola it's the correct guess !! ")
        break

    elif user_guess > random_number:
        print("your guess is greater than the number ")

    else:
        print("your guess is less then the number")
    
    
print("you took total", total_guess," guess to get the correct number")