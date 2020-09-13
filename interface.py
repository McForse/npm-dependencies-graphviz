from tkinter import *

from parser import NpmParser


def generate():
    code.delete('1.0', END)
    code.insert(1.0, str(NpmParser.getDependencies(dependence.get())))


root = Tk()
root.title("Npm dependencies")

dependence = StringVar()
dependence_entry = Entry(textvariable=dependence)
dependence_entry.pack()
button = Button(text='Generate', command=generate)
button.pack()
code = Text(width=50, height=10, bg="grey25", fg='white', wrap=WORD)
code.pack()

root.mainloop()
