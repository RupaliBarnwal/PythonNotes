import tkinter as tk

root = tk.Tk()
# Tk() is used to create root window

#jpeg, png are not allowed as icon image you have to use .ico files(bitmap)
#root.iconbitmap('fname')
ph = tk.PhotoImage(file='images/master.png')
root.iconphoto(False, ph)
root.title("My First Application Ever")
root.geometry('400x400')
root.wm_maxsize(400, 400)
root.wm_minsize(300, 300)
# title of our master window
root.mainloop()
# to hold our application untill we close it