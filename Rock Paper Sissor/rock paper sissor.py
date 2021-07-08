import random

user_score = 0
computer_score = 0
option = ['rock','paper','sissor']
print("\n-------------------------------------------------------")
while True:
    
    user_input = input("Type Rock/Paper/Sissors or 'q' to quit the Game: ").lower()

    if user_input == 'q':
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
    
    else:
        computer_score += 1
        print("You Lost \n")




print("\nThnaks for playing the game , Untill we meet again \n")
print("---------------------SCORE---------------------------")
print(f"Your score is {user_score}")
print(f"The computer score is {computer_score}\n" )
