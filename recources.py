import pandas as pd 
import numpy as np 
import csv 


with open('recources1.csv', 'w', newline= '') as file:
        writer = csv.writer(file)
        writer.writerow(["Number", "Bread", "Wheat", "Meat", "Water", "Ale"])
        writer.writerow([1, 6, 19, 5, 20, 1])
        writer.writerow([2,'3months', '2,5months', '1,5months', '4months', '3weeks'])





def foodgeneration(): 


    foodstats = {
        'foodType' : ["Bread", "Wheat", "Meat", "Water", "Ale"],
        'foodAmount' : [6, 19, 5, 20, 1],
        'Duration' : ['3months', '2,5months', '1,5months', '4months', '3weeks']
    }

    df = pd.DataFrame(foodstats)
    
    df.to_csv("c:/Users/tim.clement/Desktop/TimClement4/recources1.csv", index=False)

foodgeneration()


