from StatPlotting import graph 
import PySimpleGUI as sg 
import recources as rc
import pandas as pd

def mainWindow():
    while True:

        layout = [[sg.Text('Test Fönster')],
                        [sg.InputText()],
                        [sg.Button('Submit')],
                        [sg.Button('Cancel')],
                        [sg.Button('help')],
                        [sg.Button('Dina Soldater')],
                        [sg.Button('Din mat')]]

        window = sg.Window('Window Title', layout)

        event, values = window.read()
        text_input = values[0]

        if event == 'help':
            sg.popup('Du ska skriva in ditt namn')
            window.close()
            pass
        
        elif event == 'Submit':
            sg.popup('You entered', text_input)
            graph()
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



df = pd.read_csv('recources2.csv')
table =  df
headings = list(df)
values = table.values.tolist()
sg.set_options(font=("Times new roman", 16))


def soldierWindow():
    while True: 
            
            df = pd.read_csv('recources2.csv')
            table =  df
            headings = list(df)
            values = table.values.tolist()
            sg.set_options(font=("Times new roman", 16))

            layout = [[sg.Button('Back')],
                      [sg.Table(values = values, headings = headings,
                auto_size_columns=False,
                col_widths=list(map(lambda x:len(x)+1, headings)))]]

            window = sg.Window('Soldier stats',  layout, size=(500,200))
            event, value = window.read()
            if event == 'Back':
                window.close()
                mainWindow()
                break

def foodWindow():
    while True: 
            
            df = pd.read_csv('recources1.csv')
            table =  df
            headings = list(df)
            values = table.values.tolist()
            sg.set_options(font=("Times new roman", 16))

            layout = [[sg.Button('Back')],
                      [sg.Table(values = values, headings = headings,
                auto_size_columns=False,
                col_widths=list(map(lambda x:len(x)+1, headings)))]]

            window = sg.Window('Food stats',  layout, size=(500,200))
            event, value = window.read()
            if event == 'Back':
                window.close()
                mainWindow()
                break



mainWindow()














