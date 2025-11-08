# Imports
from guizero import App, Text, PushButton, Box
import random

# Initiate app
window = App(title = "Rock Paper Scissors", width = 300, height = 200)

# Run app + text display
display_txt = Text(window ,text = "May one of the choices lead you to victory:")

# Rock paper scissors app
riel_choice = None
# Functions
# Text showing result
result = Text(window, text = "")


def lock_choice(btn : PushButton):
    global riel_choice
    global result
    # COM choose
    com_riel_choice = random.choice(["rock", "paper", "scissors"])

    # Assigning player's choice
    value = btn.text.lower()
    riel_choice = value
    result.value = "Human: " + riel_choice + " | " + "Computer: " + com_riel_choice + " | "

    if riel_choice == com_riel_choice: # Drawing
        result.value += "Result: You drawed!"
    elif (riel_choice == "rock" and com_riel_choice == "scissors") or (riel_choice == "paper" and com_riel_choice == "rock") or (riel_choice == "scissors" and com_riel_choice == "paper"):
        result.value += "Result: You won!"
    else:
        result.value += "Result: You lose!"
# Box contain btns
widget_box = Box(window, layout = "grid")

rock = PushButton(widget_box, text = "Rock", grid = [0, 0])
paper = PushButton(widget_box, text = "Paper", grid = [2, 0])
scissors = PushButton(widget_box, text = "Scissors", grid = [4, 0])
filler_1 = Text(widget_box, text = " | ", grid = [1, 0])
filler_2 = Text(widget_box, text = " | ", grid = [3, 0])
# Update commands
rock.update_command(command = lambda: lock_choice(rock)) # Only executed when btn is clicked, same as
paper.update_command(command = lambda: lock_choice(paper))# only creating the function, not immediately
scissors.update_command(command = lambda: lock_choice(scissors)) # executing it.

window.display()