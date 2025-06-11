import FreeSimpleGUI as sg
from feet_converter import convert

sg.theme("Black")

label1 = sg.Text("Enter feet: ")
input1 = sg.Input(tooltip="Enter feet", key="feet")

label2 = sg.Text("Enter inches: ")
input2 = sg.Input(tooltip="Enter inches", key="inches")

convert_button = sg.Button("Convert")
exit_button = sg.Button("Exit", key="Exit", tooltip="Exit program")

window = sg.Window("Feet to Meters Converter", layout=[[label1, input1], [label2, input2], [convert_button, exit_button]], font=("Helvetica", 10))

while True:
    event, values = window.read()

    feet = float(values["feet"])
    inches = float(values["inches"])

    result = convert(feet, inches)
    sg.popup(f"{feet} feet and {inches} inches is equal to {result:.2f} meters", title="Conversion Result")

    match event:
        case "Exit":
            break

window.close()
