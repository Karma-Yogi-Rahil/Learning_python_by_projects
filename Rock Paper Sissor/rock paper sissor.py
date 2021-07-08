import random

user_score = 0
computer_score = 0
tie_score = 0
option = ['rock','paper','sissor']
print("\n--------------------------Let's Start-----------------------------")
while True:
    
    user_input = input("Type Rock/Paper/Sissors or 'q' to quit the Game: ").lower()

    if user_input == 'q':
        print("----------- Pls wait Quitting -----------")
        break
    
    if user_input not in option:
        print(" pls enter eithier rock/paper/sissor")
        continue


    random_number = random.randint(0,2)
    #rock : 0 , paper : 1, sissor : 2
    computer_picked = option[random_number]

    if user_input == 'sissor' and computer_picked == 'paper':
        user_score += 1
        print("-> Sissor cuts Paper ")
        print("---You Won!!--- \n")

    elif user_input == 'paper' and computer_picked == 'rock':
        user_score += 1
        print("-> Paper covered the Rock ")
        print("---You Won!!--- \n")
    
    elif user_input == 'rock' and computer_picked == 'sissor':
        user_score += 1
        print("-> Rock destoryed the Sissor")
        print("---You Won!!--- \n")

    elif user_input == computer_picked:
        print(f"You and Computer both showed {user_input}\n")
        tie_score += 1


    
    else:
        computer_score += 1
        print("You Lost \n")





print("\n---------------------SCORE---------------------------")
print(f"Your score is:{user_score}")
print(f"The computer score is:{computer_score}" )
print(f"You tied with computer {tie_score} times")
print("\nThanks for playing the game , Untill we meet again \n")
