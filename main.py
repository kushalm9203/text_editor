from Tkinter import *
from tkFileDialog import *

filename = None

def newFile():
    global filename
    filename = "Untitled"
    text.delete(0.0, END)

def openFile():
    file = askopenfile(mode = 'r')
    t = file.read()
    text.delete(0.0, END)
    text.insert(0.0, t)
def saveFile():
    pass

def saveFileAs():
    pass

my_main = Tk()
my_main.title("Ktom Editor")
my_main.minsize(width=400, height=500)
my_main.minsize(width=400, height=500)

text = Text(my_main, width=400, height=500)
text.pack()

menubar = Menu(my_main)
filemenu = Menu(menubar)
menubar.add_cascade(label = "File", menu = filemenu) 
filemenu.add_command(label = "New File...", command = newFile)
filemenu.add_command(label = "Open File...", command = openFile)
filemenu.add_command(label = "Save", command = saveFile)
filemenu.add_command(label = "Save File As...", command = saveFileAs)
filemenu.add_separator()
filemenu.add_command(label = "Exit", command = my_main.quit)

my_main.config(menu = menubar)
my_main.mainloop()
