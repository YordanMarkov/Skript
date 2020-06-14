import tkinter as tk 
from tkinter import *
from tkinter import messagebox
from tkinter import scrolledtext
from tkinter import ttk
import yaml, json, sys
window = Tk()
window.title("To JSON or YAML")
window.geometry('750x350')
lbl = Label(window, text="Enter directory:")
lbl.grid(column=0, row=0)
txt = Entry(window,width=10)
txt.grid(column=1, row=0)
def JSON():
    with open(r'{}'.format(txt.get())) as file:
        json_data = yaml.full_load(file)
    text_area.insert(tk.INSERT, "{}".format(json.dumps(json_data, indent=4))) 
def YAML():
    with open('{}'.format(txt.get())) as f:
        yaml_data = json.load(f)
    text_area.insert(tk.INSERT, "{}".format(yaml.dump(yaml_data)))
btn = Button(window, text="To JSON", command=JSON)
btn.grid(column=2, row=0)
btn = Button(window, text="To YAML", command=YAML)
btn.grid(column=3, row=0)

text_area = scrolledtext.ScrolledText(window,  
                                      wrap = tk.WORD,  
                                      width = 40,  
                                      height = 10,  
                                      font = ("Sans Serif", 
                                              12)) 
  
text_area.grid(column = 0, pady = 10, padx = 10) 
text_area.focus() 
window.mainloop()
