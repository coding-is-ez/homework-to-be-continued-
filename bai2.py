# Import modules and widgets
import random
from guizero import App, Text, PushButton

# App
window = App(title = "Random Numbers", width = 200, height = 150)

# Function to random
txt = Text(window, text = "Waiting...", size = 30)

def rand_number():
    global txt
    num = random.randint(1, 100)
    txt.value = str(num)

# Intiate button
btn = PushButton(window, command = rand_number)

# Run app
window.display()