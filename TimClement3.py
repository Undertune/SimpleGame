from StatPlotting import graph 
import PySimpleGUI as sg 
import recources 



while True:

    layout = [[sg.Text('Test Fönster')],
                    [sg.InputText()],
                    [sg.Submit()],
                    [sg.Cancel()],
                    [sg.Button('help')]]

    window = sg.Window('Window Title', layout)

    event, values = window.read()
    text_input = values[0]

    if event == 'help':

        sg.popup('Du ska skriva in ditt namn')
        window.close()
        
    
    elif event == sg.Submit():
        sg.popup('You entered', text_input)
        graph()
        pass
    elif event == sg.Cancel():
        window.close()
        break
    window.close()
    break


  



















