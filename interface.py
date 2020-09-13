from tkinter import *
from parser import NpmParser
from graphviz import Graphviz


def generate():
    code.configure(state='normal')
    code.delete('1.0', END)
    code.insert(1.0, Graphviz.generateText(NpmParser.getPackage(package_name.get())))


root = Tk()
root.title('Npm dependencies')

label1 = Label(text='Enter package name:')
label1.pack()

package_name = StringVar()
package_entry = Entry(textvariable=package_name)
package_entry.pack()

button = Button(text='Generate', command=generate)
button.pack()

code = Text(width=80, height=40, font=('Menlo', 14), bg='grey25', fg='white', wrap=WORD)
code.configure(state='disabled')
code.pack()

root.mainloop()
