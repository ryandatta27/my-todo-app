import FreeSimpleGUI as sg

import sys
sys.path.append('./bonus')
from zip_creator import make_archive


label1 = sg.Text("Select files to compress: ")
input1 = sg.Input()   
choose_button1 = sg.FilesBrowse("Choose", key="Files")

label2 = sg.Text("Select destination folder: ")
input2 = sg.Input()   
choose_button2 = sg.FolderBrowse("Choose", key="Folder")

compress_button = sg.Button("Compress")

window = sg.Window("My File Compression App", layout=[[label1, input1, choose_button1], [label2, input2, choose_button2],[compress_button]], font=("Helvetica", 10))


while True:
    event, values = window.read()
    print(event)
    print(values)
    filepaths = values["Files"].split(";")
    folder = values["Folder"]
    make_archive(filepaths, folder)

    sg.popup("Files compressed successfully!", title="Success")
    if event == sg.WIN_CLOSED or event == "Exit":
        break

window.close()
