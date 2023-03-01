import os
from tkinter import *
from PIL import Image,ImageTk

# methods defined
def system():
    os.startfile(r'C:\WINDOWS\system32\cmd.exe')

def system1():
    os.startfile(r'C:\Users\Deepsoumya\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\System Tools\Run.lnk')

# Images to embed (local images)

img= (Image.open("F:\py_to_exe\images\cmd.png"))
resized_image= img.resize((60,40), Image.LANCZOS)

# Images to embed (virtual images)
"""
img= (Image.open("data\images\cmd.png"))
resized_image= img.resize((60,40), Image.LANCZOS)

img1= (Image.open("data\images\cmd.png"))
resized_image1= img1.resize((60,40), Image.LANCZOS)

img2= (Image.open("data\images\cmd.png"))
resized_image2= img2.resize((60,40), Image.LANCZOS)

img3= (Image.open("data\images\cmd.png"))
resized_image3= img3.resize((60,40), Image.LANCZOS)
"""