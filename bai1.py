# Import GUI essentials
from guizero import App, Text, Box, TextBox, Combo, ButtonGroup, PushButton, info # + tenary operator

# Function
def display():
    global name_output, class_output, gender_output
    global name_entry, class_entry, gender_entry
    
    info(title = "Notification", text = "You must enter a name!") if name_entry.value == "" else text_assigning()

def text_assigning():
    global name_output, class_output, gender_output
    global name_entry, class_entry, gender_entry

    name_output.value = name_entry.value
    class_output.value = class_entry.value
    gender_output.value = gender_entry.value

    

# GUI
window = App(title = "Display information")

# Info entry box
entry_box = Box(window, layout = "grid")
txt1 = Text(entry_box, text = "Full name: ", grid = [0 ,0])
name_entry = TextBox(entry_box, width = 30, grid = [1, 0])
txt2 = Text(entry_box, text = "Class: 10A", grid = [0, 1])
class_entry = Combo(entry_box, grid =[1, 1], options = [i for i in range(1, 16)])
txt3 = Text(entry_box, text = "Gender: ", grid =[0, 2])
gender_entry = ButtonGroup(entry_box, grid =[1, 2], options =["Male", "Female", "Other"])

display_btn = PushButton(window, command = display, width = 10, height = 1, text = "Display")

display_box = Box(window, layout = "grid")
tx4 = Text(display_box, grid = [0, 0], text = txt1.value)
name_output = Text(display_box, grid = [1, 0], text = "")
txt5 = Text(display_box, grid = [0, 1], text = txt2.value)
class_output = Text(display_box, grid = [1, 1], text = "")
txt6 = Text(display_box, grid = [0, 2], text = txt3.value)
gender_output = Text(display_box, grid = [1, 2], text = "")

window.display()
