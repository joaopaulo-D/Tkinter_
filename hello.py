from tkinter import *

class App:
    def __init__(self, master = None):
        self.widget1 = Frame(master)
        self.widget1.pack()
        self.msg = Label(self.widget1, text="Hello World")
        self.msg.pack()

root = Tk()
App(root)
root.mainloop()
