import pandas as pd 
import numpy as np 
import csv 
from faker import Faker
import random

fake = Faker()


with open('recources2.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Attack", "Defence", "Consumption"])
        writer.writerow([fake.name(), 20, 12, 3])
        file.close()



def soldierGeneration(x):

    for i in range (0,x):
        attackValue = random.randint(0,21)
        defenceValue = random.randint(0,21)
        consumptionValue = random.randint(0,11)
        df = pd.read_csv('recources2.csv')
        Soldier = pd.DataFrame({"Name":[fake.name()],"Attack": [attackValue],"Defence": [defenceValue],"Consumption": [consumptionValue]})
        hf = pd.concat([df, Soldier], ignore_index=True)
        hf.to_csv('recources2.csv', index= False, encoding='utf-8')
        
soldierGeneration(4)
with open('recources2.csv', 'r') as file:
  dataset = pd.read_csv('recources2.csv')
  print(dataset)

soldierGeneration(3)


""" with open('recources1.csv', 'w', newline= '') as file:
        writer = csv.writer(file)
        writer.writerow(["Number", "Bread", "Wheat", "Meat", "Water", "Ale"])
        writer.writerow([1, 6, 19, 5, 20, 1])
        writer.writerow([2,'3months', '2,5months', '1,5months', '4months', '3weeks'])
        file.close() """

pf = pd.DataFrame({
        'foodType' : ["Bread", "Wheat", "Meat", "Water", "Ale"],
        'foodAmount' : [6, 19, 5, 20, 1],
        'Duration' : [3,2 , 1.5, 4, 3]
    })
pf.to_csv('recources1.csv', index= False, encoding='utf-8')

def foodgeneration(x):   

    for i in range (0,x):
        breadAmount = random.randint(0,21)
        wheatAmount = random.randint(0,21)
        meatAmount = random.randint(0,21)
        waterAmount = random.randint(0,21)
        aleAmount = random.randint(0,21)
        foodDuration1 = random.randint(0,11)
        foodDuration2 = random.randint(0,11)
        foodDuration3 = random.randint(0,11)
        foodDuration4 = random.randint(0,11)
        foodDuration5 = random.randint(0,11)

        lf = pd.read_csv('recources1.csv')
        food = pd.DataFrame({"foodType":['Bread','Wheat','Meat','Water','Ale'],"foodAmount": [breadAmount,wheatAmount,meatAmount,waterAmount,aleAmount],"Duration": [foodDuration1,foodDuration2,foodDuration3,foodDuration4,foodDuration5]})
        kf = pd.concat([lf, food], ignore_index=True)
        kf.to_csv('recources1.csv', index= False, encoding='utf-8')


foodgeneration(3)
"""  df = pd.DataFrame(foodstats)
    
    df.to_csv("c:/Users/tim.clement/Desktop/TimClement4/recources1.csv", index=False)
 """
""" foodgeneration() """


soldierGeneration(4)



