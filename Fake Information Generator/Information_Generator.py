from io import BufferedIOBase
from os import name, writev
from faker import Faker 
import pandas as pd 
import csv

fk = Faker()

def gen_data(max_data_no):
    attri =['username' , 'name', 'sex', 'address', 'mail', 'birthdate']
    all_generated_data = []
    for i in range(max_data_no):
        data = fk.simple_profile()
        all_generated_data.append(data)
    
    return attri , all_generated_data

def save_user_data_to_csv(num,file_name):
    attri , all_generated_data = gen_data(num)
    adress = f'Fake Information Generator/{filename}.csv'
    with open(adress, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames = attri)
        writer.writeheader()
        for k in all_generated_data: 
            writer.writerow(k)
        



def generate_credit_card(n):
    fk = Faker()
    for i in range(n):
        print("\n",fk.credit_card_full())


print("----Welcome----")
while True:
    option = input("would you like to generate fake user data('user') or fake credit card('credit'). [q to Quit]: ").lower()

    if option == 'q':
        print("Thank you using this")
        break

    elif option == 'user':
        print("Generating the data ----> ")
        save_data = input("would you like to save the data(yes/no) : ").lower()
        if save_data =='yes':
            num = int(input("Enter the total no of fake user data you want: "))
            filename = input("Enter the finle name: ")
            save_user_data_to_csv(num,filename)
        elif save_data == "no":
            num = int(input("Enter the total no of fake user data you want: "))
            attri , all_generated_data = gen_data(num)
            for i in all_generated_data:
                print('\n',i)

    elif option == 'credit':
        num_credit = int(input("Enter the total no of fake credit card you want to Generate: "))
        generate_credit_card(num_credit)

    else:
        continue

        
    