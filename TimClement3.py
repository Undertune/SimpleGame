#Import av funktioner och bibliotek
from StatPlotting import graphS, stapelGraphS, circleGraphS, graphF, stapelGraphF, circleGraphF
import PySimpleGUI as sg 
from recources import foodgeneration, soldierGeneration
import pandas as pd



#Funktionen för start fönstret
def mainWindow():

    while True:
        

        #Sätter Fönstrets font, text storlek och färg
        sg.set_options(font=("Times new roman", 16), )
        sg.change_look_and_feel('DarkBlue') 


        #Fönstrets layout med en text, en input box och fem knappar
        layout = [[sg.Text('Skriv in hur många år du vill simulera')],
                        [sg.InputText()],
                        [sg.Button('Ok')],
                        [sg.Button('Avbryt')],
                        [sg.Button('Hjälp')],
                        [sg.Button('Dina Soldater')],
                        [sg.Button('Din mat')]]


        #Skapar själva fönstret
        window = sg.Window('Meny Fönster', layout)

        #Anger variablerna values och event från det fönsret du skapat anger. Text input får en bas value.
        event, values = window.read()
        text_input = values[0]


        #En If sekvens som beror på vilken knapp du trycker på
        if event == 'Hjälp':
            window.close()
            sg.popup('Du ska skriva in i text fältet ett hel tal på hur många år du vill simulera', font=('Times new roman', 16))
            window.close()
            pass
        
        elif event == 'Ok':
            window.close()
            sg.popup('Du skrev in', text_input, font=('Times new roman', 16))
            soldierGeneration(int(text_input)*4)
            foodgeneration(int(text_input))
            pass

        elif event == 'Avbryt':
            window.close()
            break

        elif event == 'Dina Soldater':
            window.close()
            soldierWindow()
            break

        elif event == 'Din mat':
            window.close()
            foodWindow()
            break

        else:
            pass



#Funktionen för fönsret där du väljer vilken graf du vill se av dina soldater. 
def graphSoldier():

     while True:


        #Sätter Fönstrets font, text storlek och färg
        sg.set_options(font=("Times new roman", 16))
        sg.change_look_and_feel('DarkBlue')


        #Fönstrets layout med en text, en droppdown meny och tre knappar
        layout = [[sg.Text('Här kan du välja hur du ska få en visulisation av dina soldaters prestanda')],
                  [sg.Text('Välj din typ av diagram')],
                  [sg.Combo(['Stapel Diagram','Graf','cirkelDiagram'], key='Diagram')],
                  [sg.Button('Fortsätt')],
                  [sg.Button('Tillbaka')],
                  [sg.Button('Hjälp')]]


        #Det är här fönstret skapas och även designerar vart variabler ska få sina värden och en som får ett värde designerat. 
        window = sg.Window('Window Title', layout)
        event, values = window.read()
        val = 0


        #En if sekvens som bestämmer vad som händer beroende vad du väljer i drop down menyn och vilken knapp du trycker på. 
        if event == 'Fortsätt': 
             val = values['Diagram']

        elif event == 'Tillbaka':
            window.close()
            soldierWindow()
            break

        elif event == 'Hjälp': 
            window.close()
            sg.popup('Om talet för åren var för stort och datan är väldigt ihop tryck använd förstorings glaset i fönstret för att zooma in', font=('Times new roman', 16))
            graphSoldier()

        if val == 'Stapel Diagram':
            window.close()
            stapelGraphS()

        elif val == 'Graf':
             window.close()
             graphS()

        elif val == 'cirkelDiagram':
             window.close()
             circleGraphS()
        else: 
            break



#En funktion för fönstrest där du väljer vilken grav du vill se av din mat data.
def graphFood():

    while True:


        #Sätter Fönstrets font, text storlek och färg
        sg.set_options(font=("Times new roman", 16))
        sg.change_look_and_feel('DarkBlue')


        #Fönstrets layout med en text, en droppdown meny och tre knappar
        layout = [[sg.Text('Välj vilken typ av diagram du vill visualisera din mat i')],
                  [sg.Combo(['Stapel Diagram','Graf','cirkelDiagram'], key='Diagram')],
                  [sg.Button('Fortsätt')],
                  [sg.Button('Tillbaka')],
                  [sg.Button('Hjälp')]]
        

        #Det är här fönstret skapas och även designerar vart variabler ska få sina värden och en som får ett värde designerat.
        window = sg.Window('Window Title', layout)
        event, values = window.read()
        val = 0


        #En if sekvens som bestämmer vad som händer beroende vad du väljer i drop down menyn och vilken knapp du trycker på. 
        if event == 'Fortsätt': 
            val = values['Diagram']

        elif event == 'Tillbaka':
            window.close()
            foodWindow()
            break

        elif event == 'Hjälp': 
            window.close()
            sg.popup('Om talet för åren var för stort och datan är väldigt ihop tryck använd förstorings glaset i fönstret för att zooma in',
                    font=('Times new roman', 16))
            graphFood()

        if val == 'Stapel Diagram':
            window.close()
            stapelGraphF()

        elif val == 'Graf':
            window.close()
            graphF()

        elif val == 'cirkelDiagram':
            window.close()
            circleGraphF()
        else: 
            break  



#En funktion för fönstret där du ser din lista av data för dina soldater
def soldierWindow():

    while True: 
        

            #Skapar en dataframe och lista. Ändrar även font och tema. 
            df = pd.read_csv('recources2.csv')
            table =  df
            headings = list(df)
            values = table.values.tolist()
            sg.set_options(font=("Times new roman", 16))
            sg.change_look_and_feel('DarkBlue')


            #Fönstrets layout med två knappar och en table. 
            layout = [[sg.Button('Tillbaka')],
                      [sg.Button('Visualisera')],
                      [sg.Table(values = values, headings = headings,
                        auto_size_columns=False,
                        col_widths=list(map(lambda x:len(x)+1, headings)))]]


            #Det är här fönstret skapas med namn, layout och storlek. 
            # Designerar även vart variablerna event och values ska få sina värden.
            window = sg.Window('Soldier stats',  layout, size=(500,200))
            event, values = window.read()


            #En if sekvens som kollar vilken knapp man trycker på.
            if event == 'Tillbaka':
                window.close()
                mainWindow()
                break

            elif event == 'Visualisera':
                 window.close()
                 graphSoldier()
                 break
            


#En funktion för fönstret där du ser din lista av data för din mat
def foodWindow():

    while True: 
            

            #Skapar en data frame och lista. Ändrar även font och tema.
            df = pd.read_csv('recources1.csv')
            table =  df
            headings = list(df)
            values = table.values.tolist()
            sg.set_options(font=("Times new roman", 16))
            sg.change_look_and_feel('DarkBlue')


            #Fönstrets layout med två knappar och en table.
            layout = [[sg.Button('Tillbaka')],
                      [sg.Button('Visualisera')],
                      [sg.Table(values = values, headings = headings,
                        auto_size_columns=False,
                        col_widths=list(map(lambda x:len(x)+1, headings)))]]


            #Det är här fönstret skapas med namn, layout och storlek. 
            # Designerar även vart variablerna event och values ska få sina värden.
            window = sg.Window('Food stats',  layout, size=(500,200))
            event, values = window.read()


            #En if sekvens som kollar vilken knapp man trycker på.
            if event == 'Tillbaka':
                window.close()
                mainWindow()
                break

            elif event == 'Visualisera':
                 window.close()
                 graphFood()
                 break




if __name__ == "__main__": 
    mainWindow()












