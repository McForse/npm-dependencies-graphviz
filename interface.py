from tkinter import *

from parser import NpmParser


def generate():
    code.configure(state='normal')
    code.delete('1.0', END)
    code.insert(1.0, str(NpmParser.getDependenciesJson(dependence.get())))
    code.configure(state='disabled')


root = Tk()
root.title('Npm dependencies')

label1 = Label(text='Enter package name:')
label1.pack()

dependence = StringVar()
dependence_entry = Entry(textvariable=dependence)
dependence_entry.pack()

button = Button(text='Generate', command=generate)
button.pack()

code = Text(width=50, height=10, bg='grey25', fg='white', wrap=WORD)
code.configure(state='disabled')
code.pack()

root.mainloop()
