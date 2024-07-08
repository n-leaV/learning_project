import numpy as np
import csv
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd


class Exit(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.frame = tk.Frame(self.parent)
        self.button = ttk.Button(
            self.parent,
            text='Exit',
            command=lambda: root.quit()
        )
        #self.button.pack(side='right')

class Databar(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.frame = tk.Frame(self.parent)
        #self.frame.pack(side='top')

        self.textbody= tk.StringVar(value="State 1")
        self.s1button = tk.Radiobutton(self.frame, text="State 1", variable=self.textbody,
            indicatoron=False, value="State 1", width=32)
        self.s2button = tk.Radiobutton(self.frame, text="State 2", variable=self.textbody,
            indicatoron=False, value="State 2", width=32)
        self.s1button.pack(side="left")
        self.s2button.pack(side="left")

class Main(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.frame = tk. Frame(self.parent)
        Dict = {'State 1': 'This is the first section of text', 'State 2':'This is body #2, there is one more state',
                'State 3': 'The third and final set of textual data'}
        self.textbody = Dict[kwargs['body']]
        self.text = tk.Label(self.frame, textvariable=self.textbody)

class MainApplication(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.databar = Databar(self)
        self.main = Main(self, parent, body=self.databar.textbody)
        self.exit = Exit(self)

        self.databar.frame.pack(side='top')
        self.main.frame.pack(side='top')
        self.exit.button.pack(side='bottom')

       # <create the rest of your GUI here>

if __name__ == "__main__":
    root = tk.Tk()
    MainApplication(root).pack(side="top", fill="both", expand=True)
    root.mainloop()