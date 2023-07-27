from pathlib import Path
import PySimpleGUI as sg
import pandas as pd

# Add some color to the window
sg.theme('DarkTeal9')

current_dir = Path(__file__).parent if '__file__' in locals() else Path.cwd()
EXCEL_FILE = current_dir / 'Data_Entry.xlsx'

# Load the data if the file exists, if not, create a new DataFrame
if EXCEL_FILE.exists():
    df = pd.read_excel(EXCEL_FILE)
else:
    df = pd.DataFrame()

layout = [
    [sg.Text('Please fill out the following fields:')],
    [sg.Text('Name', size=(15,1)), sg.InputText(key='Name')],
    [sg.Text('State', size=(15,1)), sg.Combo(['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming'
], key='State you live in')],
    [sg.Text('University', size=(15,1)), sg.Combo(['Columbia University', 'New York University', 'Cornell University', 'University at Buffalo', 'Syracuse University', 'Rochester Institute of Technology', 'Stony Brook University', 'Fordham University', 'Binghamton University', 'University of Rochester', 'Rensselaer Polytechnic Institute', 'Hofstra University', 'Pace University', 'Yeshiva University', 'The New School', 'St. John\'s University', 'University of Albany', 'Adelphi University', 'Buffalo State College', 'Brooklyn College', 'City College of New York'
], key='University of choice')],
    [sg.Submit(), sg.Button('Clear'), sg.Exit()]
]

window = sg.Window('Simple data entry form', layout)

def clear_input():
    for key in values:
        window[key]('')
    return None


while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == 'Clear':
        clear_input()
    if event == 'Submit':
        new_record = pd.DataFrame(values, index=[0])
        df = pd.concat([df, new_record], ignore_index=True)
        df.to_excel(EXCEL_FILE, index=False)  # This will create the file if it doesn't exist
        sg.popup('Data saved!')
        clear_input()
window.close()