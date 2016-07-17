from Tkinter import *
from tkFileDialog import *


class TextEditor(object):
    def text_editor(self):
        filename = None
        self.my_main = Tk()
        self.my_main.title("Ktom Editor")
        self.my_main.minsize(width=400, height=500)
        self.my_main.maxsize(width=400, height=500)

        self.text = Text(self.my_main, width=400, height=500)
        self.text.pack()

        self.menubar = Menu(self.my_main)
        self.filemenu = Menu(self.menubar)

        self.menubar.add_cascade(label = "File", menu = self.filemenu)

        self.filemenu.add_command(label = "New File...", command = self.newFile)
        self.filemenu.add_command(label = "Open File...", command = self.openFile)
        self.filemenu.add_command(label = "Save", command = self.saveFile)
        self.filemenu.add_command(label = "Save File As...", command = self.saveFileAs)
        self.filemenu.add_separator()
        self.filemenu.add_command(label = "Exit", command = self.my_main.quit)

        self.editmenu = Menu(self.menubar)
        self.menubar.add_cascade(label = "Edit", menu = self.editmenu)
        #self.editmenu.add_command(label = "Cut", command =) 

        self.my_main.config(menu = self.menubar)
        self.my_main.mainloop()

    """create new file"""
    def newFile(self): 
        #global filename
        filename = "Untitled"
        self.text.delete(0.0, END)

    """open file""" 
    def openFile(self):
        fp = askopenfile(mode = 'r')
        t = fp.read()
        self.text.delete(0.0, END)
        self.text.insert(0.0, t)
    
    """update an existing file"""
    def saveFile():
        #global filename
        t = text.get(0.0, END)
        fp = open(filename, mode = 'w')
        fp.write(t)
        fp.close()

    """save a new file"""
    def saveFileAs():
        fp = asksaveasfile(mode = 'w', defaultextension = '.txt')
        t = text.get(0.0, END)
        fp.write(t.rstrip())
        fp.close()
