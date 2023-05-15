#Import av bibliotek
import matplotlib.pyplot as plt 
import pandas as pd



#Funktionen för linje grafen för soldaterna
def graphS():
    columns = ['Attack', 'Defence']
    df = pd.read_csv('recources2.csv', usecols=(columns))
    df = df.sort_values('Defence', ascending=False)
    df.plot(x='Defence', y='Attack')
    plt.show()



#Funktionen för stapeldiagramet för soldaterna
def stapelGraphS():
    columns = ['Attack', 'Defence']
    df = pd.read_csv('recources2.csv', usecols=(columns))
    df = df.sort_values('Defence', ascending=False)
    df.plot(x='Defence', y='Attack', kind='bar')
    plt.show()
 


#Funktionen för cirkeldiagramet för soldaterna
def circleGraphS():
    columns = ['Attack', 'Defence']
    df = pd.read_csv('recources2.csv', usecols=(columns))
    df = df.sort_values('Defence', ascending=False)
    df.plot.pie(x='Defence', y='Attack', autopct='%1.1f%%', startangle=90)
    plt.show()
 

 
#Funktion för linjediagramet för maten
def graphF():
    columns = ['foodAmount', 'Duration']
    df = pd.read_csv('recources1.csv', usecols=(columns))
    df = df.sort_values('foodAmount', ascending=False)
    df.plot(y='Duration', x='foodAmount')
    plt.show()



#Funktionen för stapeldiagramet för maten
def stapelGraphF():
    columns = ['foodType', 'foodAmount']
    df = pd.read_csv('recources1.csv', usecols=(columns))
    df = df.sort_values('foodAmount', ascending=False)
    df.plot(x='foodType', y='foodAmount', kind='bar')
    plt.show()
 


#Funktionen för cirkeldiagramet för maten
def circleGraphF():
    columns = ['foodAmount', 'Duration']
    df = pd.read_csv('recources1.csv', usecols=(columns))
    df = df.sort_values('foodAmount', ascending=False)
    df.plot.pie(x='foodAmount', y='Duration', autopct='%1.1f%%', startangle=90)
    plt.show()
 