from StatPlotting import graphS, stapelGraphS, circleGraphS, graphF, stapelGraphF, circleGraphF
import PySimpleGUI as sg 
import recources as rc
from recources import foodgeneration, soldierGeneration
import pandas as pd



def mainWindow():
    while True:

        layout = [[sg.Text('Skriv in hur många år du vill simulera')],
                        [sg.InputText()],
                        [sg.Button('Submit')],
                        [sg.Button('Cancel')],
                        [sg.Button('help')],
                        [sg.Button('Dina Soldater')],
                        [sg.Button('Din mat')]]

        window = sg.Window('Meny Fönster', layout)

        event, values = window.read()
        text_input = values[0]

        if event == 'help':
            window.close()
            sg.popup('Du ska skriva in i text fältet ett hel tal på hur många år du vill simulera')
            window.close()
            pass
        
        elif event == 'Submit':
            window.close()
            sg.popup('You entered', text_input)
            soldierGeneration(int(text_input)*4)
            foodgeneration(int(text_input))

            pass

        elif event == 'Cancel':
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



def graphSoldier():
     while True:
        layout = [[sg.Text('Här kan du välja hur du ska få en visulisation av dina soldaters prestanda')],
                  [sg.Text('Välj din typ av diagram')],
                  [sg.Combo(['Stapel Diagram','Graf','cirkelDiagram'], key='Diagram')],
                  [sg.Button('Fortsätt')],
                  [sg.Button('Tillbaka')],
                  [sg.Button('Help')]]

        window = sg.Window('Window Title', layout)
        event, values = window.read()
        val = 0

        if event == 'Fortsätt': 
             val = values['Diagram']

        elif event == 'Tillbaka':
            window.close()
            soldierWindow()
            break

        elif event == 'Help': 
            window.close()
            sg.popup('Om talet för åren var för stort och datan är väldigt ihop tryck använd förstorings glaset i fönstret för att zooma in')
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

def graphFood():

    while True:
        layout = [[sg.Text('Välj vilken typ av diagram du vill visualisera din mat i')],
                  [sg.Combo(['Stapel Diagram','Graf','cirkelDiagram'], key='Diagram')],
                  [sg.Button('Fortsätt')],
                  [sg.Button('Tillbaka')],
                  [sg.Button('Help')]]
        
        window = sg.Window('Window Title', layout)
        event, values = window.read()
        val = 0


        if event == 'Fortsätt': 
            val = values['Diagram']

        elif event == 'Tillbaka':
            window.close()
            foodWindow()
            break
        elif event == 'Help': 
            window.close()
            sg.popup('Om talet för åren var för stort och datan är väldigt ihop tryck använd förstorings glaset i fönstret för att zooma in')
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






def soldierWindow():

    while True: 
            
            df = pd.read_csv('recources2.csv')
            table =  df
            headings = list(df)
            values = table.values.tolist()
            sg.set_options(font=("Times new roman", 16))

            layout = [[sg.Button('Tillbaka')],
                      [sg.Button('Visualisera')],
                      [sg.Table(values = values, headings = headings,
                        auto_size_columns=False,
                        col_widths=list(map(lambda x:len(x)+1, headings)))]]

            window = sg.Window('Soldier stats',  layout, size=(500,200))
            event, values = window.read()

            if event == 'Tillbaka':
                window.close()
                mainWindow()
                break

            elif event == 'Visualisera':
                 window.close()
                 graphSoldier()
                 break
            


def foodWindow():

    while True: 
            
            df = pd.read_csv('recources1.csv')
            table =  df
            headings = list(df)
            values = table.values.tolist()
            sg.set_options(font=("Times new roman", 16))

            layout = [[sg.Button('Back')],
                      [sg.Button('Visualisera')],
                      [sg.Table(values = values, headings = headings,
                        auto_size_columns=False,
                        col_widths=list(map(lambda x:len(x)+1, headings)))]]

            window = sg.Window('Food stats',  layout, size=(500,200))
            event, values = window.read()

            if event == 'Back':
                window.close()
                mainWindow()
                break

            elif event == 'Visualisera':
                 window.close()
                 graphFood()
                 break

if __name__ == "__main__": 
    mainWindow()












