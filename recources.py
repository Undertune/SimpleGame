#Import av funktioner och bibliotek
import pandas as pd 
import csv 
from faker import Faker
import random
fake = Faker()


#Skapar preliminär för soldater data så programet alltid har en bas av data att hantera
with open('recources2.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Attack", "Defence", "Consumption"])
        writer.writerow([fake.name(), 20, 12, 3])
        file.close()


#Funktion för generation av soldat data
def soldierGeneration(x):


    #Här skapas dataframen för pandas från csv filen,
    #sedan läggs den ny skapade datan av Soldier dataframen tillsammans med dataframen df från csv filen.
    #Dessa två dataframes läggs in i en ny dataframe med hjälp av concat i dataframen hf som sedan läggs in i csv filen
    for i in range (0,x):
        attackValue = random.randint(0,21)
        defenceValue = random.randint(0,21)
        consumptionValue = random.randint(0,11)
        df = pd.read_csv('recources2.csv')
        Soldier = pd.DataFrame({"Name":[fake.name()],"Attack": [attackValue],"Defence": [defenceValue],"Consumption": [consumptionValue]})
        hf = pd.concat([df, Soldier], ignore_index=True)
        hf.to_csv('recources2.csv', index= False, encoding='utf-8')



#Skapar preliminär för mat data så programet alltid har en bas av data att hantera
pf = pd.DataFrame({
        'foodType' : ["Bread", "Wheat", "Meat", "Water", "Ale"],
        'foodAmount' : [6, 19, 5, 20, 1],
        'Duration' : [3,2 , 1.5, 4, 3]
    })
pf.to_csv('recources1.csv', index= False, encoding='utf-8')




#En funktion för generationen av mat data
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


        #Här skapas dataframen df för pandas från csv filen,
        #sedan läggs den ny skapade datan av food dataframen tillsammans med dataframen lf från csv filen.
        #Dessa två dataframes läggs in i en ny dataframe med hjälp av concat i dataframe kf som sedan läggs in i csv filen
        lf = pd.read_csv('recources1.csv')
        food = pd.DataFrame({"foodType":['Bread','Wheat','Meat','Water','Ale'],"foodAmount": [breadAmount,wheatAmount,meatAmount,waterAmount,aleAmount],
                             "Duration": [foodDuration1,foodDuration2,foodDuration3,foodDuration4,foodDuration5]})
        kf = pd.concat([lf, food], ignore_index=True)
        kf.to_csv('recources1.csv', index= False, encoding='utf-8')
