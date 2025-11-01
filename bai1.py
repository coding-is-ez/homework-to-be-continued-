# Import widgets from guizero
from guizero import App, Text, PushButton, Box

# Initiate app
window = App(title = "Quiz App", width = 300, height = 200, layout = "grid")
window.bg = "white"

# Header box + quiz
header = Box(window, layout = "grid", grid = [0, 0])
q = Text(header, text = "What is the capital of Vietnam?", grid = [0, 0])

# Answer + logic check (if answer correct -> bg turns green and vice versa for wrong -> red)
answer_box = Box(window, align = "bottom", grid = [0, 1], layout = "grid")

def logic_check(ans_btn : PushButton):
    if ans_btn.text == "Hanoi":
        return True
    else:
        return False

def change_screen_color(ans_btn : PushButton):
    if logic_check(ans_btn) == True:
        window.bg = "green"
    elif logic_check(ans_btn) == False:
        window.bg = "red"
real_btn_1 = PushButton(answer_box, text = "Hanoi", grid = [0, 0]) 
real_btn_2 = PushButton(answer_box, text = "Danang City", grid = [0, 1])
real_btn_3 = PushButton(answer_box, text = "Saigon City", grid = [0, 2])

# Update the command for each one
real_btn_1.update_command(command = change_screen_color, args = [real_btn_1])
real_btn_2.update_command(command = change_screen_color, args = [real_btn_2])
real_btn_3.update_command(command = change_screen_color, args = [real_btn_3])

# Run app
window.display()