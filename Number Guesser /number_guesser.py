import random


upper_limit = int(input("Enter the upper limit of the number: "))

random_number = random.randint(0,upper_limit)

print(random_number) 

total_guess = 0

while True:
    total_guess +=1
    user_guess = int(input("Make your Guess: "))

    if user_guess == random_number:
        print("Vola it's the correct guess !! ")
        break
    elif user_guess > random_number:
        print("your guess is greater than the number ")

    else:
        print("your guess is less then the number")
    
    
print("you took total", total_guess,"to get the correct number")