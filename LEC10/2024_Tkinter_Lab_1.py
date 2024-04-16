import logging
logging.basicConfig(
    level=logging.INFO,
    format='%(filename)s(%(lineno)d): %(asctime)s - %(levelname)s - %(message)s'
)

from logging import info as info, debug as debug, warning as warning

from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog


window = Tk()
window.title('My First App')
window.geometry('800x600+0+0')
window.resizable(False, False)


label = Label(master=window, text='Hello, Tkinter~', font=('Segoe UI', 10))
label.pack()
# label.place(x=100, y=100)


def rotate():
    text = label.cget('text')
    text = text[1:] + text[0]
    label.config(text=text)

button = Button(master=window, text='Rotate', command=rotate)
button.pack()



def update_text(event=None):
    label.config(text=entry.get())

entry = Entry(master=window, font=('Segoe UI', 10))
entry.bind('<Return>', update_text)
entry.pack()



from tkinter.scrolledtext import ScrolledText

wiki_python = '''Python is a high-level, general-purpose programming language. Its design philosophy emphasizes code readability with the use of significant indentation.[31]
Python is dynamically typed and garbage-collected. It supports multiple programming paradigms, including structured (particularly procedural), object-oriented and functional programming. It is often described as a "batteries included" language due to its comprehensive standard library.[32][33]
Guido van Rossum began working on Python in the late 1980s as a successor to the ABC programming language and first released it in 1991 as Python 0.9.0.[34] Python 2.0 was released in 2000. Python 3.0, released in 2008, was a major revision not completely backward-compatible with earlier versions. Python 2.7.18, released in 2020, was the last release of Python 2.[35]
Python consistently ranks as one of the most popular programming languages, and has gained widespread use in the machine learning community.[36][37][38][39]
'''*2
text = ScrolledText(master=window, font=('Segoe UI', 10))
text.delete("1.0", END)
text.insert(END, wiki_python)
text.pack()

# tagging
text.tag_config('found', background='yellow', foreground='red')
text.tag_add('found', '3.0', '3.0+16chars')


def cb_clicked():
    info(f'checkbutton updated {checked.get()}')

checked = BooleanVar(value=True)
checkbutton = Checkbutton(master=window, text='CheckButton', command=cb_clicked, variable=checked)
checkbutton.pack()




def rb_clicked():
    info(f'checkbutton updated {color.get()}')

color = StringVar(value='red')
Radiobutton(master=window, text='RED', value='red', command=rb_clicked, variable=color).pack()
Radiobutton(master=window, text='GREEN', value='green', command=rb_clicked, variable=color).pack()
Radiobutton(master=window, text='BLUE', value='blue', command=rb_clicked, variable=color).pack()




window.bind('<Escape>', lambda e: window.quit())
window.mainloop()

