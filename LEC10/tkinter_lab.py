import logging

logging.basicConfig(
    filename='log.txt',
    # level=logging.INFO,
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# tkinter 레퍼런스 사이트
# https://anzeljg.github.io/rin2/book2/2405/docs/tkinter/index.html
from tkinter import *
from tkinter.ttk import *
from tkinter.scrolledtext import ScrolledText

window = Tk()


def stop(event=None):
    window.quit()


window.geometry('640x480+0+0')
window.resizable(False, False)

first_line_frame = Frame(window)
first_line_frame.pack()

label = Label(first_line_frame, text='Hello, Tkinter~~~')
label.pack(side=LEFT)   # 아무것도 없으면 top
# label.place(x=200, y=200)


def rotate(event=None):
    logging.info('Button Presed.')
    text = label.cget('text')
    text = text[1:] + text[0]
    label.config(text=text)


button = Button(first_line_frame, text='Rotate',  command=rotate)
button.pack(side=LEFT)


def delete(event=None):
    text_box.delete("1.0", END)


button_del = Button(first_line_frame, text='Delete', command=delete)
button_del.pack(side=LEFT)


def change_text(event=None):
    new_text = entry.get()
    label.config(text=new_text.center(50, ' '))
    text_box.insert(END, new_text)


entry = Entry(window, width=50)
entry.bind('<Return>', change_text)
entry.pack(side=TOP)

python_text = '''Python is a high-level, general-purpose programming language. Its design philosophy emphasizes code readability with the use of significant indentation.[31]
Python is dynamically typed and garbage-collected. It supports multiple programming paradigms, including structured (particularly procedural), object-oriented and functional programming. It is often described as a "batteries included" language due to its comprehensive standard library.[32][33]
Guido van Rossum began working on Python in the late 1980s as a successor to the ABC programming language and first released it in 1991 as Python 0.9.0.[34] Python 2.0 was released in 2000. Python 3.0, released in 2008, was a major revision not completely backward-compatible with earlier versions. Python 2.7.18, released in 2020, was the last release of Python 2.[35]
Python consistently ranks as one of the most popular programming languages, and has gained widespread use in the machine learning community.'''

text_box = ScrolledText(window, width=50, height=10, font=('Arial', 10))
text_box.insert(END, python_text)
text_box.pack(fill=BOTH, expand=True, padx=10, pady=10)

text_box.tag_config('found', background='yellow', foreground='red')
text_box.tag_add('found', '3.0+3chars', '3.0+10chars')

def cb_clicked():
    logging.info(f'{ignore_case.get()}')

ignore_case = IntVar()
case_checkbutton = Checkbutton(window, text='Ignore case', variable=ignore_case, command=cb_clicked)
ignore_case.set(0)
case_checkbutton.pack()

def found_color_updated(var, index, mode):
    logging.info(f'{var=} {mode=} {index=}')
    logging.info(f'{found_color.get()}')


found_color = StringVar(value='yellow')
# yellow_rb = Radiobutton(window, text='Yellow', variable=found_color)
# yellow_rb.pack()
Radiobutton(window, text='Yellow', value='yellow', variable=found_color).pack()
Radiobutton(window, text='Green', value='green', variable=found_color).pack()
Radiobutton(window, text='Red', value='red', variable=found_color).pack()
# text는 버튼에 써있는 거, value는 버튼을 선택했을 때의 값 => 녹색이 된다..
found_color.trace_add('write', found_color_updated)

label2 = Label(window, text='TEST')
entry.pack()

window.bind('<Escape>', stop)
window.mainloop()
