import matplotlib.pyplot as plt 
import pandas as pd


def graphS():
    columns = ['Attack', 'Defence']
    df = pd.read_csv('recources2.csv', usecols=(columns))
    df = df.sort_values('Defence', ascending=False)
    df.plot(x='Defence', y='Attack')
    plt.show()



def stapelGraphS():
    columns = ['Attack', 'Defence']
    df = pd.read_csv('recources2.csv', usecols=(columns))
    df = df.sort_values('Defence', ascending=False)
    df.plot(x='Defence', y='Attack', kind='bar')
    plt.show()
 


def circleGraphS():
    columns = ['Attack', 'Defence']
    df = pd.read_csv('recources2.csv', usecols=(columns))
    df = df.sort_values('Defence', ascending=False)
    df.plot.pie(x='Defence', y='Attack', autopct='%1.1f%%', startangle=90)
    plt.show()
 
 
def graphF():
    columns = ['foodAmount', 'Duration']
    df = pd.read_csv('recources1.csv', usecols=(columns))
    df = df.sort_values('foodAmount', ascending=False)
    df.plot(y='Duration', x='foodAmount')
    plt.show()



def stapelGraphF():
    columns = ['foodType', 'foodAmount']
    df = pd.read_csv('recources1.csv', usecols=(columns))
    df = df.sort_values('foodAmount', ascending=False)
    df.plot(x='foodType', y='foodAmount', kind='bar')
    plt.show()
 


def circleGraphF():
    columns = ['foodAmount', 'Duration']
    df = pd.read_csv('recources1.csv', usecols=(columns))
    df = df.sort_values('foodAmount', ascending=False)
    df.plot.pie(x='foodAmount', y='Duration', autopct='%1.1f%%', startangle=90)
    plt.show()
 