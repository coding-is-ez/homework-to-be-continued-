from guizero import App, PushButton, Box

window = App(title = "LED Control", width = 400, height = 300)

# Box containing LEDs + buttons
a_simple_box = Box(window, layout = "grid")

r_count = 0
g_count = 0
b_count = 0

# Set up functions
def red():
    global r_count
    global red_decoy_btn
    global red_btn
    if r_count % 2 != 0:
        red_decoy_btn.bg = red_btn.text.lower() # Set the color to text
    elif r_count % 2 == 0:
        red_decoy_btn.bg = "white" # Reset color
    r_count += 1

def green():
    global g_count
    global green_decoy_btn
    global green_btn
    if g_count % 2 != 0:
        green_decoy_btn.bg = green_btn.text.lower() # Set the color to text
    elif g_count % 2 == 0:
        green_decoy_btn.bg = "white" # Reset color
    g_count += 1

def blue():
    global b_count
    global blue_decoy_btn
    global blue_btn
    if b_count % 2 != 0:
        blue_decoy_btn.bg = blue_btn.text.lower() # Set the color to text
    elif b_count % 2 == 0:
        blue_decoy_btn.bg = "white" # Reset color
    b_count += 1

# Setting up btns
red_btn = PushButton(a_simple_box, grid = [0, 1], text = "    Red    ")
red_decoy_btn = PushButton(a_simple_box, grid = [0, 0], enabled = False, text = "              ")
green_btn = PushButton(a_simple_box, grid = [1, 1], text = "  Green  ")
green_decoy_btn = PushButton(a_simple_box, grid = [1, 0], enabled = False, text = "              ")
blue_btn = PushButton(a_simple_box, grid = [2, 1], text = "  Blue  ")
blue_decoy_btn = PushButton(a_simple_box, grid = [2, 0], enabled = False, text = "            ")

# Updating commands
red_btn.update_command(command = red)
green_btn.update_command(command = green)
blue_btn.update_command(command = blue)

# Run app
window.display()
