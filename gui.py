import csv
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd


class Exit(tk.Frame):                                                   #Exit button class
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.frame = tk.Frame(self.parent)
        self.button = ttk.Button(
            self.parent,
            text='Exit',
            command=lambda: root.quit()
        )

class Databar(tk.Frame):                                                 #databar class. a radiobutton w/ 3 states
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.frame = tk.Frame(self.parent)
        self.textbody= tk.StringVar(value="State 1")
        self.s1button = tk.Radiobutton(self.frame, text="State 1", variable=self.textbody,
            indicatoron=False, value="State 1", width=32, command=self.onRadioChange)
        self.s2button = tk.Radiobutton(self.frame, text="State 2", variable=self.textbody,
            indicatoron=False, value="State 2", width=32, command=self.onRadioChange)
        self.s3button = tk.Radiobutton(self.frame, text="State 3", variable=self.textbody,
            indicatoron=False, value="State 3", width=32, command=self.onRadioChange)
        self.s1button.pack(side="left")
        self.s2button.pack(side="left")
        self.s3button.pack(side='left')
    
    def onRadioChange(self):
        #print(self.textbody.get())
        application.update()
        
    def getkey(self):
        return self.textbody.get()

class Main(tk.Frame):                                                    #main class, meant to hold a main body of text based on databar
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.frame = tk. Frame(self.parent)
        self.textbody = 'initialising'
        self.text = tk.Label(self.frame, text=self.textbody)
        self.text.pack()
    def set(self, body):
        self.textbody = body
        self.text.config(text=self.textbody)
        self.text.pack()

class Label(tk.Frame):                                                  #label class used for testing atm                                                    
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.frame = tk. Frame(self.parent)
        self.textbody ='Message Bar Text'
        self.text = tk.Label(self.frame, text=self.textbody)
        self.text.pack()
    def set(self, body):
        self.textbody = body
        self.text.config(text=self.textbody)
        self.text.pack()

class MainApplication(tk.Frame):                                        #MainApp class
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.databar = Databar(self)
        self.main = Main(self)
        self.label = Label(self)
        self.exit = Exit(self)

        self.Dict = {'State 1': 'This is the first section of text', 
                'State 2': 'This is body #2, there is one more state',
                'State 3': 'The third and final set of textual info'}
        
        self.update()

        #self.label.set('Hello World')
        #self.main.set(self.Dict[self.dictkey])
        #print(self.dictkey)
        
        self.databar.frame.pack(side='top')
        self.label.frame.pack(side='top')
        self.main.frame.pack(side='top')
        self.exit.button.pack(side='bottom')
    
    def update(self):
        self.dictkey = self.databar.getkey()
        self.main.set(self.Dict[self.dictkey])


if __name__ == "__main__":
    root = tk.Tk()
    application = MainApplication(root)
    application.pack(side="top", fill="both", expand=True)
    root.mainloop()