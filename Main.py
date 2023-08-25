import tkinter as tk
from tkinter import filedialog
import easygui
import numpy
from Internal import create_sheet

root = tk.Tk()
root.withdraw()

file = filedialog.askopenfilename(title='Select the spritesheet to rearrange.')

anchor = numpy.clip(easygui.integerbox('choose the sprite anchor (from 1 to 9 starting from the top-left hand corner going from left and right and then frop top to bottom)'), 1, 9)

path = file[:file.rfind('/') + 1]

create_sheet(file, anchor, path)