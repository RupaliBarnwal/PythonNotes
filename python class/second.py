"""
    This is a basic tkinter application
"""
#%%writefile first_app.py
# code
#!python first_app.py 

import tkinter as tk
# python module to create desktop application
# wxpython, kivi, PyQt

master = tk.Tk()
# Tk() class is used to create master window

hello_label = tk.Label(master,
        text="Hello World",
        font=('Monospace', 30, 'bold'),
        fg='white', bg='black')
hello_label.pack()
# to attach your label widget to master window

button = tk.Button(master,
        text='Exit',
        command=lambda :master.destroy())
# master.destroy()-> call -> None
# master.destroy
button.config(
        fg='black', bg='white',
        font=("Times", 30, 'bold')
        )

button.pack()

master.wm_minsize(400, 400)
master.wm_maxsize(400, 400)
#icon on master window so use ico
master.iconbitmap('images/master.ico')
master.title('MyFirstApplication')
# updating title of your master window
master.mainloop()
# it holds your master window unitll you quit
# or you destroy your master window
