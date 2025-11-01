# Import the features
from guizero import App, Text, Picture, PushButton, Box
import PIL

# Functions
def resize(pic_name):
    (pic_name + ".jpg").resize(200, 150)

def change_pic(pic_name):
    global picture
    picture.image = pic_name + ".jpg"
# Initiate app
window = App(title = "Image Viewer", width = 400, height = 350)

# Picture box
pic_box = Box(window, align = "top")

picture = Picture(pic_box, image = None)

# Initiate btn
btn_box = Box(window, align = "bottom")

cat_btn = PushButton(btn_box, command = change_pic, args = ["cat"], text = "Cat ")
dog_btn = PushButton(btn_box, command = change_pic, args = ["dog"], text = "Dog ")
bird_btn = PushButton(btn_box, command = change_pic, args = ["bird"], text = "Bird")

# Display
window.display()