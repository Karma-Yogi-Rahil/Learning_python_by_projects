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

def save_to_csv(num):
    attri , all_generated_data = gen_data(num)
    with open('Fake Information Generator/Names1.csv', 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames = attri)
        writer.writeheader()
        for k in all_generated_data: 
            writer.writerow(k)


