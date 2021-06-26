print("----Welcome to the Quiz game----")
print("--------------------------------")


want_to_play = input("Do you want to play the game? (yes/no) ").lower()

if want_to_play != "yes": 
    quit()


print("------okay lets play------ ")
score = 0 

# Question 1 
print("Question 1")
question = input("What is the answer to this expression, 22 % 3 is?\n ")
if question == "1":
    print("Your answer is correct")
    score +=1
else:
    print("incorrect")


# Question 2 
print("\nQuestion 2")
question = input("What is the output of this expression, 3*1**3?\n ")
if question == "1":
    print("Your answer is correct")
    score +=1
else:
    print("incorrect")


# Question 3
print("\nQuestion 3")
question = input("In order to store values in terms of key and value we use what core data type \n").lower()
if question == "dictionary":
    print("Your answer is correct")
    score +=1
else:
    print("incorrect")



# Question 4 
print("\nQuestion 4")
question = input("Q What data type is the object below? \n L = [1, 23, 'hello', 1]\n ").lower()
if question == "list":
    print("Your answer is correct")
    score +=1
else:
    print("incorrect")


# Question 5 
print("\nQuestion 5")
question = input("In which language is Python written?\n ").lower()
if question == "c":
    print("Your answer is correct")
    score +=1
else:
    print("incorrect")



# Question 6
print("\nQuestion 6")
question = input("Which character is used in Python to make a single line comment?\n ")
if question == "#":
    print("your answer is correct")
    score +=1
else:
    print("incorrect")




# Question 7
print("\nQuestion 7")
question = input("What is the method inside the class in python language?\n ").lower()
if question == "function":
    print("Your answer is correct")
    score +=1
else:
    print("incorrect")



# Question 8
print("\nQuestion 8")
question = input("Suppose listExample is [‘h’,’e’,’l’,’l’,’o’], what is len(listExample)?\n ")
if question == "5":
    print("Your answer is correct")
    score +=1
else:
    print("incorrect")




# Question 9
print("\nQuestion 9")
question = input("Suppose list1 is [2445,133,12454,123], what is max(list1)?\n ")
if question == "12454":
    print("Your answer is correct")
    score +=1
else:
    print("incorrect")



# Question 10
print("\nQuestion 10")
question = input("Which module in Python supports regular expressions?\n ").lower()
if question == "re":
    print("your answer is correct")
    score +=1
else:
    print("incorrect")



print(f"Your score is {(score/10)*100}")

answer = input("Would like to see all the answer (yes/no) ").lower()
if answer != "no":
    print("\nQ1) What is the answer to this expression, 22 % 3 is?\nAnswer : 1\n")
    print("Q2) What is the output of this expression, 3*1**3?\nAnswer : 1\n")
    print("Q3) What data type is the object below?\nL = [1, 23, 'hello', 1]\nAnswer : list\n")
    print("Q4) In order to store values in terms of key and value we use what core data type\nAnswer : Dictionary\n")
    print("Q5) In which language is Python written?\nAnswer : c\n")
    print("Q6) Which character is used in Python to make a single line comment?\nAnswer : #\n")
    print("Q7) What is the method inside the class in python language?\nAnswer : Function\n")
    print("Q8) Suppose listExample is [‘h’,’e’,’l’,’l’,’o’], what is len(listExample)?\nAnswer : 5 \n")
    print("Q9) Suppose list1 is [2445,133,12454,123], what is max(list1)?\nAnswer : 12454\n")
    print("Q10) Which module in Python supports regular expressions?\nAnswer : re \n")

else :
    print("Thank You for taking Quiz ")












