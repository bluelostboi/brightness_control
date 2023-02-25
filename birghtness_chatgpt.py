import PySimpleGUI as sg
import screen_brightness_control as sbc

# get the number of displays
num_displays = len(sbc.list_monitors())

# create a layout with sliders for each display
layout = []
for i in range(num_displays):
    layout.append([sg.Text(f"Display {i+1}")])
    layout.append([sg.Slider(range=(0, 100), orientation="h", key=f"slider{i}")])

layout.append([sg.Button("Apply")])

# create a window
window = sg.Window("Brightness Control", layout)

# event loop
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == "Apply":
        # set the brightness for each display according to slider values
        for i in range(num_displays):
            sbc.set_brightness(values[f"slider{i}"], display=i)

window.close()
